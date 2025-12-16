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

# --------------------------------------------------
# 4. file manager
# --------------------------------------------------
"""
Responsibility:
Handles file system operations
Behavior:
- Prompts user before overwritting files
- Handles unsaved changes warnings
"""
class FileManager:
    def __init__(self):
        self.file_path = None
    
    def reset(self):
        self.file_path = None

    def read_file(self, path):
        with open(path, "r", encoding="utf-8") as f:
            self.file_path = path
            return f.read()

    def write_file(self, path, content):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        self.file_path = path
