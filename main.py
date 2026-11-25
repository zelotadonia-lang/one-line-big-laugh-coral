"""One Line, Big Laugh entry: a single funny line written to /output/entry.txt."""

import os

ENTRY = "My dog buried the remote in the garden, so movie night now starts with a shovel."


def main():
    # Bounty gate: entry must be 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, f"ENTRY is {len(ENTRY)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: the bytes on disk must be exactly ENTRY,
    # with no trailing newline added by the write.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
