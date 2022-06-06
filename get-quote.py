import random

def primary():
  #print("Keep it logically awesome.")
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    
    quo = random.choice(quotes)
    print(quo)

if __name__== "__main__":
    primary()
