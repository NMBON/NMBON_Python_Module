'''
This is the NMBON Module used as a boiler plate for NMBON development.
'''
#import os
import csv
import json
import random
from datetime import date
import pyperclip

def date_to_string():
    '''
    Returns date as 'MM.DD.YYYY' string
    '''
    todays_date = date.today() # Get todays date
    # Setup each date section with leading zeros
    day = str(todays_date.day).zfill(2)
    month = str(todays_date.month).zfill(2)
    year = str(todays_date.year).zfill(4)
    return f'{month}.{day}.{year}'

def list_to_csv(location, file_name, content):
    '''
    Python List -> .CSV
    '''
    with open(location + file_name + ' ' + date_to_string() + '.csv',
              'w', newline='') as output_file:
        csv_out = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for csv_row in content:
            csv_out.writerow(csv_row)

def csv_to_list(location, file_name):
    '''
    .CSV -> Python List
    '''
    with open(location + file_name, encoding="utf-8-sig", newline='') as csv_file:
        csv_return = list()
        csv_in = csv.reader(csv_file, delimiter=',', quotechar='"', skipinitialspace=True)
        for row in csv_in:
            csv_return.append(row)
        return csv_return

def string_to_file(location, file_name, file_content):
    '''
    Python String -> to File
    '''
    with open(location + file_name, "w", encoding="utf-8-sig") as output_file:
        output_file.write(file_content)

def list_to_file(location, file_name, file_content):
    '''
    Python List -> to File
    Recieves a one dementional list and adds a newline to each row.
    '''
    with open(location + file_name, "w", encoding="utf-8-sig") as output_file:
        for row in file_content:
            output_file.write(row + '\n')

def file_to_string(location, file_name):
    '''
    File to -> Python String
    '''
    with open(location + file_name, "r", encoding="utf-8-sig") as input_file:
        return str(input_file.read())

def file_to_list(location, file_name):
    '''
    File to -> Python List
    Strips out newline characters for each line
    '''
    with open(location + file_name, "r", encoding="utf-8-sig") as input_file:
        return [line.rstrip() for line in input_file]

def json_to_list(location, file_name):
    '''
    JSON File -> Python List of dict
    '''
    with open(location + file_name, 'r', encoding="utf-8-sig", newline='') as infile:
        return json.loads(infile.read())

def json_to_csv(location, file_name, file_content):
    '''
    JSON List of dict -> .CSV file
    '''
    # Determine all the keys present, which will each become csv fields
    header_content = list(set(key for row in file_content for key in row))
    with open(location + file_name + ' ' + date_to_string() + '.csv',
              'w', encoding="utf-8-sig", newline='') as output_file:
        csv_out = csv.DictWriter(output_file, header_content) # Write the header row
        csv_out.writeheader()
        csv_out.writerows(row for row in file_content) # Write the CSV content

def generate_password(num_of_digits=8):
    '''
    Use this method to generate temp passwords for Users & Guest WIFI
    Default length is eight digits with '@NMBON' appended
    The passwords generated will not have simular charecters: i, l, 1, L, o, 0
    '''
    password = ''
    for _each in range(num_of_digits):
        password += str(random.randint(2, 9))
    password = password + '@NMBON'
    # Handle note being able to copy paste in repl.it
    try:
        pyperclip.copy(password) 
    finally:
        return password
