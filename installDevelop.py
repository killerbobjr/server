import sys
import os
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

def name_directory():#возврашает название временной папки
    return "initialization_number_version_or_programm_nodejs"

def number_version_nodejs_check():#Определяет установлен или нет Nodejs, если установлен возврашает установленую версию
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
    send_request = requests.get("https://nodejs.org/download/release/" + number_version_nodejs() + "/node-" + number_version_nodejs() + "-" + initialization_system() + "-x" + initialization_system_capacity() + ".zip")
    file.write(send_request.content)
    file.close()

    zipfile_type = zipfile.ZipFile(name_file, 'r')
    zipfile_type.extractall(name_directory)
    zipfile_type.close()

    folder_from = name_directory + "\\node-" + number_version_nodejs() + "-" + initialization_system() + "-x" + initialization_system_capacity()
    folder_to = "C:\\Program Files\\nodejs"

    for f in os.listdir(folder_from):
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            os.system(f'rd /S /Q {folder_to}\\{f}')
            shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))

    #shutil.rmtree('archive')
    print("Noojs installer")

    if number_version_nodejs() != number_version_nodejs():
        print("failed to change the version of the Nodejs, do it manually")
        exit(0)


def installer_nodejs_win():#Устанавливает Nodejs для Windows
    f = open("node-" + number_version_nodejs() + "-x" + initialization_system_capacity() + ".msi", "wb")
    send_request = requests.get("https://nodejs.org/dist/" + number_version_nodejs() + "/node-" + number_version_nodejs() + "-x" + initialization_system_capacity() + ".msi")
    f.write(send_request.content)
    f.close()
    if (subprocess.call("msiexec /i node-" + number_version_nodejs() + "-x" + initialization_system_capacity() + ".msi") != 0):
        exit(0)
    os.remove("node-" + number_version_nodejs() + "-x" + initialization_system_capacity() + ".msi")
    print("Noojs installer")

def installer_nodejs():#Устанавливает Nodejs
    if initialization_system() == "win":
        installer_nodejs_win()

def cast_nodejs():#Проверяет версию Nodejs устанавливает или меняет её
    if (number_version_nodejs_check() != ""):
        if number_version_nodejs() != number_version_nodejs():
            refresh_nodejs_version()
    else:
        installer_nodejs()
    print("the correct version is installed Nodejs")

cast_nodejs()