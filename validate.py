import re
class Form:
    def __init__(self,data):
        self.data = data
    def is_complete(self):
        isComplete = True 
        for data in self.data:
            if data[1] == '':
                isComplete = False
        return isComplete
