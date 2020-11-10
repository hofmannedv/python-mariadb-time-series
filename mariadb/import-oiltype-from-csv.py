import csv, sys, datetime,re

def isEmptyColumn(grade, market, publisher,instrument):
    result = False
    patternEmpty = re.compile("^\s*$")
    if re.match(patternEmpty, grade):
        result = True
    return result

def isCurrencyColumn(grade):
    result = False
    patternCurrency = re.compile("^EUR/.+$")
    if re.match(patternCurrency, grade):
        result = True
    return result

def insert(sortid, grade, market, publisher, instrument):

    sqlStatement = "INSERT INTO oilsort (id, grade, market, publisher, instrument) VALUES (%i, '%s','%s','%s', '%s');" % (sortid, grade, market, publisher, instrument);
    return sqlStatement

# csvFile = "spot-data-1.csv"
csvFile = sys.argv[1]

with open(csvFile) as fileId:
    currentLine = 1
    try:
        currentLine = 1
        reader = csv.reader(fileId)
        for row in reader:
            if currentLine == 1:
                # read grade line
                gradeData = row[1:]
            if currentLine == 2:
                # read market line
                marketData = row[1:]
            if currentLine == 3:
                # read publisher line
                publisherData = row[1:]
            if currentLine == 4:
                # read instrument line
                instrumentData = row[1:]
            if currentLine > 4:
                # analyze previously read data

                for currentColumn in range(len(gradeData)):
                    grade = gradeData[currentColumn]
                    market = marketData[currentColumn]
                    publisher = publisherData[currentColumn]
                    instrument = instrumentData[currentColumn]

                    # exclude empty columns
                    if isEmptyColumn(grade, market, publisher, instrument):
                        # print("empty column")
                        continue
                    
                    # exclude currency columns
                    if isCurrencyColumn(grade):
                        # print("currency column")
                        continue

                    sqlStatement = insert(currentColumn + 1, grade, market, publisher, instrument)
                    print(sqlStatement)
                # quit
                sys.exit(0)
            # read the next line    
            currentLine += 1
    except csv.Error as e:
        sys.exit("Error reading the csv file", 1)
