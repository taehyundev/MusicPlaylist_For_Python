import os

def fileList():
    resultList =list()
    path = './playlist'
    file_list = os.listdir(path)
    for x in file_list:
        resultList.append(x)
    return resultList
