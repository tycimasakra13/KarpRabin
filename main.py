import time
import unittest
from subprocess import Popen, PIPE, STDOUT

def rk_algorithm(patternStr, searchStr, charCount, maxPrime):
    x = []
    h = 1

    patternHash = 0
    stringHash = 0
    patternLength = len(patternStr)
    stringLength = len(searchStr)
    for i in range(patternLength-1):
        h = (h * charCount) % maxPrime #basic hash function with modulo

    print("HASH: ", h)

    for i in range(patternLength):
        #x=t[i]b^(M-1)+t[i+1]b^(M-2)+...+t[i+M-1]
        patternHash = (patternHash * charCount + ord(patternStr[i])) % maxPrime #calculate hash value for pattern
        stringHash = (stringHash * charCount + ord(searchStr[i])) % maxPrime #calculate hash value for text

    for i in range(stringLength - patternLength +1): #find pattern in text
        if patternHash == stringHash: #if hash values are equal
            for j in range(patternLength):
                if searchStr[i + j] != patternStr[j]: #compare char by char
                    break #chars in pattern don't match

            j += 1
            if j == patternLength:
                x.append(i)

        if i < (stringLength - patternLength):
            #x'=(x-t[i]b^(M-1))+t[i+M]
            stringHash = (charCount*(stringHash - ord(searchStr[i])*h) + ord(searchStr[i+patternLength])) % maxPrime #calculate new text hash value
        if stringHash < 0:
            stringHash = stringHash + maxPrime
            if stringHash < 0:
                stringHash = stringHash + charCount
    print(len(x))
    if len(x) > 0:
        print('Pattern find at index: ' + str(x))
    else:
        print('Pattern not found')
    return x


validate = True
caseSensitive = input('Case sensitive? yes/no ')
patternStr = input("Provide pattern: ")
searchStr = input("Provide search string: ")

if caseSensitive.lower() == 'yes':
    caseSensitive = True
elif caseSensitive.lower() == 'no':
    caseSensitive = False
else:
    print('Wrong input value for case sensitive')
    validate = False

if searchStr == "":
    print('String could not be null')
    validate = False
if len(searchStr) < len(patternStr):
    print('String should be longer than search pattern')
    validate = False
if patternStr == "":
    patternStr = searchStr

if validate:
    charCount = 64
    maxPrime = 999999
    machinePerformance = 0

    if not caseSensitive:
        patternStr = patternStr.lower()
        searchStr = searchStr.lower()

    print(patternStr)
    print(searchStr)

    start = time.perf_counter()
    rk_algorithm(patternStr, searchStr, charCount, maxPrime)
    stop = time.perf_counter() - start

    num_digits = 20

    formatted_stop = '{:.{}f}'.format(stop, num_digits)
    print(formatted_stop + ' (' + str(stop) + ')' + " seconds")

    checkMachinePerformance = input('Compare machine performance? yes/no ')
    if checkMachinePerformance.lower() == 'yes':
        p = Popen(['java', '-jar', './FactorialPerformance.jar'], stdout=PIPE, stderr=STDOUT)
        for line in p.stdout:
            machinePerformance = line.decode().strip()

        print("mp: " + str(machinePerformance))

        scriptPerformance = stop / int(machinePerformance)
        formatted_performance = '{:.{}f}'.format(scriptPerformance, num_digits)
        print('script performance is: ' + formatted_performance + ' (' + str(scriptPerformance) + ')')
else:
    print('Search nor started...')