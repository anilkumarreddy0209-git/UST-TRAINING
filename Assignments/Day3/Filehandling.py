import os
os.mkdir("Mydirectory")
os.getenv("C:/Users/Administrator")
a=open("C:/Users/Administrator/Desktop/Mydirectory/Myfile.txt","w+")
a.write("Welcome to the data engineering")
a.write(" Welcome to the UST Global")
a.seek(0)
b=a.read()
print(b)
a.close()

"""Delete the empyt directoyr"""
import os
os.rmdir("C:/Users/Administrator/Desktop/Training")

"""Delete the non empty directory"""

import shutil
shutil.rmtree("C:/Users/Administrator/Desktop/Normal")