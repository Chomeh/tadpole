from tests.Test import Test
import http.client

class WebSiteTest(Test):
    def __init__(self, name, site):
        super(WebSiteTest, self).__init__(name)
        self.site = site


    def run(self):
        h = http.client.HTTPConnection(self.site)
        h.request("GET","/")
        return h.getresponse().code in [http.client.OK, http.client.FOUND]

