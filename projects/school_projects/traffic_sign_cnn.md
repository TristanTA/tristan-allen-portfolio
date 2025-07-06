# Traffic Sign Classifier (Deep Learning Project)

This project implements a **traffic sign classification system** using deep learning (PyTorch). The model classifies images of traffic signs into multiple categories with data augmentation and performance evaluation.

---

## Project Overview
- **Goal:** Classify traffic signs from images using a Convolutional Neural Network (CNN).
- **Dataset:** Custom dataset sourced from the [BYU-I CSE 450 course](https://github.com/byui-cse/cse450-course).
- **Techniques:**
  - Data Augmentation
  - CNN Architecture
  - Training & Validation Splits
  - Model Evaluation (Confusion Matrix, Classification Metrics)
  - Holdout Set Testing

---

## Technologies Used
- **PyTorch** (Modeling)
- **Pandas, NumPy** (Data Analysis)
- **Matplotlib** (Visualization)
- **TorchVision** (Image Processing)
- **TQDM** (Progress Bars)
- **Sklearn** (Metrics)

---

## Project Structure
- `starter_signs_v2_student.py` — Full training & evaluation script (CNN-based classifier).
- Dataset loading and preprocessing via PyTorch `ImageFolder`.
- Model training with early stopping and learning rate scheduling.
- Final testing on holdout dataset.

---

## Key Features
- Randomized image augmentation (flips, rotations, color jitter).
- Early stopping based on validation performance.
- Evaluation includes confusion matrix, per-class stats, and most frequent misclassifications.
- Model persistence (saving/loading).

---

## Results
- Achieved strong classification accuracy on training, validation, and holdout sets.
- Detailed classification report generated for analysis.

---

## License
Educational use; part of coursework at BYU-Idaho (CSE 450 - Machine Learning).

---

## Contact
For questions or collaborations, reach me at:
- [GitHub](https://github.com/TristanTA)
- [LinkedIn](https://www.linkedin.com/in/tristantravus)
