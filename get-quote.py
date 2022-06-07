import random
import sys

act = input("What would you like to do, add or read a quote? \n")


#Defining Function for read quote
def primary():
  #print("Keep it logically awesome.")
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    
    for i in range(0,2):
        quo = random.choice(quotes)
        print(quo)
#Defining Function for add quote
def secondary():
    quot = input("Please enter your quote? \n\n")    
    sys.stdout = open('quotes.txt', 'a')
    print(quot)    

#code to get which function to run
if act == "read":
    primary()
else:
    secondary()    

    
#if __name__== "__main__":
    #primary()
