from bs4 import BeautifulSoup
import requests
import urllib2

url = 'http://10.11.100.17/.hidden/'
r = requests.get(url, allow_redirects=True)

data = r.text
soup = BeautifulSoup(data)

i = 0

for link in soup.find_all('a'):
    dire = link.get('href')
    if dire != "../":
        url2 = url + dire
        r2 = requests.get(url2, allow_redirects=True)
        data2 = r2.text
        soup2 = BeautifulSoup(data2)
        for link2 in soup2.find_all('a'):
            dire2 = link2.get('href')
            if dire2 != "../":
                url3 = url2 + dire2
                #print(url3)
                r3 = requests.get(url3, allow_redirects=True)
                data3 = r3.text
                soup3 = BeautifulSoup(data3)
                for link3 in soup3.find_all('a'):
                    dire3 = link3.get('href')
                    if dire3 != "../":
                        url4 = url3 + dire3
                        r4 = requests.get(url4, allow_redirects=True)
                        data4 = r4.text
                        soup4 = BeautifulSoup(data4)
                        for link4 in soup4.find_all('a'):
                            dir4 = link4.get('href')
                            if dir4 != "../":
                                url5 = url4 + dir4
                                if dir4 == "README":
                                    print(url5)
                                    read = requests.get(url5, allow_redirects=True)
                                    open("./readme", 'a').write(read.content)
                                    i += 1
                        if dire3 == "README":
                            print(url4)
                            read = requests.get(url4, allow_redirects=True)
                            open("./readme", 'a').write(read.content)
                            i += 1
                if dire2 == "README":
                        print(url3)
                        read = requests.get(url3, allow_redirects=True)
                        open("./readme", 'a').write(read.content)
                        i += 1
        if dire == "README":
            print(url2)
            read = requests.get(url2, allow_redirects=True)
            open("./readme", 'a').write(read.content)
            i += 1


print(i)
