class WebPage:
    def __init__(self, homepage: str):
        self.val = homepage
        self.forward = None
        self.backward = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homePage = WebPage(homepage)
        self.currentPage = self.homePage

    def visit(self, url: str) -> None:
        newPage = WebPage(url)
        self.currentPage.forward = newPage
        newPage.backward = self.currentPage
        self.currentPage = newPage
        # print("**VISIT**",self.currentPage.forward.val)

    def back(self, steps: int) -> str:
        i = 1
        while self.currentPage.backward:
            self.currentPage = self.currentPage.backward
            if i == steps:
                # print("**BACK**",self.currentPage.forward.val)
                return self.currentPage.val
            i += 1
            
        return self.currentPage.val   

    def forward(self, steps: int) -> str:
        i = 1
        while self.currentPage.forward:
            self.currentPage = self.currentPage.forward
            if i == steps:
                # print("**FRONT**",self.currentPage.forward.val)
                return self.currentPage.val
            i += 1
            
        return self.currentPage.val 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)