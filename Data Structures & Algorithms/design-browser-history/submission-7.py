class WebPage:
    def __init__(self, homepage: str):
        self.val = homepage
        self.forward = None
        self.backward = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homePage = WebPage(homepage)
        self.currentPage = WebPage("")
        self.currentPage.forward = self.homePage
        self.currentPage.backward = self.homePage

    def visit(self, url: str) -> None:
        newPage = WebPage(url)
        self.currentPage.forward.forward = newPage
        newPage.backward = self.currentPage.forward
        self.currentPage.backward =  self.currentPage.forward
        self.currentPage.forward = newPage
        print("**VISIT**",self.currentPage.forward.val)

    def back(self, steps: int) -> str:
        i = 1
        while self.currentPage.backward:
            self.currentPage.forward = self.currentPage.backward
            self.currentPage.backward = self.currentPage.forward.backward
            if i == steps:
                print("**BACK**",self.currentPage.forward.val)
                return self.currentPage.forward.val
            i += 1
            
        return self.currentPage.forward.val   

    def forward(self, steps: int) -> str:
        i = 1
        while self.currentPage.forward.forward:
            self.currentPage.backward = self.currentPage.forward
            self.currentPage.forward = self.currentPage.forward.forward
            if i == steps:
                print("**FRONT**",self.currentPage.forward.val)
                return self.currentPage.forward.val
            i += 1
            
        return self.currentPage.forward.val 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)