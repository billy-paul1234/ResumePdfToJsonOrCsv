#program to convert resume pdf to csv file


import PyPDF2
import csv

#to convert dict to csv
def dictToCSV(data,output_file):
    keys = list(data.keys())
    lists = list(data.values())

    max_length = max(len(lst) for lst in lists)

    filled_lists = [lst + [None] * (max_length - len(lst)) for lst in lists]

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        writer.writerow(keys)
        
        writer.writerows(zip(*filled_lists))

    print(f"Data successfully converted and saved to {output_file}.")

#to convert pdf to dict
def resumePdfToCsv(pdfPath,csvPath):
    d={}
    dl=[]
    pline="PERSONAL_DETAILS"#to store the key
    myFile = open(pdfPath,"rb")
    pdfReader = PyPDF2.PdfFileReader(myFile)
    numOfPages = pdfReader.numPages

    #reading headings to take key from pdf text
    with open ("./heading.txt", "r") as myfile:
        headings=myfile.readlines()

    #pdf to text
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

                #comparing the heading and pdf text to trim a heading from pdf text 
                if heading1.lower() == line1.lower() or heading1.upper() in line1 or heading1.lower()+":" in line1.lower() :
                    d[pline]=dl#add list to key in dict
                    dl=[]
                    pline=heading[:-1].upper()
                    #if the key don't want to repeat in the value then uncomment tmp=1
                    #tmp=1
                    break

            #add the line to list if it not has any heading
            if tmp == 0:
                dl.append(line)
        d[pline]=dl
    myFile.close()
    dl=[]
    for x in d:
        if d[x]==[]:
            dl.append(x)
            pass
    for x in dl:
        del d[x]
    dictToCSV(d,csvPath)


#for i in range(1,6):
#    pdfPath="pdfs/"+str(i)+".pdf"
#    csvPath="csv/"+str(i)+".csv"
#    resumePdfToCsv(pdfPath,csvPath)

pdfPath=input("Entera path to pdf (/home/uname/file.pdf) : ")
jsonPath=input("Enter a path to output file (/home/unmae/file.csv) : ")
resumePdfToCsv(pdfPath,csvPath)
