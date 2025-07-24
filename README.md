# AI Profiles Dashboard

An interactive Streamlit web application showcasing team members' AI tools usage profiles.  
Profiles include names, emails, images, and detailed AI tools and prompts used.

---
## Project Structure
```commandline
ai-team-profiles/
├── README.md
├── app.py
├── pyproject.toml
├── uv.lock
├── .gitignore
├── .venv/
├── .python-version
├── data/
│ └── profiles.xlsx # Excel data source
├── images/
│ ├── anhnt446.jpg # Profile images
│ └── minhln13.jpg
├── styles/
│ └── style.css # Custom CSS styles
└── utils/
├── init.py
├── data_loader.py # Data loading utilities
├── helpers.py # Helper functions like text highlighting
└── render.py # Profile card rendering logic
```


---

## Prerequisites

- Python 3.8 or above
- [uv](https://pypi.org/project/uv/) Python package manager installed globally  
  (If not installed, run: `pip install uv`)

---

## Setup Instructions

1. **Clone the repository**

   ```bash
   - git clone https://github.com/ajeet214/ai-team-profiles.git
   - cd ai-team-profiles

2. **Install dependencies and setup environment using `uv`**

- Initialize environment (if not already done):

  ```uv init```
- Install dependencies (defined in pyproject.toml):
  ```uv sync```

3. **Activate the virtual environment**

- Using `uv`:

  ```uv shell```
- Or activate .venv manually::
  ```bash
  source .venv/bin/activate      # Linux/macOS
  .venv\Scripts\activate         # Windows
  ```
---
## Running the App
To start the Streamlit web app, run:
```bash
uv run streamlit run app.py
```
or if your virtual environment is active:
```bash
streamlit run app.py
```
Then open your browser and go to:
```commandline
http://localhost:8501
```
---
## Features
- Search profiles by name, email, AI tool, or role.
- Highlight matched search terms for easier scanning.
- Responsive profile cards with hover effects.
- Externalized CSS for easy theming and style maintenance.
- Modular Python code with clear separation of concerns.
---
## Development Notes
- Profile data is stored in `data/profiles.xlsx`.
- Profile images are stored in the `images/` folder.
- Styles are defined in `styles/style.css`.
- Core logic split across modules in the `utils/` package.
---
## Managing Dependencies
- Use uv commands to manage dependencies:
- `uv add <package>` to add new packages.
- `uv remove <package>` to remove packages.
- `uv sync` to install/update dependencies.
- Use `uv shell` to activate the virtual environment.