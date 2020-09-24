#Airbridge Slope Calculator
#Sean Morrissey
#20180622

print ("Description")
print (" ")     
print ("The following program calculates the slope of a PBB (Passenger Boarding bridge)and displays the following results:")
print (" ")
print ("1. Airbridge slope in degrees")
print ("2. Airbridge gradient")
print ("3. The slope length")
print ("4. The slope percentage")
print ("5. The Horizontal Length")
print (" ")
print ("The calculations can be made using the following aircraft models:")
print (" ")
print ("Boeing Aircraft")
print ("---------------")
print ("1. 737-800")
print ("2. 737-700")
print (" ")
print ("Airbus Aircraft")
print ("---------------")
print ("3. 330-200")
print ("4. 350-1000")
print ("5. 340-600")
print ("6. 380")
print (" ")

#Import modules
import math

#Get PBB Information
#Constants
rot_hinge_dist = 1372 #Rotunda center to hinge distance (Horizontal)
cab_bumper_dist = 3379 #Cab center to bumper distance (Horizontal)
a3_vstep = 344 #Three tunnel airbridge step (Vertical)
a2_vstep = 171 #Two tunnel airbridge step (Vertical)
bumper_threshold = 150 #Threshold of aircraft door to top of bumper

#Variables - Airbridge
rot_rl = int(input("Enter the Rotunda RL in millimeters: "))
apr_rl = int(input("Enter the Apron RL in millimeters: "))
rot_level = rot_rl - apr_rl
rot_cab_dist =  int(input("Enter the center distance from Rotunda to Cab in millimeters: "))

#Variables - Apron
apron_delta_z = int(input("Enter the maximum apron change of level in millimeters: "))

#Get Aircraft Information
aircraft_model = input("Enter the model of aircraft: (eg. 737-800 or 380)")

if aircraft_model == "737-800":
    aircraft_h1 = 2740 #2590 is the fully laden dimension
elif aircraft_model == "737-700":
    aircraft_h1 = 2740 #2590 is the fully laden dimension
elif aircraft_model == "330-200":
    aircraft_h1 = 4630 #4440 is the fully laden dimension
elif aircraft_model == "350-1000":
    aircraft_h1 = 5360 #5050 is the fully laden dimension
elif aircraft_model == "340-600":
    aircraft_h1 = 4600 #4780 is the fully laden dimension
elif aircraft_model == "380": #Door 3 (Upper)
    aircraft_h1 = 8080 #7870 is the fully laden dimension
#elif aircraft_model == "380": #Door 2 (Lower)
    #aircraft_h1 = 5340 #5120 is the fully laden dimension
#elif aircraft_model == "380": #Door 2 (Lower)
    #aircraft_h1 = 5360 #5100 is the fully laden dimension
else:
    aircraft_h1 = 0
    
#Internal Calculations   
#Vertical & Horizontal 
airbridge_delta_x = (rot_cab_dist-rot_hinge_dist)+cab_bumper_dist #Horizotal calulation
#airbridge_delta_z = ((rot_level + apron_delta_z)-((aircraft_h1 - bumper_threshold) +a2_vstep))  #Vertical calculation two tunnel bridge
airbridge_delta_z = ((rot_level + apron_delta_z)-((aircraft_h1 - bumper_threshold) + a3_vstep))#Vertical calculation three tunnel bridge

#Slope
ang_deg = math.degrees(math.atan(airbridge_delta_z/airbridge_delta_x)) #Slope in degrees
ang_grade = airbridge_delta_x/airbridge_delta_z
slope_len = math.sqrt(airbridge_delta_x**2 + airbridge_delta_z**2)
slope_percent = (1/ang_grade)*100

#Output
print (" ")
print (" ")
print ("Results:")
print ("--------")
print ("Airbridge slope in degrees =",ang_deg)
print ("Airbridge gradient is = 1 :",ang_grade)
print ("The slope length is =",slope_len)
print ("The slope % is =",slope_percent)
print ("The Horizontal Length is =", airbridge_delta_x)
print ("The Vertical Height is =", airbridge_delta_z)

