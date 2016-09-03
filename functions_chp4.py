#########################
#Functions from Chapter 4
#########################

#check if a integer is even - printParity
def printParity(x):
    if x%2 == 0:
        print x, "is even"
    else:
        print x, "is odd"

#compares two integers - compare
def compare(x,y):
    if x<y:
        print x, "is less than", y
    elif x > y:
        print x, "is greater than", y
    else:
        print x, "and", y, "are equal"

#selects a function based on a parameter - dispatch
def dispatch(choice):
    if choice == "A":
        functionA()
    elif choice == "B":
        functionB()
    elif choice == "C":
        functionC()

#prints a countdown - countdown
def countdownr(n):
    if n == 0:
        print "Blastoff!"
    else:
        print n
        countdownr(n-1)

#prints a user specified number of lines - nLines
def nLines(n):
    if n > 0:
        print
        nLines(n-1)

