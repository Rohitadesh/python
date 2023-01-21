import time
timer=int(input())
while True:
	print(timer)
	timer-=1
	time.sleep(1)
	if timer==0:
		print("its finished")
		break
	elif timer<0:
		print("its not finished")
		break

