#program to convert resume pdf to json file


import PyPDF2
import json

def resumepdftojson(pdfPath,jsonPath):
    d={}
    dl=[]
    pline="PERSONAL_DETAILS"
    myFile = open(pdfPath,"rb")
    output_file = open(jsonPath[:-4]+"txt", "w")
    pdfReader = PyPDF2.PdfFileReader(myFile)
    numOfPages = pdfReader.numPages

    with open ("./heading.txt", "r") as myfile:
        headings=myfile.readlines()

    for i in range(numOfPages):
        page = pdfReader.getPage(i)
        text = page.extractText()
        #print(text)
        print("-----------------------------------")
        for line in text.replace(".","\n").split("\n"):
            tmp=0
            line1=line.replace(" ","")
            for heading in headings:
                heading1=heading[:-1].replace(" ","")
                if heading1.lower() == line1.lower() or heading1.upper() in line1 or heading1.lower()+":" in line1.lower() :
                    d[pline]=dl
                    dl=[]
                    pline=heading[:-1].upper()
                    #if the key don't want to repeat in the value then uncomment tmp=1
                    #tmp=1
                    break
            if tmp == 0:
                dl.append(line)
        d[pline]=dl
        output_file.write(text)
    output_file.close()
    myFile.close()
    dl=[]
    for x in d:
        if d[x]==[]:
            dl.append(x)
            pass
    for x in dl:
        del d[x]
    json_string=json.dumps(d,indent = 9)
    f = open(jsonPath, "w")
    f.write(json_string)
    f.close()


#for i in range(1,31):
#    pdfPath="pdfs/"+str(i)+".pdf"
#    jsonPath="json/"+str(i)+".json"
#    resumepdftojson(pdfPath,jsonPath)


pdfPath=input("Entera path to pdf (/home/uname/file.pdf) : ")
jsonPath=input("Enter a path to output file (/home/unmae/file.json) : ")
resumepdftojson(pdfPath,jsonPath)