from bs4 import BeautifulSoup
<<<<<<< HEAD
from urllib.request import urlopen
from splinter import Browser
import time
import random
=======
from urllib import urlopen
>>>>>>> origin/master
import scraperwiki

def dateclean(date):
    d=date.split('/')
    return d[2]+'-'+d[1]+'-'+d[0]

def datecleannow(date):
    a=date.split(' ')
    d=a[1].split('/')
    return d[2]+'-'+d[1]+'-'+d[0]

def convertirUrl(url):
    l= url.split('/')
    newurl= l[0]+'//'+l[2]+'/'+l[3]+'/'
    return newurl


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

    Published=BeautifulSoup(str(suit[2])).text
    Published_clean=dateclean(Published)

    Title= titre(Text)
    Awarding_Authority=Awarding(Text)
    try:
        Contact_Type =contact_type(Text)
    except:
        Contact_Type =""
    Description = descpription(Text)
    CVP_Codes = cvp(Text)
    NUTS_Codes= nuts(Text)
    Main_Site_or_Location_of_Works=Main(Text)
    Reference_Attributed_by_the_Awarding_Authority=reference(Text)
    Estimated_Value_of_Requirement=estimated(Text)
    Deadline_for_Expression_of_Interest=deadline(Text)
    Deadline_for_Expression_of_Interest_clean=datecleannow(Deadline_for_Expression_of_Interest)
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
          "Published clean":unicode(Published_clean),\
          "Awarding Authority":unicode(Awarding_Authority),\
          "Contact Type":unicode(Contact_Type),\
          "Description":unicode(Description),\
          "CVP Codes":unicode(CVP_Codes),\
          "NUTS Codes":unicode(NUTS_Codes),\
          "Main Site or Location of Works":unicode(Main_Site_or_Location_of_Works),\
          "Reference Attributed by the Awarding Authority":unicode(Reference_Attributed_by_the_Awarding_Authority),\
          "Estimated Value of Requirement":unicode(Estimated_Value_of_Requirement),\
          "Deadline for Expression of Interest":unicode(Deadline_for_Expression_of_Interest),\
          "Deadline for Expression of Interest clean":unicode(Deadline_for_Expression_of_Interest_clean),\
          "Address to which they must be sent":unicode(Address_to_which_they_must_be_sent),\
          "Other Information":unicode(Other_Information),\
          "Description of Amendment":unicode(Description_of_Amendment)}
    scraperwiki.sqlite.save(unique_keys=['ID'], data=data)

def scrap_now(url):
    response = urlopen(url)
    htmltext = BeautifulSoup(response)
    Id=getId(url)

    suit =htmltext.find('div',{"id":"content1"}).findAll('label')
    Description= BeautifulSoup(str(suit[3])).text
    Description=Description.encode('ascii','ignore')

    Published=BeautifulSoup(str(suit[2])).text
    Published_clean=dateclean(Published)

    Title=BeautifulSoup(str(suit[0])).text
    Awarding_Authority=BeautifulSoup(str(suit[1])).text

    data={"ID":unicode(Id), \
          "Url":unicode(url),\
          "Title":unicode(Title),\
          "Published":unicode(Published),\
          "Published clean":unicode(Published_clean),\
          "Awarding Authority":unicode(Awarding_Authority),\
          "Contact Type":unicode(),\
          "Decription":unicode(Description),\
          "CVP Codes":unicode(),\
          "NUTS Codes":unicode(),\
          "Main Site or Location of Works":unicode(),\
          "Reference Attributed by the Awarding Authority":unicode(),\
          "Estimated Value of Requirement":unicode(),\
          "Deadline for Expression of Interest":unicode(),\
          "Deadline for Expression of Interest clean":unicode(),\
          "Address to which they must be sent":unicode(),\
          "Other Information":unicode(),\
          "Description of Amendment":unicode()}
    scraperwiki.sqlite.save(unique_keys=['ID'], data=data)



def Navigation(link):
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
            print (convertirUrl(link)+links[i].get('href'))
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
                    print (convertirUrl(link)+links[i].get('href'))
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


def scrap_now(url):
    response = urlopen(url)
    htmltext = BeautifulSoup(response)
    Id=getId(url)

    suit =htmltext.find('div',{"id":"content1"}).findAll('label')
    Description= BeautifulSoup(str(suit[3])).text
    Description=Description

    Published=BeautifulSoup(str(suit[2])).text

    Title=BeautifulSoup(str(suit[0])).text
    Awarding_Authority=BeautifulSoup(str(suit[1])).text

    data={"ID":unicode(Id), \
          "Url":unicode(url),\
          "Title":unicode(Title),\
          "Published":unicode(Published),\
          "Awarding Authority":unicode(Awarding_Authority),\
          "Contact Type":unicode(),\
          "Description":unicode(Description),\
          "CVP Codes":unicode(),\
          "NUTS Codes":unicode(),\
          "Main Site or Location of Works":unicode(),\
          "Reference Attributed by the Awarding Authority":unicode(),\
          "Estimated Value of Requirement":unicode(),\
          "Deadline for Expression of Interest":unicode(),\
          "Address to which they must be sent":unicode(),\
          "Other Information":unicode(),\
          "Description of Amendment":unicode()}
    scraperwiki.sqlite.save(unique_keys=['ID'], data=data)

if __name__ == '__main__':
<<<<<<< HEAD
    main()

=======
    lis=["http://noticesearch.supply4nwfire.org.uk/noticeSearch/viewNotice.html?displayNoticeId=108456102","http://noticesearch.supply4nwfire.org.uk/noticeSearch/viewNotice.html?displayNoticeId=141938986",
    "http://noticesearch.supply4nwfire.org.uk/noticeSearch/viewNotice.html?displayNoticeId=80347654","http://noticesearch.supply4nwfire.org.uk/noticeSearch/viewNotice.html?displayNoticeId=57046877",
    "http://noticesearch.supply4nwfire.org.uk/noticeSearch/viewNotice.html?displayNoticeId=64179696"]
    for i in lis :
        try:
            scrap(i)
        except:
            scrap_now(i)
>>>>>>> origin/master
