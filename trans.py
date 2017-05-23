import time
name = raw_input("please enter name of plaintext file... include extension , .txt, .bin, etc..")
myfile = open(name, "r")

b = ""

for line in myfile:
	b = b + line
	print b

myfile.close()

b = b.replace("\n\n","|")
b = b.replace("\n", " ")
b = b.replace("|", "\n\n")
print b
myfile = open(name, "w")
myfile.write(b)
myfile.close()
