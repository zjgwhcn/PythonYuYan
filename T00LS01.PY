#C段查询

from bs4 import BeautifulSoup
import requests
import socket
import sys
import os
import re


def main():
        for i in range(1,255):
                ips = re.findall(r'.+\.',ip)[0]+str(i)
                print ('[+]:%s' %ips)
                fout = open('release.txt','a')
                fout.write('[+]:%s\n' %ips)
                while True:
                        ver = ['0']
                        urls = set([])
                        try:
                                for page in range(0,100):
                                        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
                                        url = 'https://cn.bing.com/search?ensearch=2&q=ip:%s&first=%d0' %(ips,page)
                                        s = requests.get(url,headers=headers)
                                        info_string = BeautifulSoup(s.text,"html.parser")

                                        for info_page in info_string.find_all("a",{"class":"sb_pagS"}):
                                                ver.append(info_page.text)

                                        if ver[page] == ver[page+1]:
                                                break

                                        for info in info_string.find_all("cite"):
                                                delete = re.compile(r'/.+')
                                                relest = delete.sub('',info.text)
                                                urls.add(relest)
                                                
                                for url in urls:
                                        print (url)
                                        fout.write('%s\n' %url)

                        except:
                                pass

                        break

                fout.close()

if __name__ == '__main__':
        if len(sys.argv) != 2:
                print ('Usage: ' + os.path.basename(sys.argv[0]) + ' [url]www.baidu.com[/url]')
                sys.exit()
        domain = sys.argv[1]        
        ip = socket.gethostbyname(domain)
        main()
