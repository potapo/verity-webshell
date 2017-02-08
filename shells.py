import requests
from sets import Set
from time import sleep
from threading import Thread

thread_count = 3
shells = dict();


class URLThread(Thread):
    def __init__(self, urls, timeout):
        super(URLThread, self).__init__()
        self.urls = urls
        self.timeout = timeout

    def run(self):
        try:
            for x in self.urls:
                url, password = x.split('|')[0], x.split('|')[1]
                try:
                    if requests.get(url, timeout = self.timeout, ).status_code == 200:
                        print "add",url
                        shells[url] = password
                except requests.RequestException:
                    pass
        except Exception , what:
            pass

def multi_get(uris, timeout=2):

    threads = list()
    page,i = len(uris)/thread_count, 0
    while i*page<len(uris):
        a = i*page
        b= (i+1)*page if len(uris)>=(i+1)*page else len(uris)
        threads.append(URLThread(uris[a:b], timeout))
        i+=1
    print len(threads)
    for thread in threads:
        thread.start()
    for t in threads:
        t.join()
    with open("/Users/captain/shell.txt","a") as f:
        for k,v in shells.items():
            f.writelines(k+":"+v)



dict = Set()
with open('/Users/captain/Downloads/01-10.txt', 'r') as f:
    for x in f.xreadlines():
        dict.add(x)

urls = list(dict)
multi_get(urls)
