from tests.DummyTests import *
from tests.WebSiteTest import WebSiteTest
from test.DNStest import DNStest


tests = [
    DummyPassTest("A dummy test that will pass"),
    DummyFailTest("A dummy test that will fail"),
    DummyErrorTest("A dummy test that will raise an exception"),
    WebSiteTest("Check we can get to google", site="www.google.com"),
    WebSiteTest("Check we can get to cisco", site="www.cisco.com"),
    WebSiteTest("Check we can get to microsoft", site="www.microsoft.com"),
    DNStest('makes sure DNS works for youtubes load balancer', 'www.youtube.com', ['216.58.220.142']),
    DNStest('makes sure DNS works for website', 'www.dropbox.com',  ['108.160.172.206', '108.160.172.238'])]

passed = 0
for test in tests:
    try:
        if test.run():
            print(test.get_name() + " ... passed")
            passed += 1
        else:
            print(test.get_name() + " ... failed")
    except: #catch all exceptions
        print(test.get_name() + " ... error")

print("total passed " + str(passed) + "/" + str(len(tests)))
