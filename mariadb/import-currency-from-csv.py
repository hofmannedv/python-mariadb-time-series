import csv, sys, datetime,re

def cleanValue (value, valueType):
    cleanedValue = value

    if valueType == "timestamp":
        if isDate(value):
            timestamp = datetime.datetime.strptime(value, "%d/%m/%Y")
            cleanedValue = timestamp.strftime("%Y-%m-%d")
        #else:
        #   # print("Error. Given value is not a date: %s" % value)

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

def insertEURGBP(timestamp, value):

    sqlStatement = "INSERT INTO exchangegbp (timestamp, value) VALUES ('%s',%s);" % (timestamp, value);
    return sqlStatement

def insertEURUSD(timestamp, value):

    sqlStatement = "INSERT INTO exchangeusd (timestamp, value) VALUES ('%s',%s);" % (timestamp, value);
    return sqlStatement

# csvFile = "spot-data-1.csv"
csvFile = sys.argv[1]

with open(csvFile) as fileId:
    currentLine = 1
    try:
        # read csv file
        reader = csv.reader(fileId)

        # define previous value: 0.0
        previousValueGBP = 0.0
        previousValueUSD = 0.0

        for row in reader:
            if currentLine > 5:
                # transform date value into database date format
                entryDate = cleanValue(row[0], "timestamp")

                # check for the last line: Average
                if isAverage(row[0]):
                    break

                sortValues = row[1:]
                includedColumns = [91,92]
                currentColumn = 1
                for value in sortValues:

                    if currentColumn in includedColumns:
                        if currentColumn == 91:
                            # if current value is empty, take the previous one
                            if not value:
                                value = previousValueGBP
                            else:
                                previousValueGBP = value
                            sqlStatement = insertEURGBP(entryDate, value)
                        if currentColumn == 92:
                            # if current value is empty, take the previous one
                            if not value:
                                value = previousValueUSD
                            else:
                                previousValueUSD = value
                            sqlStatement = insertEURUSD(entryDate, value)
                        print(sqlStatement)

                    currentColumn += 1
            currentLine += 1
            #if currentLine > 6:
            #    sys.exit(0)
    except csv.Error as e:
        sys.exit("Error reading the csv file", 1)
