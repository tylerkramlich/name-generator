import random
import time

MALE_FILE_NAME_PATH = "../resources/male-first-names.txt"
FEMALE_FILE_NAME_PATH = "../resources/female-first-names.txt"
LAST_NAME_FILE_NAME_PATH = "../resources/last-names.txt"
OUTPUT_FILE_NAME = "../requested_names.txt"

def grabRandomLine(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num): continue
        line = aline
        line = line.strip('\n')
    return line

def generateFirstName(gender):
    if (gender == 0):
        afile = open(MALE_FILE_NAME_PATH)
    else:
        afile = open(FEMALE_FILE_NAME_PATH)

    firstName = grabRandomLine(afile)
    afile.close()

    return firstName

def generateLastName():
    afile = open(LAST_NAME_FILE_NAME_PATH)

    lastName = grabRandomLine(afile)
    afile.close()
    
    return lastName

def generateFullName(gender): 
    firstName = generateFirstName(gender)
    lastName = generateLastName()

    spaceStyle = " "

    return firstName + spaceStyle + lastName

def outputStandardListOfFirstNames(length):
    afile = open(OUTPUT_FILE_NAME, "w")

    print('Processing...')

    start = time.process_time()
    for _ in range(length):
        gender = random.randint(0, 1)
        afile.write(generateFirstName(gender) + '\n')
    end = time.process_time()

    print('Process complete in {} seconds. Check output file for results.'.format(end-start))

    afile.close()

def outputStandardListOfLastNames(length):
    afile = open(OUTPUT_FILE_NAME, "w")

    print('Processing...')

    start = time.process_time()
    for _ in range(length):
        afile.write(generateLastName() + '\n')
    end = time.process_time()

    print('Process complete in {} seconds. Check output file for results.'.format(end-start))

    afile.close()

def outputStandardListOfFullNames(length):
    afile = open(OUTPUT_FILE_NAME, "w")

    print('Processing...')

    start = time.process_time()
    for _ in range(length):
        gender = random.randint(0, 1)
        afile.write(generateFullName(gender) + '\n')
    end = time.process_time()
    
    print('Process complete in {} seconds. Check output file for results.'.format(end-start))

    afile.close()

def outputArrayOfFirstNames(length):
    afile = open(OUTPUT_FILE_NAME, "w")

    print('Processing...')

    start = time.process_time()
    for _ in range(length):
        num = random.randint(0,1)
        if (_ == 0):
            afile.write("{"+"\'{}\',".format(generateFirstName(num)))
        elif (_ == length-1):
            afile.write("\'{}\'".format(generateFirstName(num)) + "}")
        else:
            afile.write("\'{}\',".format(generateFirstName(num)))
    end = time.process_time()

    print('Process complete in {} seconds. Check output file for results.'.format(end-start))

    afile.close()

def outputArrayOfLastNames(length):
    afile = open(OUTPUT_FILE_NAME, "w")

    print('Processing...')

    start = time.process_time()
    for _ in range(length):
        if (_ == 0):
            afile.write("{"+"\'{}\',".format(generateLastName()))
        elif (_ == length-1):
            afile.write("\'{}\'".format(generateLastName()) + "}")
        else:
            afile.write("\'{}\',".format(generateLastName()))
    end = time.process_time()

    print('Process complete in {} seconds. Check output file for results.'.format(end-start))

    afile.close()

def outputArrayOfFullNames(length):
    afile = open(OUTPUT_FILE_NAME, "w")

    print("Processing...")

    start = time.process_time()
    for _ in range(length):
        num = random.randint(0,1)
        if (_ == 0):
            afile.write("{"+"\'{}\',".format(generateFullName(num)))
        elif (_ == length-1):
            afile.write("\'{}\'".format(generateFullName(num)) + "}")
        else:
            afile.write("\'{}\',".format(generateFullName(num)))
    end = time.process_time()

    print('Process complete in {} seconds. Check output file for results.'.format(end-start))

    afile.close()
