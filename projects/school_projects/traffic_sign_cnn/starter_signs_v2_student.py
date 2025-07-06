# Import libraries
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
import os
import urllib.request
import zipfile
import shutil
from torchvision.datasets import ImageFolder
from torch.utils.data import Dataset
from PIL import Image
from torch.utils.data import ConcatDataset
import random


# URLs to download
file_urls = [
    "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/training1.zip",
    "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/training2.zip",
    "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/holdout.zip",
    "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/mini_holdout.zip",
    "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/mini_holdout_answers.csv"
]

# Download files
print("Downloading files...")
for url in file_urls:
    filename = url.split("/")[-1]
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
    else:
        print(f"{filename} already exists, skipping download.")

# Unzip files
print("Unzipping files...")
for zip_filename in ["training1.zip", "training2.zip", "holdout.zip", "mini_holdout.zip"]:
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall()

# Merge training directories
print("Merging training data...")
os.makedirs("training", exist_ok=True)

for folder in ["training1", "training2"]:
    for filename in os.listdir(folder):
        src_path = os.path.join(folder, filename)
        dst_path = os.path.join("training", filename)
        shutil.move(src_path, dst_path)
    os.rmdir(folder)

# Cleanup zip files
print("Cleaning up...")
for zip_filename in ["training1.zip", "training2.zip", "holdout.zip", "mini_holdout.zip"]:
    os.remove(zip_filename)

print("Data ready.")


id_to_name = {
    '00000': 'Speed_20',
    '00001': 'Speed_30',
    '00002': 'Speed_50',
    '00003': 'Speed_60',
    '00004': 'Speed_70',
    '00005': 'Speed_80',
    '00006': 'Speed_Limit_Ends',
    '00007': 'Speed_100',
    '00008': 'Speed_120',
    '00009': 'Overtaking_Prohibited',
    '00010': 'Overtaking_Prohibited_Trucks',
    '00011': 'Priority',
    '00012': 'Priority_Road_Ahead',
    '00013': 'Yield',
    '00014': 'STOP',
    '00015': 'Entry_Forbidden',
    '00016': 'Trucks_Forbidden',
    '00017': 'No_Entry(one-way traffic)',
    '00018': 'General Danger(!)',
    '00019': 'Left_Curve_Ahead',
    '00020': 'Right_Curve_Ahead',
    '00021': 'Double_Curve',
    '00022': 'Poor_Surface_Ahead',
    '00023': 'Slippery_Surface_Ahead',
    '00024': 'Road_Narrows_On_Right',
    '00025': 'Roadwork_Ahead',
    '00026': 'Traffic_Light_Ahead',
    '00027': 'Warning_Pedestrians',
    '00028': 'Warning_Children',
    '00029': 'Warning_Bikes',
    '00030': 'Ice_Snow',
    '00031': 'Deer_Crossing',
    '00032': 'End_Previous_Limitation',
    '00033': 'Turning_Right_Compulsory',
    '00034': 'Turning_Left_Compulsory',
    '00035': 'Ahead_Only',
    '00036': 'Straight_Or_Right_Mandatory',
    '00037': 'Straight_Or_Left_Mandatory',
    '00038': 'Passing_Right_Compulsory',
    '00039': 'Passing_Left_Compulsory',
    '00040': 'Roundabout',
    '00041': 'End_Overtaking_Prohibition',
    '00042': 'End_Overtaking_Prohibition_Trucks',
}


image_size = (100, 100)
batch_size = 32
num_copies = 10
data_dir = '/content/training'
semantic_targets = ['Stop', 'SpeedLimit30', 'Speed_30', 'Speed_50', 'Speed_60', 'Speed_70', 'Speed_80', 'Warning_Pedestrians', 'Warning_Children', 'Warning_Bikes', 'STOP','Entry_Forbidden', 'Trucks_Forbidden', 'No_Entry(one-way traffic)', 'General Danger(!)']

name_to_id = {v: k for k, v in id_to_name.items()}
target_class_names = [name_to_id[name] for name in semantic_targets if name in name_to_id]

train_transform = transforms.Compose([
    transforms.Resize(image_size),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(degrees=15),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
    transforms.RandomApply([transforms.GaussianBlur(kernel_size=3)], p=0.2),
    transforms.ToTensor(),
])

val_transform = transforms.Compose([
    transforms.Resize(image_size),
    transforms.ToTensor()
])

base_dataset = datasets.ImageFolder(root=data_dir, transform=train_transform)
class_to_idx = base_dataset.class_to_idx
target_class_ids = [class_to_idx[name] for name in target_class_names if name in class_to_idx]

target_samples = [sample for sample in base_dataset.samples if sample[1] in target_class_ids]

class AugmentedSubset(Dataset):
    def __init__(self, samples, transform):
        self.samples = samples
        self.transform = transform

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        path, label = self.samples[idx]
        image = Image.open(path).convert('RGB')
        image = self.transform(image)
        return image, label

combined_dataset = []
for _ in range(num_copies):
    random.shuffle(target_samples)
    subset = AugmentedSubset(target_samples, transform=train_transform)
    combined_dataset.append(subset)

final_train_dataset = ConcatDataset([base_dataset] + combined_dataset)

train_size = int(0.8 * len(final_train_dataset))
val_size = len(final_train_dataset) - train_size
train_dataset, val_dataset = random_split(final_train_dataset, [train_size, val_size], generator=torch.Generator().manual_seed(42))

val_dataset.dataset.transform = val_transform

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader   = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)


print("Number of training samples:", len(final_train_dataset))
print("Number of validation samples:", len(val_dataset))


target_names = ['Speed_20', 'Speed_30', 'Speed_50', 'Speed_60', 'Speed_70',
               'Speed_80','Speed_Limit_Ends', 'Speed_100', 'Speed_120', 'Overtaking_Prohibited',
               'Overtakeing_Prohibited_Trucks', 'Priority', 'Priority_Road_Ahead', 'Yield', 'STOP',
               'Entry_Forbidden', 'Trucks_Forbidden', 'No_Entry(one-way traffic)', 'General Danger(!)', 'Left_Curve_Ahead',
               'Right_Curve_Ahead', 'Double_Curve', 'Poor_Surface_Ahead', 'Slippery_Surface_Ahead', 'Road_Narrows_On_Right',
               'Roadwork_Ahead', 'Traffic_Light_Ahead', 'Warning_Pedestrians', 'Warning_Children', 'Warning_Bikes',
               'Ice_Snow', 'Deer_Crossing', 'End_Previous_Limitation', 'Turning_Right_Compulsory', 'Turning_Left_Compulsory',
               'Ahead_Only', 'Straight_Or_Right_Mandatory', 'Straight_Or_Left_Mandatory', 'Passing_Right_Compulsory', 'Passing_Left_Compulsory',
               'Roundabout', 'End_Overtaking_Prohibition', 'End_Overtaking_Prohibition_Trucks']
print(len(target_names))


class TrafficSignCNN(nn.Module):
    def __init__(self, num_classes):
        super(TrafficSignCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.conv3 = nn.Conv2d(32, 64, 3, padding=1)
        self.fc1 = nn.Linear(64 * 12 * 12, 128)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 64 * 12 * 12)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


    def evaluate_model(self, data_loader, device='cpu'):
        self.eval()
        print("Evaluating model...")
        correct, total = 0, 0
        with torch.no_grad():
            for images, labels in data_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = self(images)
                _, predicted = torch.max(outputs, 1)
                correct += (predicted == labels).sum().item()
                total += labels.size(0)
        return 100 * correct / total

    def train_model(self, train_loader, val_loader, criterion, optimizer, num_epochs=200, device='cpu', patience=10):
        self.to(device)
        print("Training model...")

        print("Original dataset size:", len(base_dataset))
        print("Final training dataset size:", len(final_train_dataset))
        print("Train split size:", len(train_dataset))
        print("Validation split size:", len(val_dataset))
        print("Train batches per epoch:", len(train_loader))

        train_losses = []
        val_accuracies = []

        best_val_acc = 0.0
        epochs_no_improve = 0
        best_model_state = None

        for epoch in range(num_epochs):
            self.train()
            running_loss = 0.0
            correct, total = 0, 0

            for images, labels in tqdm(train_loader, desc=f"Epoch {epoch+1}"):
                images, labels = images.to(device), labels.to(device)
                optimizer.zero_grad()
                outputs = self(images)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()

                running_loss += loss.item()
                _, predicted = torch.max(outputs, 1)
                correct += (predicted == labels).sum().item()
                total += labels.size(0)

            average_loss = running_loss / len(train_loader)
            train_acc = 100 * correct / total
            val_acc = self.evaluate_model(val_loader, device)

            train_losses.append(average_loss)
            val_accuracies.append(val_acc)

            scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)
            scheduler.step()

            print(f"Epoch [{epoch+1}/{num_epochs}], Average Loss: {average_loss:.4f}, Train Acc: {train_acc:.2f}%, Val Acc: {val_acc:.2f}%")

            if val_acc > best_val_acc:
                best_val_acc = val_acc
                best_model_state = self.state_dict()
                epochs_no_improve = 0
            else:
                epochs_no_improve += 1
                if epochs_no_improve >= patience:
                    print(f"Early stopping at epoch {epoch+1}")
                    break

        if best_model_state:
            self.load_state_dict(best_model_state)

        return train_losses, val_accuracies


    def save_model(self, path='traffic_sign_cnn.pth'):
        print("Saving model...")
        torch.save(self.state_dict(), path)
        print(f"Model saved to {path}")

    def load_model(model, path='traffic_sign_cnn.pth', device='cpu'):
        print("Loading model...")
        model.load_state_dict(torch.load(path, map_location=device))
        model.to(device)
        model.eval()
        print("Model loaded.")
        return model


num_classes = len(target_names)
traffic_sign_classifier = TrafficSignCNN(num_classes)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(traffic_sign_classifier.parameters(), lr=0.001, weight_decay=1e-4)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
train_losses, val_accuracies = traffic_sign_classifier.train_model(train_loader, val_loader, criterion, optimizer, num_epochs=200, device=device)


traffic_sign_classifier.save_model()


traffic_sign_classifier = TrafficSignCNN.load_model(traffic_sign_classifier, path='traffic_sign_cnn.pth', device=device)


def evaluate_model(model, dataloader, class_names, device='cpu'):
    model.eval()
    all_preds = []
    all_labels = []

    # Collect predictions and labels
    with torch.no_grad():
        for images, labels in dataloader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, preds = torch.max(outputs, 1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    # Create confusion matrix
    cm = confusion_matrix(all_labels, all_preds, labels=list(range(len(class_names))))

    # Per-class evaluation
    report = []
    for i, class_name in enumerate(class_names):
        TP = cm[i, i]
        FP = cm[:, i].sum() - TP
        FN = cm[i, :].sum() - TP
        TN = cm.sum() - (TP + FP + FN)

        accuracy = (TP + TN) / cm.sum() if cm.sum() > 0 else 0
        precision = TP / (TP + FP) if (TP + FP) > 0 else 0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0

        # Most common misclassification
        misclassified_as = None
        misclassified_count = 0
        row = cm[i, :].copy()
        row[i] = 0  # zero out correct predictions
        if row.sum() > 0:
            misclassified_as_idx = np.argmax(row)
            misclassified_as = class_names[misclassified_as_idx]
            misclassified_count = row[misclassified_as_idx]

        report.append({
            'Class': class_name,
            'TP': TP,
            'FP': FP,
            'FN': FN,
            'TN': TN,
            'Accuracy': round(accuracy, 4),
            'Precision': round(precision, 4),
            'Recall': round(recall, 4),
            'Misclassified As': misclassified_as,
            'Misclassified Count': misclassified_count
        })

    df = pd.DataFrame(report)
    return df

print("Evaluating model...")
evaluation_df = evaluate_model(traffic_sign_classifier, val_loader, target_names, device)

print(evaluation_df)


image_dir = '/content/mini_holdout'
csv_path = '/content/mini_holdout_answers.csv'

labels_df = pd.read_csv(csv_path)

transform = transforms.Compose([
    transforms.Resize(image_size),
    transforms.ToTensor()
])

class MiniHoldoutDataset(Dataset):
    def __init__(self, image_dir, labels_df, transform=None):
        self.image_dir = image_dir
        self.labels_df = labels_df
        self.transform = transform

    def __len__(self):
        return len(self.labels_df)

    def __getitem__(self, idx):
        img_name = self.labels_df.iloc[idx]['Filename']
        label = self.labels_df.iloc[idx]['ClassId']
        img_path = os.path.join(self.image_dir, img_name)
        image = Image.open(img_path).convert('RGB')
        if self.transform:
            image = self.transform(image)
        return image, label

mini_holdout_dataset = MiniHoldoutDataset(image_dir, labels_df, transform)
mini_holdout_loader = DataLoader(mini_holdout_dataset, batch_size=64, shuffle=False)

traffic_sign_classifier.to(device)
traffic_sign_classifier.eval()

all_probabilities = []
all_labels = []

with torch.no_grad():
    for images, labels in mini_holdout_loader:
        images = images.to(device)
        outputs = traffic_sign_classifier(images)
        probs = torch.softmax(outputs, dim=1)
        all_probabilities.extend(probs.cpu().numpy())
        all_labels.extend(labels.numpy())

predictions = [np.argmax(p) for p in all_probabilities]

from sklearn.metrics import accuracy_score
print("Accuracy on mini_holdout:", accuracy_score(all_labels, predictions))
