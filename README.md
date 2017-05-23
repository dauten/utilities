# utilities
# trans.py
Python script that:
takes a filename (or relative path to file)
reads the contents of that plaintext into a string
removes from that string any instance of single linebreaks, while leaving double linebreaks intact
this is intended to remove any linebreaks that occur in the middle of lines while leaving linebreaks between paragraphs intact.
useful for cleaning data that has linebreaks due to copy/paste ie when you copied from a .pdf
