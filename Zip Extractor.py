from zipfile import ZipFile
filepath=r'input your file path here'
with ZipFile(filepath,'r') as zip:
    zip.printdir()
    zip.extractall()
