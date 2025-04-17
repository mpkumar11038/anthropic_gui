# Claude GUI Interaction Project Setup

This guide walks you through setting up the Claude GUI Interaction project, which includes a Flask backend and a Python script for GUI interactions (`mouse_demo.py`).

## System Requirements

Before starting, ensure your system has the following installed:
- **Python 3** (version 3.10 or higher recommended)
- **Git** (for cloning the repository)
- **virtualenv** (for managing Python virtual environments)

To install `virtualenv` on a Linux system, run:
```bash
sudo apt install python3.10-venv
```

## Setting Up the Project

### Step 1: Clone the Repository
1. Open a terminal.
2. Clone the project repository:
   ```bash
   git clone https://github.com/username/repo.git
   ```
3. Navigate to the project directory:
   ```bash
   cd claude-gui-interaction
   ```

### Step 2: Configure the Python Environment
1. Create a virtual environment to isolate dependencies:
   ```bash
   python -m venv env
   ```
2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Launch the Flask Backend
1. Start the Flask server by running:
   ```bash
   python3 app.py
   ```
2. The backend should now be running, typically accessible at `http://localhost:5000/`.

### Step 4: Run the GUI Interaction Script
1. Open a new terminal window.
2. Navigate to the project directory:
   ```bash
   cd claude-gui-interaction
   ```
3. Activate the virtual environment (same as Step 2):
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
4. Execute the GUI interaction script:
   ```bash
   python3 mouse_demo.py
   ```

## Notes
- Ensure the Flask server is running before executing `mouse_demo.py`, as the script may interact with the backend.
- If you encounter issues, verify that all dependencies are installed correctly and that your Python version is compatible.

## About Anthropic:
#### Anthropic is not supported to work on local system

As per my research Anthropic is not working on local system because as I checked generally it runs on models in isolated environments or virtual machine (VM)-based sandboxes to ensure security, isolation, and stability.

But as I found out we can run it using Docker with ngrok. It is a substitute only because it will also not work in the case of local.
