import datetime
import getpass
import re


def convertXero(xeroInput):
   # Extract info from input
    sortCode = xeroInput[:6]
    accountNumber = xeroInput[6:14]
    salary = (f"{xeroInput[41:44]}.{xeroInput[44:46]}")
    if(salary == "000.00"):
        salary = "0.00"
    if(salary.startswith('0') and salary[1].isdigit and salary[1]!="."):
        salary= salary.lstrip('0')
    type = xeroInput[64:70]
    payeeName = xeroInput[82:].rstrip()
    reason = "SALARY"

    print(accountNumber,sortCode,salary,payeeName,reason)

    # Check if all required information is found
    if sortCode and accountNumber and salary and payeeName and reason and salary!= "0.00" and type=="PAIDOK":
        # Creating Santander output
        output = ''
        for i in range(1,86):
            if(i!=4 and i!= 16 and i!=17 and i!=25 and i!=31 and i!=33 and i!=37):
                print(i,output)
                output = output + ','
            if(i==4):
                output = output + "09,"
            if(i==16):
                output = output + "GBP,"
            if(i==17):
                output = output + salary + ","
            if(i==25):
                output = output + sortCode + ","
            if(i==31):
                output = output + accountNumber + ","
            if(i==33):
                output = output + payeeName + ","
            if(i==37):
                output = output + reason
            i = i + 1
        return output
    return ""

# save converted file with current date in the name
def saveConverted():
    currentDate = datetime.datetime.now()
    date = datetime.datetime.strftime(currentDate, '%d%m%Y')
    path = 'C:\\Users\\' + getpass.getuser() + '\\Downloads\\import' + date + '.txt'
    

