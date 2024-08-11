```python

# works fucking flawlessly!!!!
# test.py
# for confirmation

    # button forward/backward
    self.nextBtn.clicked.connect(self.next_page)    
    self.prevBtn.clicked.connect(self.prev_page)
    
    # action forward/backward
    # self.actionPrevious.triggered.connect(self.prev_page)
    # self.actionNext.triggered.connect(self.next_page)
    self.homeBtn.clicked.connect(self.go_home)

def next_page(self):
    current_index = self.stackedWidget.currentIndex()
    next_index = (current_index + 1) % self.stackedWidget.count()
    self.stackedWidget.setCurrentIndex(next_index)

def prev_page(self):
    current_index = self.stackedWidget.currentIndex()
    prev_index = (current_index - 1) % self.stackedWidget.count()
    self.stackedWidget.setCurrentIndex(prev_index)
    
def go_home(self):
    self.stackedWidget.setCurrentIndex(0)

```
