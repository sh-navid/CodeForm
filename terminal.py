# base is imported from https://github.com/sh-navid/OpenGaurd/blob/master/terminal.py

import sys
from src.file import File
from src.cleaner import KotlinCleaner
from src.format import KotlinFormatter

# ----------------------------------------------------------------------------

root = sys.path[0]

files = ["Test1", "Test2", "Test3","Test4"]

for f in files:
    test_in = root + f"/sample/{f}.kt"
    test_out = root + f"/sample/{f}.formed.kt"

    # ----------------------------------------------------------------------------

    content = File.read(test_in)

    content = KotlinCleaner.remove_emptylines(content)
    content = KotlinCleaner.remove_multispace(content)
    content = KotlinCleaner.remove_extra_singlespaces(content)
    content = KotlinFormatter.fix_indentation(content)

    File.write(test_out, content)