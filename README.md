<a id="readme-top"></a>

<h1 style="text-align: center;">CLI Task Tracker</h1>
<div>
  <p style="text-align: center;">
    Task tracker is a project used to track and manage your tasks. It provides a simple command-line interface (CLI) to create, list, complete, and delete tasks. The tasks are stored locally in a JSON file.
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

**Disclaimer:** This project is for learning purposes only. It is a standard, easy project built to be submitted to [roadmap.sh](https://roadmap.sh/).

**roadmap.sh project:** [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

CLI Task Tracker is a lightweight, pure-Python command-line application to manage your daily tasks. Data is stored locally in a simple JSON file, making it completely portable and easy to use.

### Features
* Create, update, and delete tasks.
* Mark tasks as `in-progress` or `done`.
* List all tasks or filter them by status (`todo`, `in-progress`, `done`).

<p style="text-align: right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python]][Python-url]
* Standard Python libraries: `argparse`, `json`, `datetime`, `os`

<p style="text-align: right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* [Python 3.x](https://www.python.org/downloads/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Karimskee/task-tracker-cli.git
   ```
2. Navigate to the project directory
   ```sh
   cd task-tracker-cli
   ```

<p style="text-align: right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Run the CLI using Python. 

**Note:** Task descriptions do not allow quotes, so you cannot type `'` or `"` in your tasks.

### Commands

* **Add a task:**
  ```sh
  python app.py add Buy groceries
  ```
* **Update a task:**
  ```sh
  python app.py update 1 Buy groceries and milk
  ```
* **Delete a task:**
  ```sh
  python app.py delete 1
  ```
* **Mark a task in-progress or done:**
  ```sh
  python app.py mark in-progress 1
  python app.py mark done 1
  ```
* **List tasks:**
  ```sh
  python app.py list              # List all tasks
  python app.py list todo         # List only tasks that are to do
  python app.py list in-progress  # List only tasks in progress
  python app.py list done         # List only tasks that are done
  ```

<p style="text-align: right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=fff
[Python-url]: https://www.python.org/