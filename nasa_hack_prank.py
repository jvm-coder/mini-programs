import time

def dot_print(p,t):
	for i in range(4):
		print(p+"."*i+" "*(3-i),end="\r")
		time.sleep(t)

dot_print("Starting attack",2)
dot_print(" Hacking NASA 0%",1)
dot_print("  Hacking NASA 20%",1)
dot_print("  Hacking NASA 40%",1.5)
dot_print("  Hacking NASA 60%",1.5)
dot_print("  Hacking NASA 80%",1)
dot_print("  Hacking NASA 80%",1)
dot_print("  Hacking NASA 99%",1.5)
dot_print("  Hacking NASA 99%",1.5)
dot_print("  Hacking NASA 99%",1.5)
print("\nNASA Hacked Successfully !!!")
