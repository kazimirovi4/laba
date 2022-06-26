import re

# url1 = "http://github.com/carbonfive/raygun"   -> domain name = "github"
# url2 = "http://www.zombie-bites.com"           -> domain name = "zombie-bites"
# url3 = "https://www.cnet.com"                  -> domain name = "cnet"


def domain_name(url):
    match = re.search(r'[./]?(?:www.)?\w+\-?\w+[.]', url)
    s = match[0]
    s = s.replace('www', '')
    s = s.replace('.', '')
    s = s.replace('/', '')
    return s


if __name__ == '__main__':
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
