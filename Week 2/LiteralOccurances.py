 # ListOccurances.py
 
 # Method 0:
def countChars(x) :
    print("\nCountChars()...")
    unique = []
    for i in x:
        if i not in unique:
            unique.append(i)
            print(f"{i} occurs {x.count(i)} times")

# Method 1:
# Python3 implementation to print the characters and frequencies in order of its occurrence.
def printCharacterWithFrequency(inputStr):
    print("\printCharacterWithFrequency()...")
    # Store all characters and their frequencies in dictionary
    d = {}
    for i in inputStr:
        #print(i, d)
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
     
    # Print characters and their frequencies in same order of their appearance
    for i in inputStr:
 
        # Print only if this character is not printed before. 
        if d[i] != 0:
            # print("{}{}".format(i,d[i]), end =" ")
            print(f"{i} occurs {d[i]} times")
            d[i] = 0
      
     
if __name__ == "__main__" :
    #inputStr = "It was the best of times. It was the worst of times."
    inputStr = "My name is Ajay Singala"
    print("String:", inputStr)
    print("Literal Occurances...")
    printCharacterWithFrequency(inputStr)
    countChars(inputStr)

# Method 2:
# Using built-in Python function Counter().
from collections import Counter

def prCharWithFreq2(string):
    print("\nprCharWithFreq2() using Counter() collection...")
    # Store all characters and their frequencies using Counter function
    d = Counter(string)
    
    # Print characters and their frequencies in same order of their appearance
    for i in d:
        print(i+str(d[i]), end=" ")

string = "It was the best of times. It was the worst of times."
print("\n\nString: ",string, " using Counter()...")
prCharWithFreq2(string)
