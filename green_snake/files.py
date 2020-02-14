import os
# import sys
# from shutil import copyfile
# import time

def getFilesFromFolder(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk("./resources/"+path):
        for file in f:
            if not file.startswith(".") and file.endswith(".msg"):  # ".msg" in file:
                files.append(os.path.join(r, file))
    return files

def loadMessage(token, company_code, file_path):
    data = file_path.split("/")[-1].split(".")
    contents = ""
    df = open(file_path, "r")
    for l in df:
        contents += l
    message = {
        "documentType": data[0],
        "sender": data[1],
        "receiver": data[2],
        "msgNumber": data[3],
        "numVersion": data[4],
        "messageFormat": data[5],
        "signed": data[6],
        "companyCode": company_code,
        "securityToken": token,
        "path": file_path
    }
    return message

