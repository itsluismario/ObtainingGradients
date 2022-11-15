# Read Text Files with Pandas using read_csv()
import os
import glob

# import xlsxwriter module
import xlsxwriter

#  Find txt files
txtFilenamesList = glob.glob('**_QCReport.txt')

# Get the current Path
cwd = os.getcwd() 

# Define global var
dict = {}

def CreateDict(txtFilenamesList):
    for txtFile in txtFilenamesList:
        txtPath = os.path.join(cwd,txtFile)

        # String to search in file
        word = 'Included Gradients:'
        with open(txtPath, 'r') as fp:
            # Create list
            list = []
            # Read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # Check if string present on a current line
                if line.find(word) != -1:
                    x = line.split()
                    list.append(x[2])
            dict[txtFile] = list.pop()
    return dict

def CreateSpreadSheet(dict):
    # Workbook() takes one, non-optional, argument
    # which is the filename that we want to create.
    workbook = xlsxwriter.Workbook('gradients.xlsx')
    
    # The workbook object is then used to add new
    # worksheet via the add_worksheet() method.
    worksheet = workbook.add_worksheet()
    
    # Use the worksheet object to write
    # data via the write() method.
    i = 1
    for key, value in dict.items():
        
        worksheet.write('A'+str(i), key)
        worksheet.write('B'+str(i), value)
        i = i + 1
    # Finally, close the Excel file
    # via the close() method.
    workbook.close()
    return 

CreateDict(txtFilenamesList)
CreateSpreadSheet(dict)
