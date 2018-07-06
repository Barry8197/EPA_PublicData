import requests
import zipfile
import io
import os
import csv
import pandas as pd
import numpy as np
import xlrd
import unicodecsv
import warnings
from Constants import Years_eia860, eia860_url, Years_eia923, eia923_url


def eia860():
    file_name = "Automated_Output.txt"
    output = open(file_name, 'a')
    output.write("Beginning eia860 imports from years 1990+\n")
    warnings.warn("deprecated", DeprecationWarning)
    path = os.getcwd()
    output.write("Fetching data for years...\n")
    output.close()
    for item in Years_eia860:
        output = open(file_name, 'a')
        output.write("%s\n" % (item))
        os.mkdir(item)
        os.chdir("%s/%s" % (path,item))
        if item[0] == 'a':
            url = ("%seia860a/eia860%s.zip" % (eia860_url, item))
        elif item[0] == 'b':
            url = ("%seia860b/eia860%s.zip" % (eia860_url, item))
        else:
            url = ("%sxls/eia860%s.zip" % (eia860_url, item))
            
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()
        
        test = os.listdir()
        for data in test:
            r = csv.reader(open(data))
            if data.endswith(".xlsx") :
                csv_name = data.replace(".xlsx" , ".csv")
                xls2csv(data,csv_name)
            elif data.endswith(".xls") :
                csv_name = data.replace(".xls" , ".csv")
                xls2csv(data,csv_name)
                
            
        database = os.listdir()
        for table in database:
            if table.endswith(".csv"):
                table_create(table,item,'eia860')
                
        output.close()
        os.chdir(path)
        
def eia923():
    file_name = "Automated_Output.txt"
    output = open(file_name, 'a')
    output.write("Beginning eia923 imports from years 1970+\n")
    warnings.warn("deprecated", DeprecationWarning)
    path = os.getcwd()
    output.write("Fetching data for years...\n")
    output.close()
    for item in Years_eia923:
        output = open(file_name, 'a')
        output.write("%s\n" % (item))
        os.mkdir(item)
        os.chdir("%s/%s" % (path,item))
        if item in Years_eia923[:2]:
            url = ("%sxls/f923_%s.zip" % (eia923_url, item))
        elif item in Years_eia923[2:11]:
            url = ("%sarchive/xls/f923_%s.zip" % (eia923_url, item))
        elif item in Years_eia923[11:18]:
            url = ("%sarchive/xls/f906920_%s.zip" % (eia923_url, item))
        else :
            url = ("%sarchive/xls/utility/f759%s.xls" % (eia923_url, item))
        r = requests.get(url)
        if url.endswith(".zip"):
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall()
        else :
            output = open('f759%s.xls' % (item), 'wb')
            output.write(r.content)
            output.close()
        
        test = os.listdir()
        for data in test:
            r = csv.reader(open(data))
            if data.endswith(".xlsx") :
                csv_name = data.replace(".xlsx" , ".csv")
                xls2csv(data,csv_name)
            elif data.endswith(".xls") :
                csv_name = data.replace(".xls" , ".csv")
                xls2csv(data,csv_name)
                
            
        database = os.listdir()
        for table in database:
            if table.endswith(".csv"):
                table_create(table,item,'eia923')
                
        output.close()
        os.chdir(path)
                
def xls2csv (xls_filename, csv_filename):
    # Converts an Excel file to a CSV file.
    # If the excel file has multiple worksheets, only the first worksheet is converted.
    # Uses unicodecsv, so it will handle Unicode characters.
    # Uses a recent version of xlrd, so it should handle old .xls and new .xlsx equally well.

    wb = xlrd.open_workbook(xls_filename)
    sheet_names = wb.sheet_names()
    length = len(sheet_names)
    for i in range(0,length):
    
        sh = wb.sheet_by_index(i)

        if length == 1 :
            fh = open(csv_filename,"wb")
        else :
            temp_filename = csv_filename.replace(".csv","Sheet%i.csv" % (i+1))
            fh = open(temp_filename,"wb")
            
        csv_out = unicodecsv.writer(fh, encoding='utf-8')

        for row_number in range(sh.nrows):
            csv_out.writerow(sh.row_values(row_number))

        fh.close()
    os.remove(xls_filename)
    
def table_create(table,item,dB):
    from os.path import expanduser
    dp = pd.read_csv(table,header=None)
    start = header(dp)
    df = pd.read_csv(table, header = start)
    df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces


    from sqlalchemy import create_engine
    with open(expanduser('~/.pgpass'), 'r') as f:
        port,nothing, nothing, user, password = f.read().split(':')
    engine = create_engine('postgresql://%s:%s@%s/%s' % (user, password[:-1], port, dB),paramstyle="format")


    rename = naming(table)
    title = no_repeat(rename,item)
    df.to_sql(title, engine )
    
def header(kwargs):
    array = np.array(kwargs)
    count = 0
    for i in range(len(array)-1):
        i +=1
        if [type(array[i][0]),type(array[i][-1])] == [type(array[i-1][0]),(type(array[i-1][-1]))]:
            break
        else:
            count +=1

    header = count
    return header

def naming(item):
    if len(item) >= 63:
        item = item[:18] + item[-25:]
    for i in item:
        if i.isnumeric():
            item = item.lstrip(i + "__" + "_")
        elif i == ' ' :
            item = item.replace(i, "_")
 
    return item 

def no_repeat(item,year) :
    check1 = False
    for i in range(len(item)-4):
        check = item[i] + item[i+1] + item[i+2] + item[i+3]
        if check.isnumeric():
            check1 = True

    if check1 == False:
        year = "_" + year[-2] + year[-1]
        item = item.replace('.csv',year)
    if item.endswith('.csv'):
        item = item[:-4]
    
    return item


