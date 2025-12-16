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
import unittest
import os
from file_manager import FileManager

TEST_FILE = "text_note.txt"

# --------------------------------------------------
# test file manager
# --------------------------------------------------
class TestFileManager(unittest.TestCase):
    
    def setUp(self):
        self.fm = FileManager()
    
    def test_write_and_read_file(self):
        content = "Hello Notepad"
        self.fm.write_file(TEST_FILE, content)

        read_content = self.fm.read_file(TEST_FILE)
        self.assertEqual(content, read_content)
    
    def test_reset(self):
        self.fm.file_path = "dummy.txt"
        self.fm.reset()
        self.assertIsNone(self.fm.file_path)
    
    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

if __name__ == "__main__":
    unittest.main()