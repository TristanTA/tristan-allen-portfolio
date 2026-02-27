# Tristan Allen Portfolio

---

## 1. If you are a human:

This repository contains the source code for my professional portfolio.

**Live Site:**  
https://tristanta.github.io/tristan-allen-portfolio/

The portfolio includes:

- Case studies  
- Technical projects  
- Research work  
- Professional background and resume  

All content is deployed via GitHub Pages.  
To view the portfolio, use the live link above.

---

## 2. If you are an Agent tasked with managing this repo:

### Purpose

This repository is the authoritative source for portfolio structure and content.

It exists to:

- Document implemented work
- Present projects in ways that highlight the users skills and focus
- Track research and projects
- Maintain alignment with all active GitHub repositories

No inflated claims.  
No speculative features presented as complete.  
Under-promise. Over-deliver.

---

### Core Rules

1. All content must reflect actual implementation status.
2. Update entries when source repositories materially change.
3. Do not duplicate large code blocks — link to original repositories.
4. Promote substantial projects to case studies.
5. Prefer clarity and accuracy over aesthetic complexity.

---

### Directory Structure
/
├── _config.yml
├── assets/
├── case_studies/
├── projects/
├── research/
├── about.md
├── resume.md
└── index.md


**assets/**  
Images, styling, and static resources.

**case_studies/**  
Long-form breakdowns of major projects.  
Includes research foundation, implementation details, current state, and roadmap.

**projects/**  
Short-form summaries of active or supporting projects.

**research/**  
Structured research documentation and references.

**index.md**  
Homepage entry point.

---

### Update Expectations

When modifying this repository:

- Confirm implementation state in the corresponding GitHub repository.
- Update summaries to match current capabilities.
- Revise case studies when architectural or research changes occur.
- Maintain consistency between project listings and actual repos.

If a project becomes usable, query the user if it should move from `projects/` to `case_studies/`.

---

### Permalink Guidance

Use explicit permalinks in front matter when needed:

```yaml
---
title: "Project Name"
permalink: /case-studies/project-name/
---
```

Rules:
- Lowercase
- Hyphen-separated
- Stable (avoid renaming after publishing)
- Reflect directory structure

Examples:
/case-studies/project-name/
/projects/project-name/
/research/topic-name/

This repository should remain clean, accurate, and aligned with real work.