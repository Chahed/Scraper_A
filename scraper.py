from bs4 import BeautifulSoup
from urllib import urlopen
from splinter import Browser
import time
import random
import scraperwiki

def suittext(text):
    text=text.replace(", ,","")
    text=text.replace("'","")
    text=text.replace("  ","")
    text=text.replace("u\\n","")
    text=text.replace("\\r"," ")
    text=text.replace("[","")
    text=text.replace("]","")
    text=text.replace("\t","")
    return text

def dateclean(date):
    d=suittext(date).split('/')
    return d[2].strip()+'-'+d[1].strip()+'-'+d[0].strip()

def datecleannow(date):
    a=date.split(' ')
    d=a[1].split('/')
    return d[2].strip(" ")+'-'+d[1].strip(" ")+'-'+d[0].strip(" ")

def convertirUrl(url):
    l= url.split('/')
    newurl= l[0]+'//'+l[2]+'/'+l[3]+'/'
    return newurl

def duration(Text):
    a=Text.split("II.3)Duration Of The Contract Or Time-Limit For Completion")
    b=a[1].split("Information About Lots")
    return b[0]

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
    c= b[0].split('<br></br>')
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

def duration(Text):
    a=Text.split("II.3)Duration Of The Contract Or Time-Limit For Completion")
    b=a[1].split("Information About Lots")
    return b[0]

def deadlinenew(Text):
    a= Text.split("IV.3.4)Time-limit for receipt of tenders or requests to participate")
    b= a[1].split("VI.3.5)")
    c=b[0].split("Date: ")
    d=c[1].split("Time: ")
    return d[0]

def nuts(Text):
    a= Text.split("6.")
    b= a[1].split("7.")
    c= b[0].split('NUTS Codes :')
    return c[1]

def cvpnow(Text):
    a=Text.split("II.1.6)Common Procurement Vocabulary:")
    b=a[1].split("II.1.7)")
    return b[0]

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
    try:
        return c[2]
    except:
        return c[1]

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
    Text2= str(suit[3])
    Published=suittext(BeautifulSoup(str(suit[2])).text)
    Published_clean=suittext(dateclean(Published))

    Title= suittext(titre(Text))
    Awarding_Authority=suittext(Awarding(Text2))
    try:
        Contact_Type =suittext(contact_type(Text))
    except:
        Contact_Type =""
    Decription = suittext(descpription(Text))
    CPV_Codes = suittext(cvp(Text))
    NUTS_Codes= suittext(nuts(Text))
    Main_Site_or_Location_of_Works=suittext(Main(Text))
    Reference_Attributed_by_the_Awarding_Authority=suittext(reference(Text))
    Estimated_Value_of_Requirement=suittext(estimated(Text))
    Deadline_for_Expression_of_Interest=suittext(deadline(Text))
    Deadline_for_Expression_of_Interest_clean=suittext(datecleannow(Deadline_for_Expression_of_Interest))
    Address_to_which_they_must_be_sent=suittext(address(Text))
    try:
        Other_Information=suittext(other13(Text))
    except:
        Other_Information=suittext(other12(Text))
    try :
        Description_of_Amendment=suittext(amendment(Text))
    except:
        Description_of_Amendment=""
    data={"ID":unicode(Id), \
          "Url":unicode(url),\
          "Title":unicode(Title),\
          "Published":unicode(Published),\
          "Published clean":unicode(Published_clean),\
          "Awarding Authority":unicode(Awarding_Authority),\
          "Contact Type":unicode(Contact_Type),\
          "Decription":unicode(Decription),\
          "CPV Codes":unicode(CPV_Codes),\
          "NUTS Codes":unicode(NUTS_Codes),\
          "Main Site or Location of Works":unicode(Main_Site_or_Location_of_Works),\
          "Reference Attributed by the Awarding Authority":unicode(Reference_Attributed_by_the_Awarding_Authority),\
          "Estimated Value of Requirement":unicode(Estimated_Value_of_Requirement),\
          "Deadline for Expression of Interest":unicode(Deadline_for_Expression_of_Interest),\
          "Deadline for Expression of Interest clean":unicode(Deadline_for_Expression_of_Interest_clean),\
          "Address to which they must be sent":unicode(Address_to_which_they_must_be_sent),\
          "Other Information":unicode(Other_Information),\
          "Description of Amendment":unicode(Description_of_Amendment),\
          "Duration Of The Contract Or Time Limit For Completion":unicode()}
    scraperwiki.sqlite.save(unique_keys=['ID'], data=data)
      
def scrap_now(url):
    response = urlopen(url)
    htmltext = BeautifulSoup(response)
    Id=getId(url)

    suit =htmltext.find('div',{"id":"content1"}).findAll('label')
    Text= BeautifulSoup(str(suit[3])).text
    Description= BeautifulSoup(str(suit[3])).text
    Description=Description.encode('ascii','ignore')

    Published=BeautifulSoup(str(suit[2])).text
    Published_clean=dateclean(Published)

    Title=BeautifulSoup(str(suit[0])).text
    Awarding_Authority=BeautifulSoup(str(suit[1])).text
    try:
        CPV_Codes = suittext(cvpnow(Text))
    except:
        CPV_Codes=""
    try:
        Deadline_for_Expression_of_Interest=suittext(deadlinenew(Text))
    except :
        Deadline_for_Expression_of_Interest=""
    if Deadline_for_Expression_of_Interest!="":
        Deadline_for_Expression_of_Interest_clean=suittext(dateclean(Deadline_for_Expression_of_Interest))
    else :
        Deadline_for_Expression_of_Interest_clean=""
    try:
        Duration_Of_The_Contract_Or_Time_Limit_For_Completion=suittext(duration(Text))
    except:
        Duration_Of_The_Contract_Or_Time_Limit_For_Completion=""

    
    data={"ID":unicode(Id), \
          "Url":unicode(url),\
          "Title":unicode(Title),\
          "Published":unicode(Published),\
          "Published clean":unicode(Published_clean),\
          "Awarding Authority":unicode(Awarding_Authority),\
          "Contact Type":unicode(),\
          "Decription":unicode(Description),\
          "CPV Codes":unicode(CPV_Codes),\
          "NUTS Codes":unicode(),\
          "Main Site or Location of Works":unicode(),\
          "Reference Attributed by the Awarding Authority":unicode(),\
          "Estimated Value of Requirement":unicode(),\
          "Deadline for Expression of Interest":unicode(Deadline_for_Expression_of_Interest),\
          "Deadline for Expression of Interest clean":unicode(Deadline_for_Expression_of_Interest_clean),\
          "Address to which they must be sent":unicode(),\
          "Other Information":unicode(),\
          "Description of Amendment":unicode(),\
          "Duration Of The Contract Or Time Limit For Completion":unicode(Duration_Of_The_Contract_Or_Time_Limit_For_Completion)}
    scraperwiki.sqlite.save(unique_keys=['ID'], data=data)

def  Navigation(link):
    with Browser("phantomjs", service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any']) as browser:
        browser.driver.set_window_size(1280, 1024)
        browser.visit(link)
        time.sleep(random.uniform(0.5,2.9))
        button = browser.find_by_name("editSearch")
        button.click()
        button = browser.find_by_name("Search")
        button.click()
        htmltext = BeautifulSoup(browser.html, "html.parser")
        soop = htmltext.find('table',{"id":"noticeResults"}).findNext('tbody')
        links = soop.findAll('a')
        href=[]
        for i in range(0,len(links)-1):
            href.append(convertirUrl(link)+links[i].get('href'))
        j=1
        try:
            while(1):
                time.sleep(random.uniform(0.5,2.9))
                j = j+1
                page = "?page=" + str(j)
                button = browser.find_by_css('a[href=' + '"' + page + '"' +']')
                button.click()
                htmltext = BeautifulSoup(browser.html, "html.parser")
                soop = htmltext.find('table',{"id":"noticeResults"}).findNext('tbody')
                links = soop.findAll('a')
                for i in range(0,len(links)-1):
                    href.append(convertirUrl(link)+links[i].get('href'))

        except:
            pass
    return href

def main():
    urls = ['http://noticesearch.supply4nwfire.org.uk/noticeSearch/noticeSearchResults.html?page=1']

    for link in urls:
        href=Navigation(link)
        for i in href:
            try:
                scrap(i)
            except:
                scrap_now(i)




if __name__ == '__main__':
    main()


