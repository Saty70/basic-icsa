# Intelligent Customer Service Assistant (ICSA)

This project is a basic Intelligent Customer Service Assistant (ICSA) built with Flask and spaCy. It can respond to simple greetings, farewells, and thank-you messages.

## Features

- Responds to greetings, farewells, and thank-you messages.
- Uses Flask for the backend and spaCy for natural language processing.
- Simple frontend with HTML and CSS.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- virtualenv (recommended)

## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/basic-icsa.git
```
```bash
cd basic-icsa
```
<b>If you can have venv folder then delete it</b>

### Step 2: Set Up a Virtual Environment

Create and activate a virtual environment. This step is optional but recommended to avoid conflicts with other packages.

```bash
pip install virtualenv
```
For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

For MacOS / Linux(debian):
```bash
python3 -m venv venv
source venv/bin/activate
```
### Step 3: Install Dependencies

Install required libraries
```bash
pip install -r requirements.txt
```

Download the spaCy language model:
```bash
python -m spacy download en_core_web_sm
```

### Step 5: Run the Flask Application
Start the Flask application by running the following command:

```bash
python app.py
```
The application will start on http://127.0.0.1:5000/.

<br>

## File Structure
<br>

```bash
basic-icsa/
│
├── venv/               # Virtual environment
├── app.py              # Flask backend application
├── Readme.md           # Readme file for instructions
├── requirements.txt    # Dependencies file
└── static/
    ├── index.html      # HTML file for the frontend
    └── style.css       # CSS file for styling
```