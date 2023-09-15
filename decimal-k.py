#Daniel Moreno

#convert any decimal int to another base
import string
def toBase (value, base):
    #determine digits used and store temporary values
    digits = string.digits + string.ascii_uppercase + string.ascii_lowercase + "+-"
    digitsSlice = digits[0:base]
    tempValue = value
    data = [tempValue]
    #determine values
    while True:
        tempValue = tempValue // base
        data.append(tempValue)
        if tempValue < base:
            break
    #generate result
    result = ""
    for entry in data:
        result += digitsSlice[entry % base]
    result = result[::-1]
    return result

#read the file in and store the lines in a list
fileName = input("baseKaddition ")
#ensure that a file name was provided
if (fileName != ""):
    try:
        dataFile = open(fileName,"r")
        listOfLines = dataFile.readlines()
        #retrieve the number of additions that will be performed
        desiredNumOfIterations = int(listOfLines[0])
        #initialize variables
        currentNumOfIterations = 0
        baseK = 10
        num1 = 0
        num2 = 0
        while (currentNumOfIterations < desiredNumOfIterations):
            baseK = int(listOfLines[1 + (currentNumOfIterations*3)])
            num1Str = (listOfLines[2 + (currentNumOfIterations*3)])
            num1Str = num1Str.strip()
            num2Str = (listOfLines[3 + (currentNumOfIterations*3)])
            num2Str = num2Str.strip()
            num1 = int(num1Str, baseK)
            num2 = int(num2Str, baseK)
            sum = num1 + num2
            print ("The base of the numbers to add is " + str (baseK))
            print ("The first number is " + num1Str)
            print ("The second number is " + num2Str)
            print ("The sum is: " + str(sum))
            print ("The sum is: " + toBase(sum,baseK))
            print("")
            print("")
            currentNumOfIterations += 1
    except:
        print("The file " + fileName + " was not found.")
else:
    print("Please enter the name of the text file to use on the command line.")