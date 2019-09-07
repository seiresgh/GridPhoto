# slideshow

This is a simple web app that displays pictures in a grid
to manage your collection of photos.
It shows the number and resolution of your photos.
Then you can delete the photo with a simple click.
It's handy when you have a big collection.

It requires python, aiohttp, and mako.
I only tested it with visual studio code on windows.

Note that the web server and the folder needs to be on the same machine
so that it has access.

How to use:
Download all the files.
Run the python script with visual studio code ( or other python ide).
Make sure you have all the required components.
When it's up and running, point your browser to http://localhost:8080
In the text input at the top, enter the directory of the photos you
want to review and press go ( or enter ).
Any subfolder will be listed first in the bottom.
Clicking any photo will delete it.
The 'go up' button will try to go up a level of the current directory.
After it returns the parent folder, press go to actually load the photos.