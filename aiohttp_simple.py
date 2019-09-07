from aiohttp import web
from mako.template import Template
import os

path = os.getcwd()
index=0
files = []
f = []
dirs = []

def load_folder(folder):
	global index
	global f
	global dirs
	dirs.clear()
	files.clear()
	f.clear()
	print('loading ' + folder)
	ext = [".jpg" , ".jpeg", ".gif", ".png", ".bmp"]
	for item in os.listdir(folder):
		if os.path.isfile(os.path.join(folder, item)):
			if item.endswith(tuple(ext)):
				files.append(os.path.join(folder, item))
				f.append(item)
			print(item)
		else:
			dirs.append(os.path.join(folder, item))
			print(item)

def load_folder2(folder):
	global index
	global f
	global dirs
	dirs.clear()
	files.clear()
	f.clear()
	print('loading ' + folder)
	ext = [".jpg" , ".jpeg", ".gif", ".png", ".bmp"]
	for r, d, f in os.walk(folder):
		print(r)
		dirs.append(r)
		for file in f:
			#if '.jpg' in file:
			if file.endswith(tuple(ext)):
				files.append(os.path.join(r, file))

def load_index(index):
	filetemp = Template(filename='slideshow2.html')
	next = index+1
	if next >= len(f):
		next = 0
	return filetemp.render(dirs=dirs,folder=path,files=f,index=index,max=len(f),next=next)

def load_slideshow(index):
	filetemp = Template(filename='slideshow.html')
	next = index+1
	if next >= len(f):
		next = 0
	print(dirs)
	if not files and len(f) > 0:
		return filetemp.render(dirs=dirs,folder=path,image=files[index],files=f,index=index,max=len(f),next=next)
	else:
		return filetemp.render(dirs=dirs,folder=path,files=f,index=index,max=len(f),next=next)

async def delete_me(request):
	print(request.url)
	data = await request.post()
	image = data['image']
	print(image)
	matching = [s for s in files if image in s]
	print(matching)
	if os.path.exists(str(matching[0])):
		os.remove(str(matching[0]))
		files.remove(str(matching[0]))
		f.remove(image)
		print("The file does exist")
	else:
		print("The file does not exist")
	return web.Response(text=image)

async def goup(request):
	global path
	path = os.path.dirname(path)
	filetemp = Template(filename='goup.html')
	load_folder(path)
	return web.Response(text=filetemp.render(folder=path), content_type='text/html')

async def slideshow(request):
	global path
	print(request.url)
	data = await request.post()
	try:
		folder = data['folder']
		if not folder:
			folder=path
		elif folder != path:
			print(folder)
			load_folder(folder)
			path = folder
		return web.Response(text=load_slideshow(index), content_type='text/html')
	except Exception as e:
		print(e)
		print("An exception occurred")
		return web.Response(text='dicks')

async def handle_images(request):
	name = request.match_info.get('name', "Anonymous")
	#print(request.match_info.get('name', "Anonymous"))
	#print('handle')
	#print(request.url)
	print(name)
	matching = [s for s in files if name in s]
	print(matching)
	return web.FileResponse(matching[0])

async def handle_index(request):
	name = request.match_info.get('name', "Anonymous")
	print(name)
	index = int(name)
	#filetemp = Template(filename='index.html')
#	test = {"name1":{"text":"my text 1", "status":"my status"}, "name2":{"text":"my text 2", "status":"my status"}}
#	print(filetemp.render(data=test,files=files))
	return web.Response(text=load_index(index), content_type='text/html')

async def favicon(request):
	print('favicon')
	print(request.url)
	return web.FileResponse('W:\\1.jpg')

async def root(request):
	print('root')
	print(request.url)
#	test = {"name1":{"text":"my text 1", "status":"my status"}, "name2":{"text":"my text 2", "status":"my status"}}
#	print(filetemp.render(data=test,files=files))
	return web.Response(text=load_index(index), content_type='text/html')

load_folder(path)
app = web.Application()
app.add_routes([
				web.post('/goup', goup),
				web.post('/delete', delete_me),
				web.post('/slideshow', slideshow),
				web.get('/favicon.ico', favicon),
				web.get('/{name:\d+}', handle_index),
				web.get('/images/{name}', handle_images),
				web.get('/', root)
				],)

web.run_app(app)