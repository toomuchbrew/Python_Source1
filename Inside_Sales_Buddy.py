import time
import os

# change Version information here:
version = "Version 1.20"
name = "  INSIDE SALES BUDDY"

def menu():
	print
	os.system("cls")
	os.system("color 0A")
	print "",name, version
	print "  ------------------------------------"
	print "  1.  Lineal Foot to Board Feet"
	print 
	print "  2.  Board Feet to Lineal Foot"
	print
	print "  3.  Square Feet to Lineal Feet"
	print
	print "  4.  Lineal Feet to Square Feet"
	print
	print "  5.  Build Notes"
	print
	print "  6.  Exit Program"
	print
	try:
		choice = int(input("  Enter a Selection from the Menu: "))
	except ValueError:
		ERROR_Integer()
		menu()
	except NameError:
		print
		print " **INVALID INPUT!!**  Please try again using the menu numbers"
		time.sleep(2)
		menu()
	if choice == 1:
		ltob()
	elif choice == 2:
		btol()
	elif choice == 3:
		stol()
	elif choice == 4:
		ltosf()
	elif choice == 5:
		Build_Notes()
	elif choice == 6:
		end_program()
	else:
		print " ERROR:  Restarting Program"
		time.sleep(2)
		menu()

# lineal feet to board feet
def ltob():
	os.system('cls')
	print
	print "  INSIDE SALES BUDDY V1.50: "
	print "    LINEAL TO BOARD FEET: "
	print "  ------------------------------------"
	print "  Input the following information: "
	
	try:
		length = int(input("   Length: ")) 
	except ValueError:
		ERROR_Integer()
		ltob()
	if length <=0:
		ERROR_Foot()
		ltob()
	else:
		print
	
	try:
		t = int(input("   Thickness: "))
	except ValueError:
		ERROR_Integer()
		ltob()
	if t <=0:
		ERROR_Foot()
		ltob()
	else:
		print
	
	try:
		w = int(input("   Width: "))
	except ValueError:
		ERROR_Integer()
		ltob()
	if w <= 0:
		ERROR_Foot()
		ltob()
	else:
		print
	
	print
	print "Conversion is: ", (length * t * w)/12.0, "board feet"
	time.sleep(4)
	menu()
		

# board feet to lineal feet
def btol():
	os.system("cls")	
	print
	print "",name,version
	print "  BOARD FEET TO LINEAL FEET"
	print "  -----------------------------"
	
	try:
		bft = float(input("   Total Board Feet: "))
	except ValueError:
		ERROR_Integer()
		btol()
	if bft <=0:
		ERROR_Foot()
		btol()
	else:
		print
	
	try:
		t = int(input(  "   Thickness: "))
	except ValueError:
		ERROR_Integer()
		btol()
	if t <=0:
		ERROR_Foot()
		btol()
	else:
		print
	
	try:
		w = int(input("   Width: "))
	except ValueError:
		ERROR_Integer()
		btol()
	if w <= 0:
		ERROR_Foot()
		btol()
	else:
		print
	print
	print " Conversion is : ", int(((bft * 12.0)/t)/w), "lineal feet"
	time.sleep(4)
	menu()

# square feet to lineal feet
def stol():
	os.system('cls')
	print
	print "", name,version
	print "  SQUARE FEET TO LINEAL FEET"
	print " -------------------------------"
	
	try:
		sf = int(input("  Square Feet: "))
	except ValueError:
		ERROR_Integer()
	if sf <= 0:
		ERROR_Foot()
		stol()
	else:
		print
		
	try:
		exposure = float(input("  Exposure (in inches): "))
	except ValueError:
		ERROR_Integer()
	if exposure <= 0:
		ERROR_Expose()
		stol()
	else:
		print
	print " Conversion: ", int((sf * 12.0)/exposure), " lineal feet of material"
	time.sleep(4)
	menu()

	
# lineal feet to square feet
def ltosf():
	os.system('cls')
	print
	print "",name,version
	print "  LINEAL FEET TO SQUARE FEET"
	print " -------------------------------"
	
	try:
		lf = int(input("  Lineal Feet: "))
	except ValueError:
		ERROR_Integer()
	if lf <= 0:
		ERROR_Foot()
		ltosf()
	else:
		print
	
	try:
		exposure = float(input(" Exposure (in inches): "))
	except ValueError:
		ERROR_Integer()
	if exposure <= 0:
		ERROR_Expose()
		ltosf()
	else:
		print
	print " Conversion: ", int((lf * exposure)/12.0), " square feet of material"
	time.sleep(4)
	menu()
	
	
def end_program():
	print "  Exiting Program"
	print "   Thanks for using my program"
	print "   A program by Chris Nicholson"
	time.sleep(1)
		
def Build_Notes():
	print "  INSIDE SALES BUDDY"
	print "   BUILD / VERSION NOTES"
	print "  --------------------------------"
	print "  Inside Sales Buddy"
	print "   Developed and Written by Chris Nicholson"
	print "   in Python (May 13, 2015)"
	print
	print "   Current build: ", version
	print "   Version 1.00"
	print "    * Developed/Written in Python from C++"
	print "    * Support for board footage calculations"
	print "   Version 1.01"
	print "    * Support for square footage calculations"
	print "    * Support for Concrete sonotube calculations"
	print "   Version 1.10"
	print "    * Support for 'error handling' in main menu section"
	print "   Version 1.11"
	print "    * changed system colors to green on black background"
	print "   Version 1.20"
	print "    * rewrote program "
	print "    * added error handling to modules"
	print
	print "  Will return to Main Menu"
	time.sleep(6)
	menu()

def ERROR_Integer():
	print " ERROR.  Please use an integer - that's a whole number..."
	time.sleep(1)
	os.system('cls')
	

def ERROR_Foot():
	print " ERROR.  Can not have less than 1 foot - how do you walk?!?"
	time.sleep(1)
	os.system('cls')
	
def ERROR_Expose():
	print " ERROR.  Can not have less than zero exposure - You are crazy!!!"
	time.sleep(1)
	os.system('cls')
	
	
menu()
