import csv
doc=open("archivo.csv","w")

doc_csv_w=csv.writer(doc)

lista=["Pedro",98660]

doc_csv_w.writerow (lista)

doc.close()

#un caso más real version de pytho 2.7
doc=open("archivo.csv","w")

doc_csv_w=csv.writer(doc)

lista=[["Pedro",98660], ["Lucas",258],["Federico",1598],["Arturo", 45874]]

#Se recorre con un for
for x in lista:
    doc_csv_w.writerow(x)

doc.close()
