"""Meet The Snooze Cannon An: one-line entry for make.fun.

The program writes exactly one line - the drafted winning line for the 'One Sentence Absurd Invention Pitch' bounty - to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader). The line is a fixed constant with no trailing newline, so both of the grader's runs
write byte-identical output: 115 UTF-8 characters, inside the 1-200 gate.
"""
import os

LINE = 'Meet the Snooze Cannon, an alarm clock that launches you into your clothes and directly into your responsibilities.'

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
