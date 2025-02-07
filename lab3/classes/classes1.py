class StringHandler:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Введи строку: ")

    def printString(self):
        print(self.s.upper())

handler = StringHandler()
handler.getString()
handler.printString()