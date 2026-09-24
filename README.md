Workflow
Install DVC
     ↓
Initialize Git
     ↓
Initialize DVC
     ↓
Add Dataset to DVC
     ↓
Commit DVC Metadata to Git
     ↓
Modify Dataset
     ↓
Checkout Git Version
     ↓
DVC Checkout / Pull Dataset
     ↓
Train ML Model
     ↓
Add Model to DVC
     ↓
Commit Changes to Git
Git vs DVC



| Command                                          | Purpose                    | What it creates/affects                   |
| ------------------------------------------------ | -------------------------- | ----------------------------------------- |
| pip install dvc`                                | Install DVC                | Installs DVC on your system               |
| git init`                                       | Initialize Git             | Creates a Git repository                  |
| python -m dvc init`                             | Initialize DVC             | Creates DVC configuration inside Git repo |
| python -m dvc add Salary_Data.csv`              | Track dataset with DVC     | Creates `Salary_Data.csv.dvc`             |
| git add Salary_Data.csv.dvc .gitignore`         | Stage DVC files in Git     | Prepares files for commit                 |
| git commit -m "track dataset with dvc"`         | Save first version         | Git stores the DVC metadata/version       |
| git status`                                     | Check repository status    | Shows modified/untracked/staged files     |
| cd "...\DVC"`                                   | Move to project folder     | Changes terminal's current directory      |
| python alterdata.py`                            | Modify the dataset         | Changes `Salary_Data.csv`                 |
| git checkout ...`                               | Switch/restore Git version | Changes files based on Git version/branch |
| python -m dvc pull --force`                     | Download/restore DVC data  | Retrieves dataset from DVC remote         |
| python training.py`                             | Train ML model             | Generates `model.pkl`                     |
| python -m dvc add model.pkl`                    | Track model with DVC       | Creates `model.pkl.dvc`                   |
| git add .`                                      | Stage all changes          | Adds modified/new files to Git            |
| git commit -m "second commit with model track"` | Save second version        | Git stores the new DVC metadata           |
