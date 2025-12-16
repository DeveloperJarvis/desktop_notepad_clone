# 📘 Low-Level Design (LLD): Desktop Notepad Clone (Tkinter)

---

## 1. System Overview

The **Desktop Notepad Clone** is a lightweight GUI-based text editor built using **Python Tkinter**.
It provides essential text-editing features similar to a basic notepad application.

### Core Features

- Create and edit text
- Open existing text files
- Save text to files
- Change font size
- Search text within the document

---

## 2. Key Objectives

- Simple, responsive GUI
- Minimal dependencies (Tkinter only)
- Clear separation between UI and logic
- Keyboard and menu-driven interaction
- Beginner-friendly but extensible design

---

## 3. High-Level Architecture

```
User Actions (Mouse / Keyboard)
        ↓
GUI Components (Menu, Text Area)
        ↓
Event Handlers
        ↓
Editor Controller
        ↓
File / Text Operations
```

---

## 4. Core Components

---

## 4.1 NotepadApp (Main Application)

### Responsibility

Acts as the root controller and initializes all GUI components.

### Attributes

- root_window
- text_area
- menu_bar
- status_bar
- current_file_path
- font_size

### Methods

- initialize_ui()
- run()
- update_title()
- bind_shortcuts()

---

## 4.2 TextEditorArea

### Responsibility

Handles text input, editing, scrolling, and formatting.

### Attributes

- text_widget
- scrollbar
- font_family
- font_size

### Methods

- get_text()
- set_text(content)
- clear_text()
- apply_font(size)
- highlight_text(start, end)

---

## 4.3 MenuBar

### Responsibility

Provides user-accessible commands via menus.

### Menus & Items

#### File Menu

- New
- Open
- Save
- Save As
- Exit

#### Edit Menu

- Undo
- Redo
- Cut
- Copy
- Paste
- Search

#### View Menu

- Increase Font Size
- Decrease Font Size
- Reset Font Size

### Methods

- create_file_menu()
- create_edit_menu()
- create_view_menu()

---

## 4.4 FileManager

### Responsibility

Handles file system operations.

### Attributes

- current_file_path

### Methods

- new_file()
- open_file()
- save_file()
- save_file_as()
- read_file(path)
- write_file(path, content)

### Behavior

- Prompts user before overwriting files
- Handles unsaved changes warnings

---

## 4.5 SearchManager

### Responsibility

Provides text search functionality.

### Attributes

- search_term
- match_indices

### Methods

- search(text, keyword)
- highlight_matches()
- clear_highlights()

### Search Behavior

- Case-insensitive
- Highlights all matches
- Focuses on first match

---

## 4.6 FontManager

### Responsibility

Controls text appearance.

### Attributes

- current_font_size
- min_font_size
- max_font_size

### Methods

- increase_font()
- decrease_font()
- reset_font()
- apply_font()

---

## 4.7 StatusBar (Optional)

### Responsibility

Displays contextual information.

### Attributes

- cursor_position
- word_count
- file_status

### Methods

- update_cursor_position()
- update_word_count()
- update_file_status()

---

## 5. Event Handling

| Event         | Trigger       | Handler                   |
| ------------- | ------------- | ------------------------- |
| New File      | Menu / Ctrl+N | FileManager.new_file      |
| Open File     | Menu / Ctrl+O | FileManager.open_file     |
| Save File     | Menu / Ctrl+S | FileManager.save_file     |
| Search        | Menu / Ctrl+F | SearchManager.search      |
| Font Increase | Ctrl + +      | FontManager.increase_font |
| Font Decrease | Ctrl + -      | FontManager.decrease_font |
| Text Change   | Typing        | StatusBar.update          |

---

## 6. Data Flow

```
User Input
   ↓
Text Widget
   ↓
Event Trigger
   ↓
Controller / Manager
   ↓
Text or File Update
```

---

## 7. Error Handling & Edge Cases

- File open cancellation
- Invalid file paths
- Empty search input
- Font size overflow/underflow
- Unsaved content on exit
- Read/write permission errors

---

## 8. Performance Considerations

- Tkinter Text widget handles large text efficiently
- Minimal redraw operations
- Highlighting only visible text range
- No background threads needed

---

## 9. Extensibility

Possible enhancements:

- Dark mode
- Line numbers
- Syntax highlighting
- Autosave
- Tabs / multiple documents
- Clipboard history

---

## 10. Example User Flow

```
User opens app
→ Types text
→ Increases font size
→ Searches for keyword
→ Saves file
→ Exits
```

---

## 11. Skills Demonstrated

✔ GUI design (Tkinter)
✔ Event-driven programming
✔ File handling
✔ UI/UX fundamentals
✔ Clean architecture

---

## 12. Interview One-Line Summary

> A lightweight Tkinter-based desktop notepad clone featuring file operations, search, and font control with clean event-driven design.
