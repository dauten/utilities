# utilities
# trans.py
Python script that:

takes a filename (or relative path to file)

reads the contents of that plaintext into a string


removes from that string any instance of single linebreaks, while leaving double linebreaks intact

this is intended to remove any linebreaks that occur in the middle of lines while leaving linebreaks between paragraphs intact.

useful for cleaning data that has linebreaks due to copy/paste ie when you copied from a .pdf


# testing.py
Takes JSON that has an 'images' property and updates them so it can be used more easily.

It uses wget to download any images that are URL references then deletes any of those images that are 86 bytes (one pixel by one pixel).  Then it goes through and updates the JSON by replacing the URL with an HTML img tag with src pointing to the local file that was downloaded in the previous step.  If there is any object that does not have a corresponding image (an image that was deleted because it was one pixel, or a Null property) then an image will be generated using the 'title' field of the JSON and ImageMagick.  The image will be composed over a default vector image of a book by default.
