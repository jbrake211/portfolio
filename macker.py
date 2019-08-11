import subprocess
import random
import time
import getpass

def interface():
	interface=input("Plese enter interface for the mac address you want to change:")
	return interface

def random_gen():
	random_mac=input("Would you like a random MAC address? Y/N:")
	if random_mac == "Y" or random_mac == "y":
		i=0
		ranmacap=[]
		while i < 6:
			stringrand=["A","B","C","D","E","F"]
			random_num=random.randint(0,5)
			random_string=stringrand[random_num]
			ranstr=random_string
			ranmac=ranstr+str(random_num)
			i=i+1
			ranmacap.append(ranmac)
		raneven=["0","2","4","6","8"]
		ranmacap[0]=ranstr + raneven[random_num]
		randmacchange=ranmacap[0] + ":" + ranmacap[1] + ":" + ranmacap[2] + ":" + ranmacap[3] + ":" + ranmacap[4] + ":" + ranmacap[5]
		return randmacchange
	elif random_mac == "N" or random_mac =="n":
		static_mac=input("Please enter a custom MAC address you would like to add (EX: A2:B4:C6:D8:EC:F2):")
		return static_mac
	else:
		return print("Please enter Y or N to continue:")

subprocess.call("clear", shell=True)

print("***************************************************")
print("*						  *")
print("*      MACKER - MASK YOUR TRUE MAC ADDRESS        *")
print("*                    BY:	JB	                     *")
print("*                                                 *")
print("* Must be logged in as root to change MAC Address *")
print("*						  *")
print("***************************************************")
print("\n")

whoami=getpass.getuser()

if whoami == "root":

    randommacaddress=random_gen()
    result=interface()

    while result=="":
	    x=0
	    while x < 4:
		    x=x+1
		    result=interface()
	    break

    if result=="":
	    subprocess.call("clear", shell=True)
	    print("You have attempted too many times, program is terminating....")
    else:
	    subprocess.call("ifconfig " + result + " down", shell=True)
	    print("Please wait, your MAC address change is being processed.....")
	    time.sleep(5)
	    subprocess.call("clear", shell=True)
	    print("Your old MAC Address is:")
	    subprocess.call("ifconfig " + result + " | grep ether", shell=True)
	    try:
		    subprocess.call("ifconfig " + result + " hw ether " + randommacaddress, shell=True)
		    subprocess.call("ifconfig " + result + " up", shell=True)
		    print("\n")
		    print("Your new MAC Address is:")
		    subprocess.call("ifconfig " + result + " | grep ether", shell=True)
		    print("\n")
	    except:
		    print("MAC Address cannot change at the moment, please try your request again.......")
else:
    print("You are not root or logged in as super user.......")
