import requests
import os

print('Dragoncord Installer for Windows x64')
input('Press ENTER to continue')

print('Downloading Dragoncord and tools to run it, please wait...')
print()

# Git
print('[Git] Downloading git...')
print('[Git] https://github.com/git-for-windows/git/releases/download/v2.36.1.windows.1/Git-2.36.1-64-bit.exe')

gitExe = requests.get("https://github.com/git-for-windows/git/releases/download/v2.36.1.windows.1/Git-2.36.1-64-bit.exe")
open("Git-2.36.1-64-bit.exe", "wb").write(gitExe.content)

print('[Git] Downloaded! Opening...')
os.system("Git-2.36.1-64-bit.exe")

# NodeJS
print()
print('[NodeJS] Downloading nodejs')
print('[NodeJS] https://nodejs.org/dist/v16.15.1/node-v16.15.1-x64.msi')

nodejsMsi = requests.get("https://nodejs.org/dist/v16.15.1/node-v16.15.1-x64.msi")
open("node-v16.15.1-x64.msi", "wb").write(nodejsMsi.content)

print('[Git] Downloaded! Opening...')
os.system("node-v16.15.1-x64.msi")

print()
print('[Dragoncord] Downloading Dragoncord')
print('[Dragoncord] git clone https://github.com/Dragoncord-for-discord/dragoncord')
os.system("git clone https://github.com/Dragoncord-for-discord/dragoncord")
print()
print('[Dragoncord] cd dragoncord')
os.system("cd dragoncord")
print('[Dragoncord] npm i')
os.system("npm i")
print()
print('[Dragoncord] Starting')
os.system("Run.bat")
