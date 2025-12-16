# 📝 Desktop Notepad Clone (Tkinter)

A **minimal desktop text editor** built using **Python Tkinter**, providing essential Notepad-like functionality such as file operations, text search with highlighting, and font size control.
Also supporting keyboard shortcuts and dark mode using clean event-driven design.

This project demonstrates **GUI development, event handling, and file I/O** in Python.

---

## 📌 Features

- 🆕 Create new text files
- 📂 Open existing `.txt` files
- 💾 Save / Save As functionality
- 🔍 Search text within document
- 🔠 Increase / decrease font size
- ⌨ Keyboard shortcuts (Ctrl+S, Ctrl+O, Ctrl+F, etc.)
- 🖥 Lightweight, responsive GUI

---

## 🧠 Skills Demonstrated

- Tkinter GUI programming
- Event-driven architecture
- File handling and dialogs
- Text widget manipulation
- Clean separation of concerns
- Desktop application design

---

## 🏗 Project Structure

```
desktop_notepad_clone/
│
├── notepad.py              # Main application entry point
├── README.md               # Project documentation
└── LICENSE                 # GPL-3.0 License
```

---

## 🚀 Getting Started

### 1⃣ Prerequisites

- Python **3.8+**
- Tkinter (included with standard Python installation)

Verify Tkinter:

```bash
python -m tkinter
```

---

### 2⃣ Run the Application

```bash
python notepad.py
```

### 3 Run tests:

```bash
python -m unittest test_file_manager.py
```

## 3 BUID App

### 3.1 Build App

```bash
pyinstaller --onefile --windowed notepad.py
```

### 3.2 Output

```md
dist/
└── notepad.exe
```

---

## 🧩 Functional Overview

### 🗂 File Operations

- **New**: Clears editor
- **Open**: Loads `.txt` files
- **Save**: Saves current content
- **Save As**: Save with new name

### 🔍 Search

- Case-insensitive search
- Highlights matching text
- Supports repeated searches

### 🔠 Font Control

- Increase font size
- Decrease font size
- Reset to default size

---

## 🧪 Error Handling

- Handles empty files
- Prevents accidental overwrite
- Prompts before exiting with unsaved changes
- Graceful file read/write failures

---

## 📈 Performance

- Efficient for small to medium text files
- Tkinter `Text` widget optimized for live editing
- No background threads required

---

## 🔮 Future Enhancements

- Dark mode - done
- Line numbers
- Syntax highlighting
- Autosave - done
- Tabbed documents
- Regex-based search - done

## 🏗 Project Structure for Multi-File MVC Refactor

```
desktop_notepad_clone/
│
├── app.py                 # Entry point
├── controller/
│   └── notepad_controller.py
│
├── view/
│   ├── notepad_view.py
│   └── status_bar.py
│
├── model/
│   ├── file_manager.py
│   └── autosave_manager.py
│
├── utils/
│   └── search_utils.py
│
└── tests/
    └── test_file_manager.py
```

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0-or-later)**.

You are free to:

- Use
- Modify
- Distribute

Under the terms of the GPL license.

---

## 👤 Author

**Developer Jarvis** _(Pen Name)_
🔗 GitHub: [https://github.com/DeveloperJarvis](https://github.com/DeveloperJarvis)

---

## 🧑💻 Interview One-Liner

> A lightweight Tkinter-based desktop notepad clone showcasing GUI design, event handling, and file operations in Python.

## Creating tag

```bash
# 1. Check existing tags
git tag
# 2. Create a valid tag
git tag -a v1.0.0 -m "Release version 1.0.0"
# or lightweight tag
git tag v1.0.0
# push tag to remote
git push origin v1.0.0
```
