from bs4 import BeautifulSoup
from urllib import urlopen
import scraperwiki

def convertirUrl(url):
    l= url.split('/')
    newurl= l[0]+l[1]
    return newurl

def listUrl(url):

    response = urlopen(url)
    htmltext = BeautifulSoup(response)

    NewUrl=convertirUrl(url)
    soop = htmltext.find('div',{"class":"basic-table"})
    links = soop.find_all('a')
    href=[]
    for i in range(0,len(links)-1):
        href.append(NewUrl+links[i].get('href'))

    return href

def getId(Url):
    url= Url.split('=')
    return url[1]

def titre(Text):
    a= Text.split("1.")
    b= a[1].split("2.")
    c= b[0].split(':')
    return c[1]+':'+c[2]

def Awarding(Text):
    a= Text.split("2.")
    b= a[1].split("3.")
    c= b[0].split('Authority:')
    return c[1]

def contact_type(Text):
    a= Text.split("3.")
    b= a[1].split("4.")
    c= b[0].split('Contract Type:')
    return c[1]

def descpription(Text):
    a= Text.split("4.")
    b= a[1].split("5.")
    c= b[0].split('Description:')
    return c[1]

def cvp(Text):
    a= Text.split("5.")
    b= a[1].split("6.")
    c= b[0].split('CPV Codes:')
    return c[1]

def nuts(Text):
    a= Text.split("6.")
    b= a[1].split("7.")
    c= b[0].split('NUTS Codes :')
    return c[1]

def Main(Text):
    a= Text.split("7.")
    b= a[1].split("8.")
    c= b[0].split('Main Site or Location of Works, Main Place of Delivery or Main Place of Performance:')
    return c[1]

def reference(Text):
    a= Text.split("8.")
    b= a[1].split("9.")
    c= b[0].split('Reference Attributed by the Awarding Authority:')
    return c[1]

def estimated(Text):
    a= Text.split("9.")
    b= a[1].split("10.")
    c= b[0].split('Estimated Value of Requirement:')
    return c[1]

def deadline(Text):
    a= Text.split("10.")
    b= a[1].split("11.")
    c= b[0].split('Deadline for Expression of Interest:')
    return c[1]

def address(Text):
    a= Text.split("11.")
    b= a[1].split("12.")
    c= b[0].split('Address to which they must be sent:')
    return c[1]

def other12(Text):
    a= Text.split("12.")
    c= a[1].split('Other Information:')
    return c[2]

def other13(Text):
    a= Text.split("12.")
    b= a[1].split("13.")
    c= b[0].split('Other Information:')
    return c[2]

def amendment(Text):
    a= Text.split("13.")
    c= a[1].split('Description of Amendment / Addition:')
    return c[1]


def scrap(url):
    response = urlopen(url)
    htmltext = BeautifulSoup(response)

    Id=getId(url)
    suit =htmltext.find('div',{"id":"content1"}).findAll('label')
    Text= BeautifulSoup(str(suit[3])).text

    Published=BeautifulSoup(str(suit[2])).text

    Titre= titre(Text)
    Awarding_Authority=Awarding(Text)
    try:
        Contact_Type =contact_type(Text)
    except:
        Contact_Type =""
    Decription = descpription(Text)
    CVP_Codes = cvp(Text)
    NUTS_Codes= nuts(Text)
    Main_Site_or_Location_of_Works=Main(Text)
    Reference_Attributed_by_the_Awarding_Authority=reference(Text)
    Estimated_Value_of_Requirement=estimated(Text)
    Deadline_for_Expression_of_Interest=deadline(Text)
    Address_to_which_they_must_be_sent=address(Text)
    try:
        Other_Information=other13(Text)
    except:
        Other_Information=other12(Text)
    try :
        Description_of_Amendment=amendment(Text)
    except:
        Description_of_Amendment=""


    data={"ID":unicode(Id), \
          "Url":unicode(url),\
          "Title":unicode(Title),\
          "Published":unicode(Published),\
          "Awarding Authority":unicode(Awarding_Authority),\
          "Contact Type":unicode(Contact_Type),\
          "Decription":unicode(Decription),\
          "CVP Codes":unicode(CVP_Codes),\
          "NUTS Codes":unicode(NUTS_Codes),\
          "Main Site or Location of Works":unicode(Main_Site_or_Location_of_Works),\
          "Reference Attributed by the Awarding Authority":unicode(Reference_Attributed_by_the_Awarding_Authority),\
          "Estimated Value of Requirement":unicode(Estimated_Value_of_Requirement),\
          "Deadline for Expression of Interest":unicode(Deadline_for_Expression_of_Interest),\
          "Address to which they must be sent":unicode(Address_to_which_they_must_be_sent),\
          "Other Information":unicode(Other_Information),\
          "Description of Amendment":unicode(Description_of_Amendment)}
    scraperwiki.sqlite.save(unique_keys=['ID'], data=data)




if __name__ == '__main__':
    lis=["http://noticesearch.supply4nwfire.org.uk/noticeSearch/viewNotice.html?displayNoticeId=108456102","http://noticesearch.supply4nwfire.org.uk/noticeSearch/viewNotice.html?displayNoticeId=141938986",
    "http://noticesearch.supply4nwfire.org.uk/noticeSearch/viewNotice.html?displayNoticeId=80347654","http://noticesearch.supply4nwfire.org.uk/noticeSearch/viewNotice.html?displayNoticeId=57046877"]
    for i in lis :
        scrap(i)
