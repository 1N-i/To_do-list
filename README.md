# 📝 To-Do List

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)

A simple and efficient command-line interface (CLI) application to manage your daily tasks, allowing you to create, track, and organize your to-do items.

## 📋 Summary
- [Technologies](#-technologies)
- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)

---

## 🛠 Technologies
- **Python 3.x**: Core logic, dictionary-based data storage, and CLI flow.

## ✨ Features
- **Task Management:** Add new tasks and store them in a dynamic list.
- **Status Tracking:** Mark tasks as completed with a visual checkmark (`✓`).
- **Data Integrity:** Includes validation to prevent actions on empty lists and handles invalid inputs using `try-except` blocks.
- **Task Deletion:** Remove specific tasks from the list by their index.
- **Interactive Menu:** A user-friendly numeric menu to navigate between all functions.

## 📂 Project Architecture
The project is contained within a single optimized script:
* `to_do-list.py`: Contains the main execution loop and all functional modules (`add`, `view`, `mark as done`, and `delete`).

## 📚 What I Learned
* **Dictionary Manipulation:** Using Python dictionaries to map task descriptions to their completion status.
* **Error Handling:** Implementing `try-except` blocks to manage `ValueError` when dealing with user numeric inputs.
* **List Indexing:** Converting dictionary keys to lists to allow users to select items by number rather than typing full strings.

## 🔮 Future Improvements
* [ ] **Data Persistence:** Save tasks to a `.txt` or `.json` file so they aren't lost when closing the app.
* [ ] **Due Dates:** Add the ability to set deadlines for each task.
* [ ] **Priority Levels:** Categorize tasks as High, Medium, or Low priority.
