#!/usr/bin/python3

print("Content-type: text/html")
print("")

def add(b):
	return b+b

a=2
print("<p>",add(a),'</p>')

for i in range(add(a)):
	print("le chiffre: ",a)
