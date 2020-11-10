import csv, sys, datetime,re

def cleanValue (value, valueType):
    cleanedValue = value

    if valueType == "timestamp":
        if isDate(value):
            timestamp = datetime.datetime.strptime(value, "%d/%m/%Y")
            cleanedValue = timestamp.strftime("%Y-%m-%d")
        #else:
        #    print("Error. Given value is not a date: %s" % value)


    if valueType == "marketdata":
        # test for spaces
        patternSpace = re.compile("^\s+$")
        if re.match(patternSpace, value):
            return ""

        # test for negative values in brackets
        patternNegativeValue = re.compile("^\(\d+\.\d+\)$")
        if re.match(patternNegativeValue, value):
            return "-" + value[1:-1]

        # test for digits
        patternDigits = re.compile("^\d+\.\d+")
        if not re.match(patternDigits, value):
            cleanedValue = ""

    return cleanedValue

def isAverage(value):
    result = False
    patternAverage = re.compile("^Average$")
    if re.match(patternAverage, value):
        return True
    return result

def isDate(value):
    result = False
    patternDate = re.compile("^\d{1,2}/\d{1,2}/\d{4}$")
    if re.match(patternDate, value):
        result = True
    return result

def insert(timestamp, sortId, closeValue):

    sqlStatement = "INSERT INTO marketdata (date, sortid, close) VALUES ('%s',%s,%s);" % (timestamp, sortId, closeValue);
    return sqlStatement

# csvFile = "spot-data-1.csv"
csvFile = sys.argv[1]

with open(csvFile) as fileId:
    currentLine = 1
    try:
        # read csv file
        reader = csv.reader(fileId)

        # define previous values: 0.0
        previousValues = [0.0] * 250

        for row in reader:
            if currentLine > 5:
                # transform date value into database timestamp format
                entryDate = cleanValue(row[0], "timestamp")

                # check for the last line: Average
                if isAverage(row[0]):
                    break

                sortValues = row[1:]
                excludedColumns = [91,92,93,94,95,96,132]
                currentColumn = 1
                for value in sortValues:
                    if currentColumn not in excludedColumns:
                        # transform value into correct data format
                        cleanedValue = cleanValue(value, "marketdata")

                        # if current value is empty, take the previous one
                        if not cleanedValue:
                            cleanedValue = previousValues[currentColumn]
                        else:
                            previousValues[currentColumn] = cleanedValue

                        sqlStatement = insert(entryDate, currentColumn, cleanedValue)
                        print(sqlStatement)
                    currentColumn += 1
            currentLine += 1
            #if currentLine > 6:
            #    sys.exit(0)
    except csv.Error as e:
        sys.exit("Error reading the csv file", 1)
