'''
This is the NMBON Module used as a boiler plate for NMBON development.
'''
# Permit generic error handeling from Pylint
# pylint: disable=W0703

import os
import csv
import json
import random
import glob
import sys
from datetime import date
from bs4 import BeautifulSoup
from exchangelib import Credentials, Account, HTMLBody, Message, Mailbox, FileAttachment
import extract_msg

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

def file_to_binary(location, file_name):
    '''
    File to -> Python String binary
    '''
    with open(location + file_name, "rb") as input_file:
        return input_file.read()

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
    return 'abc' + password + '@NMBON'

def msg_body_to_string(location, file_name):
    '''
    .MSG file -> Python String
    Dump the body of the email into a string
    '''
    return extract_msg.Message(location + file_name).body

def msg_html_body_to_string(location, file_name):
    '''
    .MSG file -> Python String
    Dump the HTML body of the email into a string
    '''
    return extract_msg.Message(location + file_name).htmlBody

def msg_body_to_list(location, file_name):
    '''
    .MSG file -> Python List
    Add Sender, Date, Subject, Body, HTML_Body to a List
    '''
    msg = extract_msg.Message(location + file_name)
    output_list = list()
    output_list.append(msg.sender)
    output_list.append(msg.date)
    output_list.append(msg.subject)
    output_list.append(msg.body)
    output_list.append(msg.htmlBody)
    return output_list

def glob_to_list(search):
    '''
    OS file(s) -> Python List
    Return all matching criteria in list form
    EXAMPLE: '*.py'
    '''
    return glob.glob(search)

def ews_connect(email, password):
    '''
    Email credentials -> EWS Account Obj
    Authenticate with the Exchange server for reading / sending emails
    '''
    try:
        credentials = Credentials(email, password)
        return Account(email, credentials=credentials, autodiscover=True)
    except Exception as error_text:
        print(f'[Error] Unable to connect to email server - {str(error_text)}')
        sys.exit()

def ews_read_folder(ews_account, subfolder=''):
    '''
    EWS Account Obj -> Python List of EWS Emails
    '''
    try:
        location = ews_account.inbox
        if subfolder != '':
            location = ews_account.inbox / subfolder
        return location.all().order_by('-datetime_received')
    except Exception as error_text:
        print(f'[Error] Unable to read email folder - {str(error_text)}')
        sys.exit()

def ews_read_emails(list_of_emails):
    '''
    Python List of EWS Emails -> Python List of email bodies
    Converts each email from Obj to String
    '''
    output = list()
    for email in list_of_emails:
        output.append(str(HTMLBody(email.body)))
    return output

def remove_html(html_string):
    '''
    HTML String -> String
    Removes all html and returns a clean string
    '''
    return BeautifulSoup(html_string, 'lxml').get_text()

def ews_delete_emails_from_folder(ews_account, subfolder=''):
    '''
    Delete all the emails in a EWS folder
    '''
    try:
        location = ews_account.inbox
        if subfolder != '':
            location = ews_account.inbox / subfolder
        location.all().delete()
    except Exception as error_text:
        print(f'[Error] Unable to delete emails from folder - {str(error_text)}')
        sys.exit()

def ews_toggle_is_read(ews_account, subfolder='', isread=False):
    '''
    Mark as all emails in EWS folder as Read/Unread
    '''
    try:
        location = ews_account.inbox
        if subfolder != '':
            location = ews_account.inbox / subfolder
        for email in location.all().order_by('-datetime_received'):
            email.is_read = isread
            email.save(update_fields=['is_read'])
    except Exception as error_text:
        print(f'[Error] Unable to mark emails as read - {str(error_text)}')
        sys.exit()

def ews_send_email(ews_account, subject, body, recipient, attachments=None):
    '''
    Email -> Recipient
    Attachments are python dictionary {FileName : FileContent}
    Moves the sent email into the 'Outbound' folder
    '''
    try:
        # Setup empty dict
        if attachments is None:
            attachments = []

        # Prep email message
        email_draft = Message(
            account=ews_account,
            folder=ews_account.inbox / 'Outbound',
            subject=subject,
            body=body,
            to_recipients=[Mailbox(email_address=recipient)]
        )

        for dict_key in attachments:
            attachment = FileAttachment(name=dict_key, content=attachments[dict_key])
            email_draft.attach(attachment)

        # Send the Email
        email_draft.send_and_save()
        # Mark the sent email as unread
        ews_toggle_is_read(ews_account, 'Outbound')
    except Exception as error_text:
        print(f'[Error] Unable to send email - {str(error_text)}')
        sys.exit()

def files_from_folder(location, search):
    '''
    Glob -> Python List
    Returns all filenames from a glob
    '''
    files = list()
    for file in glob_to_list(location + search):
        files.append(os.path.basename(file))
    return files

def files_into_dict(location, files):
    '''
    Folder/Files -> dict[filename]Content
    '''
    output = dict()
    for file in files:
        output[file] = file_to_binary(location, file)
    return output
