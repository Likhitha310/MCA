import os
from pathlib import Path

# Deleting all the .class files in the directory.
dir_name = "C:/Users/1kryo/Documents/Github/MCA/MCA-Sem1/OOPS_lab/"
test = os.listdir(dir_name)
for item in test:
    if item.endswith(".class"):
        os.remove(os.path.join(dir_name, item))
