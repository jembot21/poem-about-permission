"""Write the competition poem, exactly as composed."""

from pathlib import Path


POEM = """I let my agent send.
First I weighed each word, then signed.
It learned my slant,
the mercy I kept for my mother.
Soon its voice came before mine.
A blank page waited by the pen.
It asked: whose hand?
I took the pen back.
My first word trembled.
At last, my name opened the door."""


def write_entry(path="/output/entry.txt"):
    """Create the parent directory and write POEM as UTF-8."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    write_entry()
