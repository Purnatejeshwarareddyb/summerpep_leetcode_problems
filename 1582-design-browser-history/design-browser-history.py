
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr_index = 0
        self.limit = 0  # Furthest accessible index in the history list

    def visit(self, url: str) -> None:
        self.curr_index += 1
        
        # Overwrite if we have space, otherwise append
        if self.curr_index < len(self.history):
            self.history[self.curr_index] = url
        else:
            self.history.append(url)
            
        # Update the limit because new forward history is cleared
        self.limit = self.curr_index

    def back(self, steps: int) -> str:
        self.curr_index = max(0, self.curr_index - steps)
        return self.history[self.curr_index]

    def forward(self, steps: int) -> str:
        self.curr_index = min(self.limit, self.curr_index + steps)
        return self.history[self.curr_index]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)