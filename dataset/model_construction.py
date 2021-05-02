from xml.dom import minidom
import csv

# parse an xml file by name
mydoc = minidom.parse('annotations.xml')

images = mydoc.getElementsByTagName('image')
heads=[]
for image in images:
    boxes= image.getElementsByTagName('box')
    for box in boxes:
    
        if(box.attributes["label"].value=="head"):

            heads.append(box)
print(len(heads))
FinalData=[]

for head in heads:
    Data={}
    atts=head.getElementsByTagName('attribute')
    for att in atts:
            if(att.attributes["name"].value=="has_safety_helmet"):Data["has_safety_helmet"] = (att.firstChild.data)
            elif(att.attributes["name"].value=="mask") : Data["mask"]=(att.firstChild.data)
            else:pass
    FinalData.append(Data)

    
filename = "ConstructionData.csv"
fields = ["mask","has_safety_helmet"]

# writing to csv file 
with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
        
    # writing data rows 
    writer.writerows(FinalData) 

