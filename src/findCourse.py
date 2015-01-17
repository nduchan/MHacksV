import csv



def GenerateDeptList():
    deptList = []
    
    with open('static/csv/WN2015.csv', 'r') as classFile:
        classDict = csv.DictReader(classFile)
        for row in classDict:
            if not (row['Subject'] in deptList):
                deptList.append(row['Subject'])
    
    deptList.sort()
    for entry in deptList:
        print("<option value=\"" + entry[entry.find("(") + 1:entry.find(")")] + "\">" + entry + "</option>")
            
            
GenerateDeptList()