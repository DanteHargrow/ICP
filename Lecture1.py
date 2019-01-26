#Dante Hargrow

"""
Question 1
Differences: Text strings are stored in unicode by default
Print statement has been replaced with print function
python 2 you can format strings with %, python 3 has a format function
"""

"""
Question 2
Takes in numbers and reverses them
"""
num = int(input("Enter three digits"))

reversenum=0

while(num > 0):
    remain= num % 10
    reversenum = (reversenum * 10) + remain
    num = num // 10

print("The reverse number is {0} \n".format(reversenum))


number1 = int(input("Enter your first number"))
number2 = int(input("Enter your second number"))



addition =  number1 + number2
subtraction = number2 - number1
multi = number2 * number1
divide = number2 / number1
exponent = number2 ** number1

print("""Addition: {0}
Subtraction: {1}
Multiplication: {2}
Division: {3}
Exponent: {4}
""".format(addition,subtraction,multi,divide,exponent))


"""
Question 3
Takes in a string and keeps track of amount of digits, letters, and words. By looping through the string and if the iterator is a 
digit then it adds one to digit and if it's an letter it adds one to letter. I track amount of words by the amount of 
blank spaces. With words counter initialized as one
"""
letters = 0
digits = 0
words = 1

usrInput = input("Enter a string ")

for i in usrInput:
    if(i.isdigit()):
        digits +=1
    if(i.isalpha()):
        letters += 1
    if(i == " "):
        words +=1


print("""Letters: {0}
Digits: {1}
Words: {2}""".format(letters,digits,words))





