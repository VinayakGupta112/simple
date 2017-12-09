#Problem:Problem:- To create a program which tells which year is leap year and which one is not. Also, all years divisible by 400 are leap years, but the ones divisible by 100 are not.
def leap_year(x):
    if x%400==0:
        print ("Leap Year")
    else:
        if x%4==0:
            if x%100!=0:
                print ("Leap Year")
            else:
                print ("Not a Leap Year")
        else:
            print ("Not a Leap Year")

             
