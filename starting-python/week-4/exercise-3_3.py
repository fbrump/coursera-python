# Exercise: Rewrite your pay computation to give the employee 1.5
#   times the hourly rate for hours worked above 40 hours.

# Input   
hrs = raw_input('Enter hours: ')
rat = raw_input('Enter Rate: ')
pay = -1

try:
    # Convert types
    hrs = int(hrs)
    rat = int(rat)
    
    # Conditions
    if (hrs > 40):
        # Calculation
        pay = (40 * rat) + ((hrs - 40) * 15)
    else:
        # Calculation
        pay = hrs * rat
    # Output
    print('Enter Hours: ' + str(hrs))
    print('Enter Rate: ' + str(rat))
    print('Pay: ' + str(pay))
except:
    print('Error, please enter numeric input.')
