# -*- coding: utf-8 -*-

import re
tables = []
#for line in open("models.py"):
text = open("models.py")
r = text.read()
text.close()
names = re.findall(r"class (\w+?)\(",r,re.S)

#for name in names:
#   tables.append(name.group()[6:-1])
#print tables
def getT():
   return names
