import sys

class LoopHandler:
    def __init__(self):
        self.heap = []

    def incrementLoop(self, pointer):
        self.heap.append(pointer)

    def decrementLoop(self):
        self.heap.pop()

    def currentLoop(self):
        return self.heap[-1]

    def isEmpty(self):
        return len(self.heap) == 0

class BrainfuckReader:

    def __init__(self):
        self.tablePointer = 0
        self.textPointer = 0
        self.table = [0] * 30000
        self.iterator = 0
        self.tableChars = []
        self.handler = LoopHandler()

    def increment(self):
        if(self.table[self.tablePointer] == 255):
            self.table[self.tablePointer] = 0
        else:
            self.table[self.tablePointer] += 1

    def decrement(self):
        if(self.table[self.tablePointer] == 0):
            self.table[self.tablePointer] = 255
        else:
            self.table[self.tablePointer] -= 1

    def shiftPointerLeft(self):
        self.tablePointer -= 1

    def shiftPointerRight(self):
        self.tablePointer += 1

    def translate(self, text):
        self.textRead(text)
        message = ""
        for num in self.tableChars:
            message += chr(num)
        return message

    def returnNumbers(self):
        return self.tableChars
            
    def textRead(self, text):
        while self.textPointer < len(text):
            if text[self.textPointer] == ".":
                self.tableChars.append(self.table[self.tablePointer])
                self.textPointer += 1
            elif text[self.textPointer] == "+":
                self.increment()
                self.textPointer += 1
            elif text[self.textPointer] == "-":
                self.decrement()
                self.textPointer += 1
            elif text[self.textPointer] == "<":
                self.shiftPointerLeft()
                self.textPointer += 1
            elif text[self.textPointer] == ">":
                self.shiftPointerRight()
                self.textPointer += 1
            elif text[self.textPointer] == "[":
                self.handler.incrementLoop(self.textPointer)
                self.iterator = self.tablePointer
                self.textPointer += 1
                self.textRead(text)
            elif text[self.textPointer] == "]":
                if not self.table[self.iterator]:
                    self.handler.decrementLoop()
                    self.textPointer += 1
                    return
                else:
                    self.textPointer = self.handler.currentLoop()+1
            else:
                self.textPointer += 1


f = open(sys.argv[1], "r")

reader = BrainfuckReader()
result = reader.translate(f.read())

print(reader.returnNumbers())
print(result)

f.close()

f = open("results.txt", "w")
f.write(result)
f.close()
