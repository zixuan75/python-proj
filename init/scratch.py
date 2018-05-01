# PROJECT 1.2 (Beta)
#
# Please find our information by running __init__
# using Python at the help folder. PROJECT is written
# in Python. The pre-release version is released at
# 28 April 2018.
#
# Every Python file on the initialization Python
# package has a class, so this file has a class, and
# it is called requestClass.

import scratch_init
class requestClass:
    @classmethod
    def __init__(self, mainClassName):
        self.mainClassName=mainClassName
        methodNumber=scratch_init.initClass("5").sendMethodNumber()
        self.methodNumber=methodNumber

        print("Method number: "+str(self.methodNumber))

    @classmethod
    def sendRequest(self):
        self.requests=1

    @classmethod
    def getRequests(self):
        return self.requests

