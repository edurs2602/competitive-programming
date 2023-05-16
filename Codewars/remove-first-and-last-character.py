def remove_char(s):
    stringChar = -1
    
    for i in range(len(s)):
    	stringChar += 1
        
    strings = list(s)
    
    del strings[stringChar]
    del strings[0]
    
    newS = "".join(strings)
    
    return newS

# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. 
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
