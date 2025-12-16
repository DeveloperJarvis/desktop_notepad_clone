# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the desktop_notepad_clone Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# desktop_notepad_clone - Minimal GUI editor with save, load, font-size and search
#                           Skills: GUI, event handling
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# desktop_notepad_clone MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font
from file_manager import FileManager

# --------------------------------------------------
# 1. notepad app (main application)
# --------------------------------------------------
"""
Responsibility:
Acts as the root and initializes all GUI components
"""
class NotepadApp:
    def __init__(self, root):
        # self.root_window 
        self.root = root
        self.update_title("Desktop Notepad Clone")

        # self.menu_bar
        # self.status_bar
        # self.current_file_path
        self.file_manager = FileManager()
        self.font_size = 12
        self.dark_mode = False
        self.text_area = None

        # self.autosave = AutoSaveManager(
        #     self.root, self.file_manager, self.text_area
        # )
        # self.autosave.start()

        self._setup_ui()
        self._bind_shortcuts()

    # --------------------------------------------------
    def _setup_ui(self):
        self.text_font = font.Font(
            family="Consolas", size=self.font_size
        )

        self.text_area = tk.Text(
            self.root,
            wrap=tk.WORD,
            font=self.text_font,
            undo=True
        )
        self.text_area.pack(
            fill=tk.BOTH,
            expand=True
        )

        self._create_menu()
        self._apply_theme()

    # def initialize_ui(self):
    #     pass

    # def run(self):
    #     pass
    # --------------------------------------------------
    def update_title(self, path=None):
        if path:
            self.root.title(f"{path} - Notepad")
        else:
            self.root.title("Untitled - Notepad")

    # def bind_shortcuts(self):
    #     pass
    # --------------------------------------------------
    def _bind_shortcuts(self):
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-f>", lambda e: self.search_text())
        self.root.bind(
            "<Control-Key-plus>", lambda e: self.increase_font()
        )
        self.root.bind(
            "<Control-Key-minus>", lambda e: self.decrease_font()
        )
    
    # --------------------------------------------------
    def _create_menu(self):
        menu_bar = tk.Menu(self.root)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(
            label="Save As", command=self.save_file_as
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit Menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(
            label="Undo", command=self.text_area.edit_undo
        )
        edit_menu.add_command(
            label="Redo", command=self.text_area.edit_redo
        )
        edit_menu.add_separator()
        edit_menu.add_command(label="Search", command=self.search_text)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # View Menu
        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(
            label="Increase Font Size", command=self.increase_font
        )
        view_menu.add_command(
            label="Decrease Font Size", command=self.decrease_font
        )
        view_menu.add_separator()
        view_menu.add_command(
            label="Toggle Dark Mode", command=self.toggle_dark_mode
        )
        menu_bar.add_cascade(label="View", menu=view_menu)

        self.root.config(menu=menu_bar)

    # --------------------------------------------------
    # File Operations
    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.file_manager.reset()
        self.update_title()
    
    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")]
        )
        if path:
            content = self.file_manager.read_file(path)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, content)
            self.update_title(path)
    
    def save_file(self):
        content = self.text_area.get("1.0", tk.END)
        if not self.file_manager.file_path:
            self.save_file_as()
        else:
            self.file_manager.write_file(
                self.file_manager.file_path, content
            )
    
    def save_file_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            content = self.text_area.get("1.0", tk.END)
            self.file_manager.write_file(path, content)
            self.update_title(path)
    
    def exit_app(self):
        if messagebox.askokcancel("Quit", "Exit without saving?"):
            self.root.destroy()
    
    # --------------------------------------------------
    # Search
    def search_text(self, search_highlight_color="yellow"):
        keyword = simpledialog.askstring("Search", "Enter text:")
        if not keyword:
            return
        
        self.text_area.tag_remove("highlight", "1.0", tk.END)
        start = "1.0"

        while True:
            pos = self.text_area.search(
                keyword, start, tk.END, nocase=True
            )
            if not pos:
                break
            end = f"{pos}+{len(keyword)}c"
            self.text_area.tag_add("highlight", pos, end)
            start = end
        
        if self.dark_mode:
            search_highlight_color="light blue"

        self.text_area.tag_config(
            "highlight", background=search_highlight_color
        )

    # --------------------------------------------------
    # Font
    def increase_font(self):
        self.font_size += 1
        self.text_font.configure(size=self.font_size)
    
    def decrease_font(self):
        if self.font_size > 8:
            self.font_size -= 1
            self.text_font.configure(size=self.font_size)
    
    # --------------------------------------------------
    # Dark Mode
    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self._apply_theme()
    
    def _apply_theme(self):
        if self.dark_mode:
            self.text_area.config(
                bg="#1e1e1e", 
                fg="light blue",
                insertbackground="light blue"
            )
        else:
            self.text_area.config(
                bg="white", fg="black", insertbackground="black"
            )

# # --------------------------------------------------
# # 2. text editor area
# # --------------------------------------------------
# """
# Responsibility:
# Handles text input, editing, scrolling and formatting
# """
# class TextEditorArea:
#     def __init__(self):
#         self.text_widget
#         self.scrollbar
#         self.font_family
#         self.font_size

#     def get_text(self):
#         pass

#     def set_text(self, content):
#         pass

#     def clear_text(self):
#         pass

#     def apply_font(self, size):
#         pass

#     def highlight_text(self, start, end):
#         pass


# # --------------------------------------------------
# # 3. menu bar
# # --------------------------------------------------
# """
# Responsibility:
# Provide user-accessible commands via menus
# """
# class MenuBar:
#     def create_file_menu(self):
#         pass

#     def create_edit_menu(self):
#         pass

#     def create_view_menu(self):
#         pass


# # --------------------------------------------------
# # 4. file manager
# # --------------------------------------------------
# """
# Responsibility:
# Handles file system operations
# Behavior:
# - Prompts user before overwritting files
# - Handles unsaved changes warnings
# """
# class _FileManager:
#     def __init__(self):
#         self.current_file_path = None
    
#     def new_file(self):
#         pass

#     def open_file(self):
#         pass
    
#     def save_file(self):
#         pass

#     def save_file_as(self):
#         pass

#     def read_file(self, path):
#         pass

#     def write_file(self, path, content):
#         pass


# # --------------------------------------------------
# # 5. search manager
# # --------------------------------------------------
# """
# Responsibility:
# Provides text search functionality
# Search Behavior:
# - Case-insensitive
# - Highlights all matches
# - Focuses on first match
# """
# class SearchManager:
#     def __init__(self):
#         self.search_item
#         self.match_indices

#     def search(self, text, keyword):
#         pass

#     def highlight_matches(self):
#         pass

#     def clear_highlights(self):
#         pass

# # --------------------------------------------------
# # 6. font manager
# # --------------------------------------------------
# """
# Responsibility:
# Controls text appearance
# """
# class FontManager:
#     def __init__(self):
#         self.current_font_size
#         self.min_font_size
#         self.max_font_size
    
#     def increase_font(self):
#         pass

#     def decrease_font(self):
#         pass

#     def reset_font(self):
#         pass

#     def apply_font(self):
#         pass

# --------------------------------------------------
# 7. status bar
# --------------------------------------------------
"""
Responsibility:
Display contextual information.
"""
class StatusBar(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        # self.cursor_position
        # self.word_count
        # self.file_status
        self.label = tk.Label(self, anchor="w")
        self.label.pack(fill=tk.X)
    
    # def update_cursor_position(self):
    #     pass

    # def update_word_count(self):
    #     pass

    # def update_file_status(self):
    #     pass

    def update(self, cursor, words, status):
        self.label.config(
            text=f"Ln {cursor[0]}, Col {cursor[1]}"
            f"| Words: {words} | {status}"
        )

# --------------------------------------------------
# 8. autosave manager
# --------------------------------------------------
class AutoSaveManager:
    def __init__(self, root, file_manager, text_widget, interval=10000):
        self.root = root
        self.file_manager = file_manager
        self.text_widget = text_widget
        self.interval = interval
    
    def start(self):
        self._autosave()
    
    def _autosave(self):
        if self.file_manager.file_path and self.text_widget.edit_modified():
            content = self.text_widget.get("1.0", tk.END)
            self.file_manager.write_file(
                self.file_manager.file_path, content
            )
            self.text_widget.edit_modified(False)
        self.root.after(self.interval, self._autosave)

# --------------------------------------------------
# main module
# --------------------------------------------------
def main():
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()