# BBC News Headlines Scraper

## Project Overview

This project is a simple Python web scraping application that fetches the latest news headlines from the BBC News website and displays the top 5 headlines in the terminal.

It uses the `requests` library to retrieve webpage content and `BeautifulSoup` to extract headlines from HTML.

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
headlines/
│
├── headlines.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.10 or later
- Visual Studio Code
- Internet connection

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd headlines
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows CMD:**

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## How to Run

Execute the following command in the terminal:

```bash
python headlines.py
```

## Expected Output

```text
1. First BBC News headline
2. Second BBC News headline
3. Third BBC News headline
4. Fourth BBC News headline
5. Fifth BBC News headline
```

*Note: Actual headlines will vary depending on the latest BBC News updates.*

## Key Features

- Fetches news content using HTTP requests.
- Checks HTTP response status before parsing.
- Uses a browser-like User-Agent header.
- Extracts headlines using BeautifulSoup CSS selectors.
- Removes empty and duplicate headlines.
- Displays a maximum of five unique headlines.
- Handles network errors and cases where fewer than five headlines are available.

## HTML Element Used

The BBC headline selector identified through Chrome Developer Tools:

```css
h2[data-testid="card-headline"]
```

## Learning Outcomes

- Understanding Python web scraping.
- Working with HTTP requests.
- Parsing HTML using BeautifulSoup.
- Inspecting HTML elements using Chrome Developer Tools.
- Using CSS selectors.
- Handling exceptions in Python.
- Managing Python dependencies and GitHub repositories.

## Author

Python Web Scraping Assignment

## License

This project is intended for educational and learning purposes.