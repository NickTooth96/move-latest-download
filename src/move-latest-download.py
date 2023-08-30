import os
import platform

dirpath = os.getcwd()
system = platform.system()
user = os.path.expanduser('~')

print(dirpath)
print(system)
print(user)


downloads_path = {"Linux" : user, "Windows": "'C:\'"}
for root, dirs, files in os.walk(downloads_path[system], topdown=False):
   for name in files:
      if name == "Downloads":
        print(os.path.join(name))