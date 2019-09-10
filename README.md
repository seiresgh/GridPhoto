# GridPhoto

This is a simple web app that displays pictures in a grid
to manage your collection of photos.
It shows the number and resolution of your photos.
Then you can delete the photo with a simple click.
It's handy when you have a big collection.

It requires python, aiohttp, and mako.
I only tested it with visual studio code on windows.

Note that the web server and the folder needs to be on the same machine
so that it has access. Although the folder can be a mapped network drive.

# How to use:
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

# Run with docker
a docker file and its requirements.txt is also included.
Build it like this:
docker build --tag=gridphoto .
After you build the image, remember to expose 8080 to a port you desired
Like this:
docker run -p 8080:8080 gridphoto