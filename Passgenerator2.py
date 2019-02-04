import random as ran
print ("This program generates random passwords")
uppercase1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase1 = ["a", "b", "c ", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
specialchar1 = ["!", "\"", "£", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", ",", ".", "'", "?", "#", "@", "~", ":", ";"]
loop = 1
while loop == 1:
    password = []
    finalpassword = []
    length = int(input("\nHow long do you want the password to be?   "))
    uppercase = int(input("\nDo you want uppercase letters? (1 = true, 0 = false)   "))
    if uppercase == 1:
        password.extend(uppercase1)
    lowercase= int(input("\nDo you want lowercase letters? (1 = true, 0 = false)   "))
    if lowercase == 1:
        password.extend(lowercase1)
    numbers= int(input("\nDo you want numbers? (1 = true, 0 = false)   "))
    if numbers == 1:
        password.extend(numbers1)
    specialchar= int(input("\nDo you want special characters? (1 = true, 0 = false)   "))
    if specialchar == 1:
        password.extend(specialchar1)
    if uppercase == 0 and lowercase == 0 and numbers == 0 and specialchar == 0:
        print ("\nError - no character type selected")
        continue
    for i in range(length):
        letter = ran.choice(password)
        finalpassword.extend(letter)
    joinedpassword = "".join(finalpassword)
    print ("")
    print (joinedpassword, "is your password")
        
        
    
