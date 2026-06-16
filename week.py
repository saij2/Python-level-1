'''
1 - > Monday 
2 -> Tuesday 
.
.
.
7 -> Sunday 

'''
week_number = int(input("Enter the week number: "))

# if week_number == 1:
#     print("Monday")
# elif week_number == 2:
#     print("Tuesday")
# elif week_number == 3:
#     print("Wednesday")
# elif week_number == 4:
#     print("Thursday")
# elif week_number == 5:
#     print("Friday")
# elif week_number == 6:
#     print("Saturday")
# elif week_number == 7:
#     print("Sunday")
# else:
#     print("Invalid week number")
    
# match statement 
match week_number:
    case 1: # this is equal to week_number === 1 
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _ : # default case it will be executed when none of the above cases is matched 
        print("Invalid week number")
