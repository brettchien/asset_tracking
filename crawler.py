import pycurl
import cStringIO
from BeautifulSoup import BeautifulSoup

def main():
    buf = cStringIO.StringIO()

    c = pycurl.Curl()
    c.setopt(c.URL, "http://sunshine.cy.gov.tw/GipOpenWeb/wSite/lp?ctNode=442&mp=2&nowPage=1&pagesize=300")
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()

    content = buf.getvalue()
    buf.close()

    soup = BeautifulSoup(content)
    baseURL = "http://sunshine.cy.gov.tw/GipOpenWeb/wSite/"
    for link in soup.findAll("a", {"target": "_blank", "title": None}):
        url = baseURL + link['href']
        title = link.img['title']
        print title
        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, buf.write)
        c.perform()
        f = open(title, 'wb')
        f.write(buf.getvalue())
        f.close()
        buf.close()

if __name__ == "__main__":
    main()
