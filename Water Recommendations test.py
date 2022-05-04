# This will tell you the amount of water you should drink a day
# The results of the calculated number, is based on a formula backed up by science
# Forget the "drink eight glasses of water a day" myth.
# Made by:
# @archaeplastida
###############################################################################################

# The reason for the loop is because to make an easier way to script the "y/n" options

while True:
    
    pounds = int(input("How much do you weigh in LB>>> "))
    
    print("---------------------------------------------")
    
    ##################################################
    # The variables for measuring in Ounces(OZ)
    amtofwater_lesser = pounds/2
    
    amtofwater_greater = (pounds + (pounds//2))/2
    ##################################################
    
    print("The recommended amount for the %s LB person is: %s-%s OZ of water daily."
          
          % (pounds, int(amtofwater_lesser), int(amtofwater_greater)))
    
    print("That's like drinking ~ %.0f-%.0f 25 OZ bottles!"
          
          % (amtofwater_lesser/25,amtofwater_greater/25))
    
    ml = input("\nWould you like this in additional units (y/n)>>> ")
    
    if ml == "n":
        
        break
    
    while ml != "y":
        
        ml = input("Choose a VALID input (y/n)>>> ")
        
        if ml == "y":
            
            break
        
        if ml == "n":
            
            break
        
    if ml == "n":
        
        break
    
###########################################################################
    
    
# This is only printed IF they chose "y" for the additional measurements input
    
    
    print("---------------------------------------------")
    
    
    print("You would need %s-%s mL of water daily." %
          
          (int(amtofwater_lesser*29.5735),int(amtofwater_greater*29.5735)))
    
    print("\nYou would need ~ %.1f-%.1f L of water daily." %
          
          (amtofwater_lesser/33.814,amtofwater_greater/33.814))
    
    print("\nYou would need ~ %.1f-%.1f Gallon(s) of water daily." %
          
          (amtofwater_lesser/128,amtofwater_greater/128))
    
    
    print('\nThe "~" means "approximately')
           
    
    break

# Alas, the 2-way single loop has finished

###############################################################################################

# Made 4/28/2022

print("---------------------------------------------")

print("\nMake sure you stay HYDRATED, and drink in the recommended range.")
