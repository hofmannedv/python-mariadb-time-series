import sys, os
import MySQLdb

def executeSQL(sqlCommandList):

    try:
        connector = MySQLdb.connect(
            user="oil",
            password="oil",
            host="localhost",
            port=3306,
            database="oilmarket"
        )
    except MySQLdb.error as e:
        print(f"Error connecting to database: {e}")
        return False

    cursor = connector.cursor()
    for sqlCommand in sqlCommandList:
        # print(sqlCommand)
        try:
            cursor.execute(sqlCommand)
        except MySQLdb.Error as e:
            print(f"Error: {e}")
            print(sqlCommand)

    connector.commit()
    connector.close()
    return True

# read command-line option for file with SQL commands to be executed
parameters = len(sys.argv) - 1
if parameters < 1:
    print("Invalid number of parameters: no SQL files given")
    sys.exit(0)

sqlFiles = sys.argv[1:]
for currentFile in sqlFiles:
    print("File to be processed: %s" % currentFile)
    if not os.path.exists(currentFile):
        print("File not found: %s . Skipping file." % currentFile)
        continue

    try:
        filehandle = open(currentFile, "r")
        sqlCommandList = filehandle.readlines()
        filehandle.close()

        result = executeSQL(sqlCommandList)
        if result:
            print("Execution of SQL commands successful")
        else:
            print("Execution of SQL commands failed")
    except:
        print("Error reading from file: %s" % currentFile)
        continue

