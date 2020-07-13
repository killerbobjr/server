import sys
sys.path.append('../build_tools/scripts')
import sys
import os
import base
import subprocess
import requests
import zipfile
import shutil
import platform

def initialization_system():#Определение системы
    s = sys.platform
    s = s[0:-2]
    return s

def initialization_system_capacity():#Определение разрядность системы
    return "64"

def number_version_nodejs():#возврашает необходимую версию программы Nodejs
    return "v10.21.0"

def number_version_nodejs():#Определяет установлен или нет Nodejs, если установлен возврашает установленую версию
    get_version_command = 'node -v'
    popen = subprocess.Popen(get_version_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    retvalue = ''
    try:
        stdout, stderr = popen.communicate()
        popen.wait()
        nodejs_version = stdout.strip().decode("utf-8")

    finally:
        popen.stdout.close()
        popen.stderr.close()
    return nodejs_version

def refresh_nodejs_version():#Меняет версию Nodejs
    name_file = 'Node_file_version_new.zip';
    name_directory = 'archive'

    file = open(name_file, "wb")




    base.download("https://nodejs.org/download/release/" + number_version_nodejs() + "/node-" + number_version_nodejs() + "-" + initialization_system() + "-x" + initialization_system_capacity() + ".zip", "./node-v10.21.0-win-x64.zip")
    #send_request = requests.get("https://nodejs.org/download/release/" + number_version_nodejs() + "/node-" + number_version_nodejs() + "-" + initialization_system() + "-x" + initialization_system_capacity() + ".zip")
    file.write(send_request.content)
    file.close()

    zipfile_type = zipfile.ZipFile(name_file, 'r')
    zipfile_type.extractall(name_directory)
    zipfile_type.close()

    folder_from = name_directory + "\\node-v" + number_version_nodejs() + "-" + initialization_system() + "-x" + initialization_system_capacity()
    folder_to = "C:\\Program Files\\nodejs"

    for f in os.listdir(folder_from):
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            os.system(f'rd /S /Q {folder_to}\\{f}')
            shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))

    #shutil.rmtree('archive')
    print("Noojs installer")

def installer_nodejs_win():#Устанавливает Nodejs для Windows
    base.configure_common_apps()
    base.download("https://nodejs.org/download/release/" + number_version_nodejs() + "/node-" + number_version_nodejs() + "-" + initialization_system() + "-x" + initialization_system_capacity() + ".zip", "./node-v10.21.0-x64.msi")

    if (subprocess.call("msiexec /i node-" + number_version_nodejs() + "-x" + initialization_system_capacity() + ".msi") != 0):
        exit(0)

    print("Nodejs installer")
    exit(0)

def installer_nodejs():#Устанавливает Nodejs
    if initialization_system() == "win":
        installer_nodejs_win()

def check_nodejs():#Проверяет версию Nodejs устанавливает или меняет её
    
    if (number_version_nodejs() == ""):
        installer_nodejs()

def check_java():#Проверяет версию java устанавливает или меняет её
    
    if (number_version_java() == ""):
        installer_java()

def check_erlang():#Проверяет версию erlang устанавливает или меняет её
    
    if (number_version_erlang() == ""):
        installer_erlang()

def check_mysql():#Проверяет версию MySQL устанавливает или меняет её
    
    if (number_version_mysql() == ""):
        installer_mysql()

def check_ST():#Проверяет версию source tree устанавливает или меняет её
    
    if (number_version_ST() == ""):
        installer_ST()

def check_Git():#Проверяет версию Git устанавливает или меняет её
    
    if (number_version_Git() == ""):
        installer_Git()

def check_RabbitMQ():#Проверяет версию RabbitMQ устанавливает или меняет её
    
    if (number_version_RabbitMQ() == ""):
        installer_RabbitMQ()

def check_all_programs():#Проверяет версию RabbitMQ устанавливает или меняет её
    
    check_nodejs()
    check_java()
    check_erlang()
    check_mysql()
    check_ST()
    check_Git()
    check_RabbitMQ()

def number_version_java():#Определяет установлен или нет Java, если установлен возврашает установленую версию
    get_version_command = 'java -v'
    popen = subprocess.Popen(get_version_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    retvalue = ''
    try:
        stdout, stderr = popen.communicate()
        popen.wait()
        Java_version = stdout.strip().decode("utf-8")

    finally:
        popen.stdout.close()
        popen.stderr.close()
    return Java_version

def installer_java_win():#Устанавливает Java для Windows
    base.configure_common_apps()
    base.download("https://javadl.oracle.com/webapps/download/AutoDL?BundleId=242030_3d5a2bb8f8d4428bbe94aed7ec7ae784", "./chromeinstall-8u251.exe")
    if (subprocess.call(['runas', '/user:Administrator', 'chromeinstall-8u251.exe']) != 0):
        exit(0)

    print("java installer")
    exit(0)

def installer_java():#Устанавливает Java
    if initialization_system() == "win":
        installer_java_win()

def number_version_erlang():#Определяет установлен или нет erlang, если установлен возврашает установленую версию
    get_version_command = 'erl -v'
    popen = subprocess.Popen(get_version_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    retvalue = ''
    try:
        stdout, stderr = popen.communicate()
        popen.wait()
        erlang_version = stdout.strip().decode("utf-8")

    finally:
        popen.stdout.close()
        popen.stderr.close()
    return erlang_version

def installer_erlang():#Устанавливает erlang
    if initialization_system() == "win":
        installer_erlang_win()

def installer_erlang_win():#Устанавливает erlang для Windows
    base.configure_common_apps()
    base.download("http://erlang.org/download/otp_win64_23.0.exe", "./otp_win64_23.0.exe")
    if (subprocess.call("otp_win64_23.0.exe") != 0):
        exit(0)

    print("erlang installer")
    exit(0)

def number_version_mysql():#Определяет установлен или нет MySQL, если установлен возврашает установленую версию
    get_version_command = 'mysqld -v'
    popen = subprocess.Popen(get_version_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    retvalue = ''
    try:
        stdout, stderr = popen.communicate()
        popen.wait()
        mysql_version = stdout.strip().decode("utf-8")

    finally:
        popen.stdout.close()
        popen.stderr.close()
    return mysql_version

def installer_mysql():#Устанавливает Mysql
    if initialization_system() == "win":
        installer_mysql_win()

def installer_mysql_win():#Устанавливает MySQL для Windows
    base.configure_common_apps()
    base.download("https://soft.mydiv.net/win/dlfileb8373_399751/MySQL/mysql-installer-community-8.0.20.0.msi", "./mysql-installer-community-8.0.20.0")

    if (subprocess.call("msiexec /i mysql-installer-community-8.0.20.0") != 0):
        exit(0)

    get_version_command = 'mysql -u root -p < schema/mysql/createdb.sql'
    subprocess.Popen(get_version_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 

def number_version_ST():#Определяет установлен или нет ST, если установлен возврашает установленую версию
    get_version_command = 'sourceteree -v'
    popen = subprocess.Popen(get_version_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    retvalue = ''
    try:
        stdout, stderr = popen.communicate()
        popen.wait()
        RabbitMQ = stdout.strip().decode("utf-8")

    finally:
        popen.stdout.close()
        popen.stderr.close()
    return RabbitMQ

def installer_ST():#Устанавливает source tree
    if initialization_system() == "win":
        installer_ST_win()

def installer_ST_win():#Устанавливает source tree для Windows
    base.configure_common_apps()
    base.download("https://product-downloads.atlassian.com/software/sourcetree/windows/ga/SourceTreeSetup-3.3.9.exe", "./SourceTreeSetup-3.3.9.exe")

    if (subprocess.call("SourceTreeSetup-3.3.9.exe") != 0):
        exit(0)

def number_version_git():#Определяет установлен или нет Git, если установлен возврашает установленую версию
    get_version_command = 'git -v'
    popen = subprocess.Popen(get_version_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    retvalue = ''
    try:
        stdout, stderr = popen.communicate()
        popen.wait()
        nodejs_version = stdout.strip().decode("utf-8")

    finally:
        popen.stdout.close()
        popen.stderr.close()
    return nodejs_version

def installer_Git():#Устанавливает Git
    if initialization_system() == "win":
        installer_Git_win()

def installer_Git_win():#Устанавливает Git для Windows 
    base.configure_common_apps()
    base.download("https://github.com/git-for-windows/git/releases/download/v2.27.0.windows.1/Git-2.27.0-64-bit.exe", "./Git-2.27.0-64-bit.exe")

    if (subprocess.call("Git-2.27.0-64-bit.exe") != 0):
        exit(0)

def number_version_RabbitMQ():#Определяет установлен или нет RabbitMQ, если установлен возврашает установленую версию
    get_version_command = 'rabbc -v'
    popen = subprocess.Popen(get_version_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    retvalue = ''
    try:
        stdout, stderr = popen.communicate()
        popen.wait()
        RabbitMQ = stdout.strip().decode("utf-8")

    finally:
        popen.stdout.close()
        popen.stderr.close()
    return RabbitMQ

def installer_RabbitMQ():#Устанавливает RabbitMQ
    if initialization_system() == "win":
        installer_RabbitMQ_win()

def installer_RabbitMQ_win():#Устанавливает RabbitMQ для Windows
    base.configure_common_apps()
    base.download("https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.5/rabbitmq-server-3.8.5.exe", "./rabbitmq-server-3.8.5.exe")

    if (subprocess.call("Git-2.27.0-64-bit.exe") != 0):
        exit(0)