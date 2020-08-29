import random
l='   YOU LOST ! ! !'
w='   YOU WON ! ! !'
d='   DRAW ! ! !'
def logic(n):
	comp_res=random.randint(1,3)
	print("")
	print("   YOUR response : ",n)
	print("   CPU response : ",comp_res)
	print("")
	if n==comp_res:
		print(d)
	elif n==1:
		if comp_res==2:
			print(l)
		else:
			print(w)
	elif n==2:
		if comp_res==1:
			print(w)
		else:
			print(l)
	elif n==3:
		if comp_res==1:
			print(l)
		else:
			print(w)
			
		
print("ENTER : ")
print("         '1' for STONE")
print("         '2' for PAPER")
print("         '3' for SCISSOR")
response=int(input("   Enter ypur response : "))
print()
if response in (1,2,3):
	logic(response)
else:
	print("   PLEASE enter 1 , 2 or 3 .")