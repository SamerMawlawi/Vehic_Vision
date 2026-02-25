# Welcom to data_prep

## 🌳 Git Workflow & Branching Strategy

To maintain a clean and conflict-free codebase, we follow a **Feature Branching** model. Please strictly adhere to the following workflow:

### 1. Base Branch
The `data_prep` branch serves as our integration hub for this phase. **Do not commit directly to this branch.**

### 2. Working on a Task
Before starting any task, create a sub-branch from `data_prep`:

```bash
# 1. Switch to the data_prep branch
git checkout data_prep

# 2. Get the latest updates from the team
git pull origin data_prep

# 3. Create your own feature branch
# Replace 'task-name' with your specific task (e.g., feature/mapping)
git checkout -b feature/task-name
```

### Submission Process (Pull Requests)

Once you have completed your task:

    Push your branch to GitHub: git push -u origin feature/task-name.

    Open a Pull Request (PR) on GitHub from your feature branch into data_prep.

    Notify the Leader for code review.

    After approval, the branch will be merged into data_prep.

 **Important Rules**

    Isolate your work: Only work on files related to your assigned Issue.

    Sync frequently: Run git pull origin data_prep regularly to stay updated with other members' contributions.

    Notebooks vs. Scripts: Use the notebooks/ folder for experiments, but move all final, reusable logic to the src/ folder.

---


📂 **Project Structure**
```text
Vehi-Vision
├── data/               # Local datasets (Ignored by Git)
├── venv/               # Python Environment (Ignored by Git)
├── weights/            # Saved model weights (.pt or .onnx)
├── notebooks/          # Research, EDA, and prototyping
├── src/                # Source code (Detection, Segmentation, XAI)
├── .gitignore          # Files to exclude from Git
└── README.md
```
