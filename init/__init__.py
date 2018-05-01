# PROJECT 1.2 (Beta)
#
# Please find our information by running __init__
# using Python at the help folder. PROJECT is written
# in Python. The pre-release version is released at
# 28 April 2018.
#
# This is the initialization file of the PROJECT,
# and this is the largest file on PROJECT. This file
# includes a class called MainClass.
#
# Every Python file on the initialization Python
# package has a class, so this file has a class, and
# it is called MainClass.

import scratch

print("\tPROJECT 1.2-alpha (Note: Please find our information by running __init__ using Python at the help folder.)\n")
mainClass = "MainClass"
finalMainClass = mainClass


def useMainClass(mainClassArgument):
    argument = "Class name: "+mainClassArgument
    return argument


finalStringArgument=useMainClass(finalMainClass)
print(finalStringArgument)


class MainClass:
    @classmethod
    def __init__(self, name, mainString):
        self.name = name
        self.mainString = mainString
        stringName = mainString
        self.useStringName(stringName, self.name)

    @classmethod
    def useStringName(self, initName, mainName):
        self.initName = initName
        finalName = self.getFinalName(mainName)
        self.finalName = finalName

    @classmethod
    def getFinalName(self, string):
        self.string = string
        return self.string

    @classmethod
    def useSelfString(self, mainClass, finalName):
        self.mainClass = mainClass
        return finalName

    @classmethod
    def useFinalMainName(self, finalMainName, finalClassBeginName, finalClassEndName):
        self.finalMainName = finalMainName
        self.finalClassBeginName = finalClassBeginName
        self.finalClassEndName = finalClassEndName
        print(self.finalClassBeginName)
        print('|Rates:\n|\t3.2 (FinalClass)\n|\t\t{ Developers: 5.2 }\n|\t4.5 (MainClass)\n|\t\t{ Developers: 7.3 }')
        print(self.finalClassEndName)
        self.finalClassNumber = 2

    @classmethod
    def getFinalClassNumber(self):
        return self.finalClassNumber


def callMainClass(finalName):
    finalString = "MainClass"
    className = finalString
    mainclass = MainClass("MainClass.name\n\?FinalName", finalString)
    print(mainclass.useSelfString(finalString, className) + " called here")
    mainclass.useFinalMainName(finalName, "FinalClass beginning {",
                               "FinalClass ended }")

    print("Final class numbers: " + str(mainclass.getFinalClassNumber()))


callMainClass("FinalName")
mainClassName = "MainClass"
# Please do not send a request more than one time
scratch.requestClass(mainClassName).sendRequest()
requests = scratch.requestClass(mainClassName).getRequests()
print("Requests: " + str(requests))
