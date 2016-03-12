#import openpyxl as px
import csv
import sqlite3
#import codecs

datasql = 'Documents/Paladion/datasql.sqlite3'
inputData = 'Documents/Paladion/Logon_Logoff_Events_copy.csv'


conn = sqlite3.connect(datasql)
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Logon_Logoff_Data (
	activityID INTEGER PRIMARY KEY UNIQUE,
    End_Time TEXT,
    Name TEXT,
    Message TEXT,
    Device_Address TEXT,
    Device_Host_Name TEXT,
    Device_Event_Class_ID TEXT,
    Device_Event_Category TEXT,
    Device_Severity TEXT,
    Source_Address TEXT,
    Device_Process_Name TEXT,
    Source_Host_Name TEXT,
    Source_Port TEXT,
    Destination_Address TEXT,
    Destination_Host_Name TEXT,
    Destination_Port TEXT,
    Destination_User_Name TEXT,
    Target_User_ID TEXT,
    Device_Custom_String2 TEXT,
    Device_Custom_String4 TEXT,
    Device_Custom_String5 TEXT
)''')


#Insert full panel data into the table
#W = px.load_workbook(inputData, use_iterators = True)
#p = W.get_sheet_by_name(name = 'Sheet1')

with open(inputData,'rb') as file:
    data = csv.reader(file, delimiter = ',')
    data.next()
    row_num = 0
    for row in data:
        row_num = row_num + 1
        if row_num%1000 == 0:
              print row_num
        #print len(row)      
        final_input = (row_num, str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]),str(row[12]), str(row[13]), str(row[14]), str(row[15]), str(row[16]), str(row[17]), str(row[18]), str(row[19]))
        cur.execute('''INSERT OR REPLACE into Logon_Logoff_Data(activityID, End_Time, Name, Message, Device_Address, Device_Host_Name,
        			   Device_Event_Class_ID, Device_Event_Category, Device_Severity, Source_Address, Device_Process_Name, Source_Host_Name,
        			   Source_Port, Destination_Address, Destination_Host_Name, Destination_Port,
        			   Destination_User_Name, Target_User_ID, Device_Custom_String2, Device_Custom_String4, Device_Custom_String5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', final_input)
       	


conn.commit()

print "Number of full panel rows inserted: ", row_num
