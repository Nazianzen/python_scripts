import os, glob

os.chdir("C:/Users/GIDEON/Documents/")
for file in glob.glob("*.txt"):
  print(file)
