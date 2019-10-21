import discord
import sys
import random
import os
import jishaku
import urllib
import asyncio
import time
import requests
import urllib.request
from discord.ext import commands
import discord, traceback, asyncio
import hashlib
def md5_encrypt(text):
    return hashlib.md5(bytes(text,'utf8')).hexdigest()
bot = commands.Bot(command_prefix='cloudmouse>')
bot.offline = "<:offline:634770176579076128>"
bot.online = "<:online:634770177036255244>"
bot.cpu = "<:servercpu:635323585568702475>"
bot.kvm = "<:kvm:635368984992022530>"
bot.hyperv = "<:hyper-v:635368053550350336>"
bot.remove_command('help')
bot.load_extension('jishaku')
TOKEN = 'NjM0NTk3MjAzMTU0ODI5MzI2.Xak1Cw.tQicVvLSFkxcNVj7mzjbs-hY1oY'
def check(url):
	try:
		res = requests.get(url)
	except: return False
	else:
		if res.status_code == 404: 
			print("0")
		else:
			print("1")

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="containers"))
def FileSave(filename,content):
	with open(filename,"a",encoding="utf8") as myfile:
		myfile.write(content)
@Bot.event
async def on_guild_join(guild): # событие подключения к серверу
    category = guild.categories[0] # выбирает первую категорию из сервера, к которому подключился
    channel = category.channels[0] # получает первый канал в первой категории
    await channel.send("Something") # отправка самого сообщения
@bot.event
async def on_message(message):
	args_ = message.content.split()
	args = args_[1:]
	if message.content.startswith("cloudmouse>help"):
		await message.channel.send("start **type_of_server** - Start your server!\ncontainer -type - types of containers\nupload - save files on your cloud\ndownload - download files from your cloud\nfile.add - Add files to your cloud!\ndatacenters - datacenters in online\nstart.container - start your new virtual container with MouseCore!\ncm2 - start CloudMouse Containers!")
	if message.content.startswith("cloudmouse>start"):
		argument1 = args[0]
		if argument1 == "fileserver":
			if os.path.isdir(str(message.author.id)):
				await message.channel.send(":x: You already have container :x:")
			else:
				message1 =  await message.channel.send("Preparing to create container...")
				await asyncio.sleep(5)
				await message1.edit(content=":x: - Now works. :white_check_mark: - Done\n:x: Creating container\n:x: Installing OS\n:x: Installing FTP")
				await asyncio.sleep(10)
				await message1.edit(content=":x: - Now works. :white_check_mark: - Done\n:white_check_mark: Creating container\n:x: Installing OS\n:x: Installing FTP")
				await asyncio.sleep(20)
				await message1.edit(content=":x: - Now works. :white_check_mark: - Done\n:white_check_mark: Creating container\n:white_check_mark: Installing OS\n:x: Installing FTP")
				await asyncio.sleep(30)
				await message1.edit(content=":x: - Now works. :white_check_mark: - Done\n:white_check_mark: Creating container\n:white_check_mark: Installing OS\n:white_check_mark: Installing FTP")
				await asyncio.sleep(5)
				await message1.edit(content="Successful! That's log for you:\nCreating container...\nInstalling Windows Server 2016...\nDone\nStarting container...\nStarted.\nSuccessful installed fileserver.Success.")
				CLOUDMOUSE_CLIENT = message.author.id
				os.system(f"mkdir {CLOUDMOUSE_CLIENT}")
	if message.content.startswith("cloudmouse>container -type"):
		await message.channel.send("Containers types:\nFileserver\nVDS[Not works]\nVDC[Not works]")
	if message.content.startswith("cloudmouse>upload"):
		url = args[0]
		filename = args[1:]
		if os.path.isdir(str(message.author.id)):
			if url == "" or 'ip' in url:
				await message.channel.send(":x: URL EMPTY")
			else:
				if filename == "":
					await message.channel.send(":x: FILENAME EMPTY")
				else:
					urllib.request.urlretrieve(str(url),str(message.author.id) + "/" + ' '.join(args[1:]))
					await message.channel.send("Success.")
	if message.content.startswith("cloudmouse>mydisk.files"):
		DISK = message.author.id
		os.system(f"dir {DISK} >> {DISK}/result.txt")
		await message.channel.send(open(f"{DISK}/result.txt",'r').read())
		os.system(f"rm -r {DISK}/result.txt")
	if message.content.startswith("cloudmouse>download"):
		file = args[0]
		DISK = message.author.id
		if os.path.isdir(f"{DISK}"):
			if os.path.isfile(f"{DISK}/{file}"):
				message_about_download = await message.channel.send("Wait please... Uploading file to discord servers and sending for you...")
				try:
					fname = str(message.author.id) + "/" + file
					await message.author.send("Hello! That's file for you!\n", file=discord.File(fp=fname, filename=file))
					await message_about_download.edit(content="Success.")
				except:
					await message.channel.send("*LOG:Error happened!*")
			else:
				await message.channel.send(":x: File not found!")
		else:
			await message.channel.send("Failure find your container")
	if message.content.startswith("cloudmouse>discord.servers"):
		test = await message.channel.send("[!] That`s can take a few minutes. \nTest")
		for check in range(0,101):
			await test.edit(content=f"[!] That`s can take a few minutes. \nSearching servers... {check}%") 
		await test.edit(content="I Found me in servers:\n" + '\n'.join([x.name for x in bot.guilds]))
	if message.content.startswith("cloudmouse>file.add"):
		filename = args[0]
		filetext = args[1:]
		if filename == "":
			await message.channel.send(":x: Heyy! I can't find a filename!")
		else:
			if os.path.isfile(str(message.author.id) + "/" + ' '.join(args[0])):
				await message.channel.send(":x:")
			else:
				await message.channel.send(":white_check_mark:")
				FileSave(str(message.author.id) + "/" + ''.join(args[0]),' '.join(args[1:]))
	if message.content.startswith("cloudmouse>datacenters"):
		datacenters = await message.channel.send("Checking availability datacenters")
		for detect_datacenter_status in range(0,31):
			if detect_datacenter_status == 30:
				await datacenters.edit(content="All datacenters online")
			else:
				await datacenters.edit(content=f"Detecting datacenters status... {detect_datacenter_status}/30")
	if message.content.startswith("cloudmouse>old.stat"):
		await message.channel.send(f"Information about your container:\nIP: 192.168.1.49\nGateway: cloudmouse.servers.1\nDNS:8.8.8.8 8.8.4.4\nServer status: {bot.online}\nOS: Linux\nRAM:256MB\nDisks: 4\nRunning in datacenter: CloudMouse Kazakhstan")
	if message.content.startswith("cloudmouse>start.container"):
		if ''.join(args[0]) == "cloud":
			if ' '.join(args[1:]) == "":
				builder = await message.channel.send("Preparing to start container...")
				for container_starter in range(0,101):
					if container_starter != 100:
						await builder.edit(content=f"Oops! Queue! Wait please! STARTED CONTAINERS: {container_starter}%")
					else:
						for starting_container in range(0,4):
							if starting_container != 3:
								await builder.edit(content="Loading container... | ( " + str(starting_container) + " )")
								await asyncio.sleep(0.1)
								await builder.edit(content="Loading container... /")
								await asyncio.sleep(0.1)
								await builder.edit(content="Loading container... -")
								await asyncio.sleep(0.1)
								await builder.edit(content="Loading container... \\")
								await asyncio.sleep(0.1)
								await builder.edit(content="Loading container... |")
								await asyncio.sleep(0.1)
							else:
								screen = await message.channel.send("CloudMouse Container Starting...")
								await asyncio.sleep(10)
								await screen.edit(content="Starting MouseLinux...")
								await asyncio.sleep(0.5)
								await screen.edit(content="Starting MouseLinux...\nPreparing to load extensions...")
								await asyncio.sleep(5)
								await screen.edit(content="Starting MouseLinux...\nPreparing to load extensions...\nOK.")
								await asyncio.sleep(0.58)
								await screen.edit(content="Starting MouseLinux...\nPreparing to load extensions...\nOK.\nIP:129.49.107." + str(random.randint(0,255)))
								await asyncio.sleep(0.10)
								await screen.edit(content="")
								await asyncio.sleep(5)
								await screen.edit(content="Welcome to MouseLinux\nUsername:")


			else:
				await message.channel.send(":x: Code not found! :x:")
		else:
			await message.channel.send(":x: Container type not found :x:")
	if message.content.startswith("cloudmouse>disk -a"):
		await message.channel.send(f"Disk 1 {bot.online}\nDisk 2 {bot.online}\nDisk 3 {bot.online}\nDisk 4 {bot.online}\nDisk 5 {bot.online}\nDisk 6 {bot.online}")
	if message.content.startswith("cloudmouse>disk"):
		await message.channel.send(":x: I don't have a arguments.")
	if message.content.startswith("cloudmouse>disk --help"):
		await message.channel.send("-a - Disks status\n--help - this list")
	if message.content.startswith("cloudmouse>power.off"):
		if open("status.txt",'r').read() == "False":
			embed=discord.Embed(title="Server already offline", color=0xff0000)
			await message.channel.send(embed=embed)
		else:			
			embed=discord.Embed(title="Server is shutting down ... OK", color=0xff0000)
			await message.channel.send(embed=embed)
			open("status.txt",'w').write("False")
	if message.content.startswith("cloudmouse>power.on"):
		if open('status.txt','r').read() == "True":
			embed=discord.Embed(title="Server already online.", color=0x00ff00)
			await message.channel.send(embed=embed)
		else:			
			embed=discord.Embed(title="The server is turning on ... OK", color=0x00ff00)
			await message.channel.send(embed=embed)
			open("status.txt",'w').write("True")
	if message.content.startswith("cloudmouse>statistic"):
		if message.author.id == 554539601977409536:
			if open("status.txt",'r').read() == "False":
				embed=discord.Embed(title="CloudMouse Administrator Panel", description="Welcome,admin!", color=0x008000)
				embed.set_author(name="CONTROL PANEL (SSL)", icon_url="https://cdn11.bigcommerce.com/s-6e5d5/images/stencil/900x900/products/6620/15766/r820-8port-nobezel__19090.1489525892.png?c=2&imbypass=on")
				embed.set_thumbnail(url="https://smhttp-ssl-67598.nexcesscdn.net/media/catalog/product/cache/1/image/1600x/040ec09b1e35df139433887a97daa66f/p/e/per820-16x2.5_front_base.jpg")
				embed.add_field(name="OS", value="MouseLinux v7", inline=True)
				embed.add_field(name="Processor", value="Intel Xeon E7-8890V4 (x4)", inline=False)
				embed.add_field(name="RAM", value="512GB DDR4 Kingston", inline=False)
				embed.add_field(name="Virtualization", value=f"KVM + Hyper-V", inline=False)
				embed.add_field(name="Server Status", value=f"{bot.offline}", inline=True)
				embed.set_footer(text="CloudMouse Server")
			else:
				cpu_usage = random.randint(0,7)
				embed=discord.Embed(title="CloudMouse Administrator Panel", description="Welcome,admin!", color=0x008000)
				embed.set_author(name="CONTROL PANEL (SSL)", icon_url="https://cdn11.bigcommerce.com/s-6e5d5/images/stencil/900x900/products/6620/15766/r820-8port-nobezel__19090.1489525892.png?c=2&imbypass=on")
				embed.set_thumbnail(url="https://smhttp-ssl-67598.nexcesscdn.net/media/catalog/product/cache/1/image/1600x/040ec09b1e35df139433887a97daa66f/p/e/per820-16x2.5_front_base.jpg")
				embed.add_field(name="OS", value="MouseLinux v7", inline=True)
				embed.add_field(name="Processor", value="Intel Xeon E7-8890V4 (x4)", inline=False)
				embed.add_field(name="RAM", value="512GB DDR4 Kingston", inline=False)
				embed.add_field(name="Virtualization", value=f"KVM + Hyper-V", inline=False)
				embed.add_field(name="Server Status", value=f"{bot.online}", inline=True)
				embed.add_field(name=":zap: Usage CPU", value=f"{cpu_usage}%", inline=False)
				embed.set_footer(text="CloudMouse Server")
		else:
			await message.channel.send(":x: Access denied :x:")
		await message.channel.send(embed=embed)
	if message.content.startswith("cm2>help"):
		await message.channel.send("create - create container automatically with recommended options.\nlist - your containers\nhelp - this help\nconnect **port** - connect to your container!\nlist - list of your containers!\nexec **port** **command** - execute commands on your container")
	if message.content.startswith("cm2>create"):
		if os.path.isdir("containers/" + str(message.author.id)):
			port = random.randint(0,65536)
			username = md5_encrypt(message.author.name)
			FileSave("containers/" + str(message.author.id) + "/containers.txt",f"{bot.online} [MouseLinux] [1024MB] [Intel Xeon E3] [Mini-1] [{port}]\n")
			FileSave("containers/" + str(message.author.id) + f"/{port}.txt",f"Welcome to MouseLinux!\nUsername:{username}\nPassword:********************************\nCPU : Intel Xeon E3\n1GB of RAM\n")
			embed=discord.Embed(title="Builded", color=0x00ff00)
			await message.channel.send(embed=embed)
			open("containers/" + str(message.author.id) + "/" + "files-" + str(port) + ".txt",'w').write("kernel/\n")
		else:
			os.mkdir("containers/" + str(message.author.id) + "/")
			open("containers/" + str(message.author.id) + "/containers.txt",'w').write("")
			embed=discord.Embed(title="Your account registered.Please re-create container", color=0x00ff00)
			await message.channel.send(embed=embed)
	if message.content.startswith("cm2>list"):
		if os.path.isdir("containers/" + str(message.author.id)):
			if open("containers/" + str(message.author.id) + "/containers.txt",'r').read() == "":
				embed=discord.Embed(title="You don't have containers! Time to create container!", color=0xff0000)
				await message.channel.send(embed=embed)				
			else:
				await message.channel.send(open("containers/" + str(message.author.id) + "/containers.txt",'r').read() )
		else:
			await message.channel.send("You don't have a containers.")
	if message.content.startswith("cm2>connect"):
		username = message.author.name
		if os.path.isfile("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt"):
			if f"{bot.online} [MouseLinux] [1024MB] [Intel Xeon E3] [Mini-1] [" + ''.join(args[0]) + "]" or f"{bot.online} [MouseLinux] [131072MB] [Intel Xeon E7] [Mini-1] [" + ''.join(args[0]) + "]" or f"{bot.online} [MouseLinux] [256000MB] [Intel Xeon E7] [Mini-1] [" + ''.join(args[0]) + "]" in open("containers/" + str(message.author.id) + "/" +"containers.txt",'r').read():
				CONTAINER_CONTENT = await message.channel.send("Connecting to container via CMRD..")
				await asyncio.sleep(6)
				await CONTAINER_CONTENT.delete()
				screen = await message.channel.send(content="```\n" + open("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt",'r').read() + "\n```")
				await screen.add_reaction("🔁")
				while True:
					try: r = await bot.wait_for('reaction_add', check=lambda r, u: u.id == message.author.id and r.emoji in "🔁", timeout=300)
					except: return await screen.edit(content='Timeout')
					if r[0].emoji == '🔁':
						await screen.edit(content="```\n" + open("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt",'r').read() + "\n```")
			else:
				embed=discord.Embed(title="Remote Screen", description="The server is currently unavailable.", color=0xff0000)
				await message.channel.send(embed=embed)
		else:
			embed=discord.Embed(title="You don't have a container or don't have a account in CM2", color=0xff0000)
			await message.channel.send(embed=embed)
	if message.content.startswith("cm2>exec"):
		if os.path.isfile("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt"):
			if ''.join(args[1:]) == "": 
				embed=discord.Embed(title="Server : " + ''.join(args[0]), description="OK", color=0x373737)
				embed.set_author(name="CloudMouse")
				await message.channel.send(embed=embed)
			if ''.join(args[1:]) == "ifconfig":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt","ifconfig:\nmodem {\n IP:192.168.1.0\nDNS:8.8.8.8 8.8.4.4\nGateway:124.10.192.39\n}\n")
			elif ''.join(args[1:]) == "netstat":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt","netstat:\n127.0.0.1 >> 127.0.0.1\n")
			elif ''.join(args[1:]) == "help":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt","help:\nnetstat - Connections\nifconfig - network configuration\ncls\nping\nwhoami\ndir\nfree\ndisconnect\n")
			elif ' '.join(args[1:]) == "apt-get update":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt","apt-get update:\nChecking updates...\ncloudmouse://192.168.1.50/*.cpk\ncloudmouse://192.168.1.57:27384/*.cpk\ncloudmouse://192.168.1.21:19200/*.cpk\nNot Found! *404 HTTP/Code*\n")
			elif ''.join(args[1:]) == "cls":
				open("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt",'w').write('')
			elif ''.join(args[1:]) == "ping":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt","ping:\nPong!\n")
			elif ''.join(args[1:]) == "whoami":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt","root\n")
			elif ''.join(args[1:]) == "dir":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt",open("containers/" + str(message.author.id) + "/" + "files-" + ''.join(args[0]) + ".txt",'r').read())
			elif ' '.join(args[1:]) == "uname -a":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt","CloudMouse Linux For Data Centers v0.495 Beta\n")
			elif ' '.join(args[1:]) == "free":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt",' '.join(args[2:]) + "TOTAL:100%\nFree:97.60%\nUsed:3.30%\n")
			elif ' '.join(args[1:]) == "disconnect":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt",'>logout')
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt",'WARN : User root disconnected from server.')
				await screen.delete()
			elif ' '.join(args[1:]) == "tna -g":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt","Build|Wait please...\n")
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt","Build|Done!\n")
			elif ' '.join(args[1:]) == "fixload":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt","FixLoad: Done! Bootloader recreated\n")
			elif ' '.join(args[1:]) == "0":
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt","0 |" + str(False) + " < Returned\n")
			else:
				FileSave("containers/" + str(message.author.id) + "/" + ''.join(args[0]) + ".txt","Command '" + ' '.join(args[1:]) + "' not found!\n")
		else:
			embed=discord.Embed(title="Server : ", description="Failure.I can't find your container!", color=0x373737)
			embed.set_author(name="CloudMouse")
			await message.channel.send(embed=embed)
bot.run(TOKEN)
