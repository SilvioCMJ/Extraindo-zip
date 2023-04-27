from zipfile import ZipFile

arquivo = 'exemplo.zip'
#abrindo

with ZipFile(arquivo, 'r') as zip:
    zip.printdir()

    #extraindo
    zip.extractall()