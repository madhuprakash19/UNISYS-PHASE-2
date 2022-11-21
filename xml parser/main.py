import xml.etree.ElementTree as ET


def displayRoot():
    mytree = ET.parse('sample.xml')
    myroot = mytree.getroot()
    list=[]
    list.append(myroot.tag)
    return list

def displayChild():
    mytree = ET.parse('sample.xml')
    myroot = mytree.getroot()
    tag_names = {t.tag for t in myroot.findall('.//student/*')}
    return tag_names

def getDetails():
    mytree = ET.parse('sample.xml')
    myroot = mytree.getroot()
    for x in myroot.findall('student'):
       name =x.find('name').text
       usn = x.find('usn').text
       section=x.find('section').text
       cgpa=x.find('cgpa').text
       print(name, usn,section,cgpa)


print("1.Get Root Tag\n2.Get Child Tags\n3.Get Student Details\n4.Exit\n")
while(True):
    ch=int(input("Enter your choice: "))
    if(ch==1):
        print(displayRoot())
    elif(ch==2):
        print(displayChild())
    elif(ch==3):
        getDetails()
    elif(ch==4):
        break
