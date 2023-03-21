# This converts Markside to HTML.
import os
txt = input("> ")
print(os.sys(f"perl Markdown.pl --html4tags {txt}"))
