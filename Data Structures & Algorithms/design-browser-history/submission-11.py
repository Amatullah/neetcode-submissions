class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.cur = 0
        self.n = 1
        

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur == len(self.urls):  # no forward history just normal appending
            self.urls.append(url)
            self.n += 1
        else:
            self.urls[self.cur] = url  # we are erasing forward history by just overwriting
            self.n = self.cur + 1
        

    def back(self, steps: int) -> str:
        self.cur = max(self.cur-steps, 0)
        return self.urls[self.cur]
        

    def forward(self, steps: int) -> str:
        self.cur = min(self.cur+steps, self.n-1)
        return self.urls[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)