# PROJECT 1.2 (Beta)
#
# Please find our information by running __init__
# using Python at the help folder. PROJECT is written
# in Python. The pre-release version is released at
# 28 April 2018.

class appClass:
    @classmethod
    def __init__(self, val, val2):
        self.val = val
        self.val2 = val2

    @classmethod
    def findVal(self):
        self.findedVal="\t1: "+self.val+"\n\t2: "+self.val2
        return self.findedVal