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
    
    #f = open("node-v" + number_version_nodejs() +  "-x" + initialization_system_capacity() + ".msi", "wb")
    base.configure_common_apps()
    #input(os.environ["PATH"] )
    #base.download("https://nodejs.org/dist/v10.21.0/node-v10.21.0-x64.msi", "./node-v10.21.0-x64.msi")
    base.download("https://nodejs.org/download/release/" + number_version_nodejs() + "/node-" + number_version_nodejs() + "-" + initialization_system() + "-x" + initialization_system_capacity() + ".zip", "./node-v10.21.0-x64.msi")
    #send_request = requests.get("https://nodejs.org/dist/v" + number_version_nodejs() + "/node-v" + number_version_nodejs() + "-x" + initialization_system_capacity() + ".msi")
    #f.write(send_request.content)
    #f.close()
    #input("node-" + number_version_nodejs() + "-x" + initialization_system_capacity() + ".msi")
    if (subprocess.call("msiexec /i node-" + number_version_nodejs() + "-x" + initialization_system_capacity() + ".msi") != 0):
        exit(0)

    print("Noojs installer")
    exit(0)

def installer_nodejs():#Устанавливает Nodejs
    if initialization_system() == "win":
        installer_nodejs_win()

def begin_nodejs():#Проверяет версию Nodejs устанавливает или меняет её
    
    if (number_version_nodejs() != ""):
        
        refresh_nodejs_version()
    else:
        
        installer_nodejs()

def begin_java():#Проверяет версию java устанавливает или меняет её
    
    if (number_version_java() != ""):
        
        refresh_java_version()
    else:
        
        installer_java()

def begin_erlang():#Проверяет версию erlang устанавливает или меняет её
    
    if (number_version_erlang() != ""):
        
        refresh_erlang_version()
    else:
        
        installer_erlang()

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
    base.download("https://www.java.com/ru/download/win8.jsp/chromeinstall-8u251.exe", "./chromeinstall-8u251.exe")
    if (subprocess.call(['runas', '/user:Administrator', 'chromeinstall-8u251.exe']) != 0):
        exit(0)

    print("Noojs java")
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
    base.download("https://www.erlang.org/downloads/otp_win64_23.0.exe", "./otp_win64_23.0.exe")
    if (subprocess.call("otp_win64_23.0.exe") != 0):
        exit(0)

    print("Noojs erlang")
    exit(0)

installer_erlang()