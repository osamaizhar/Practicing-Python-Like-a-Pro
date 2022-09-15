def domain_name(url):
    if "//" in url:
        start=url.find("//")+2
    else:
        start=url.find(".")+1
    #domain=url[start:]
    #print(domain)
    # if "www." in domain:
    #     domain=domain[4:]
    end=url[start:].find(".")+start
    return url[start:end]
print(domain_name("https://youtube.com"))
# test.assert_equals(domain_name(), "google")
# test.assert_equals(domain_name("http://google.co.jp"), "google")
# test.assert_equals(domain_name("www.xakep.ru"), "xakep")
# test.assert_equals(domain_name("https://youtube.com"), "youtube")