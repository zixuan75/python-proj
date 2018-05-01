# PROJECT 1.2 (Beta)
#
# Please find our information by running __init__
# using Python at the help folder. PROJECT is written
# in Python. The pre-release version is released at
# 28 April 2018.
#
# Every Python file on the initialization Python
# package has a class, so this file has a class, and
# it is called initClass.

class initClass:
    @classmethod
    def __init__(self, methodNumber):
        self.methodNumber=int(methodNumber)

    @classmethod
    def sendMethodNumber(self):
        self.number=self.methodNumber
        return self.number
