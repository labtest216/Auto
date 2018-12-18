import smtplib, socket, time, os, signal, json, sys
import traceback
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import inspect
import re


# Send mail.

def send_mail(sender_addr, sender_pass, notification_addr, subject, body, attach_file):
    toaddr = [elem.strip().split(',') for elem in notification_addr]
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = 'rigautolog@gmail.com'
    msg['Reply-to'] = 'rigautolog@gmail.com'
    msg.preamble = 'Multipart massage.\n'
    part = MIMEText(body)
    msg.attach(part)
    part = MIMEApplication(open(attach_file, "rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=attach_file)
    msg.attach(part)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(sender_addr, sender_pass)
    server.sendmail(msg['From'], toaddr, msg.as_string())
    dprint('Send notification mail')
    server.quit()


# Debug printer.
def dprint(data_to_print: object) -> object:
    # os.system('echo ' + str(time()) + ' ' + str(data_to_print))
    print(str(time.time()) + " " + str(datetime.now()) + " " + data_to_print)


# Get function name.
def f_name():
    stack=traceback.extract_stack()
    filename, codeline, funcName, text = stack[-2]
    return funcName


# Test net connection.
def connected():
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname("www.google.com")
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        dprint('Test internet connection: PASS.')
        return True
    except:
        pass
        dprint('Test internet connection: FAIL.')
    return False


# Kill process.
def kill_proc(pid):
    dprint('Kill process '+str(pid))
    os.signal(pid, signal.SIGTERM)


# Get/Set data from json config file.
def config_file( file_name, key, value):
    json_file = open(str(file_name), "r+")
    data = json.load(json_file)
    try:
        if value == 'get':  # Get value.
            return str(data[str(key)])
        else:  # Set value.
            data[str(key)] = str(value)
            json_file.seek(0)  # rewind
            json.dump(data, json_file, sort_keys=True, indent=4)
            json_file.truncate()
    except:
        dprint("Can not set/get value on " + str(file_name) + " file.")

# print variable name myVar = print_var_name("myVar", 15)-->myVar=15.
def echo(arg):
    frame = inspect.currentframe()
    try:
        context = inspect.getframeinfo(frame.f_back).code_context
        caller_lines = ''.join([line.strip() for line in context])
        m = re.search(r'echo\s*\((.+?)\)$', caller_lines)
        if m:
            caller_lines = m.group(1)
        print(caller_lines, arg)
    finally:
        del frame


# Create object on run time by reflection (class name = "import_file.class_name".
def get_class(class_name):
    parts = class_name.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m
