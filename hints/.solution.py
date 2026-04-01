# the solution for the demo I gave was diDy0uBr4kE!t?
# this is an auto solver for the cipher
import ast
from time import sleep


class cipherText:
    key = []
    cipherText = []
    solved = []

    def __init__(self, cipherText, keyList):
        self.cipherText = cipherText
        self.key = keyList
        self.solved = cipherText

    def knownCheck(self, character, index):
        for k in self.key:
            if ord(character) * k == self.cipherText[index]:
                return k
        return 0

    def forceCharacterOut(self, index, keyGuessIndex):
        y = self.cipherText[index]
        key = self.key[keyGuessIndex]
        if y % key != 0:
            return None
        ord_char = y // key
        if 0 <= ord_char <= 255:
            return chr(ord_char)
        return None

    def concencusCheck(self, character, index):
        target = self.cipherText[index]
        c_ord = ord(character)
        for k in self.key:
            if k * c_ord == target:
                return True
        return False

    def revert(self, cipherIndex, keyValue, character):
        if keyValue == 0:
            print("WARNING REVERT PREVENTED ON NULL")
            return
        self.solved[cipherIndex] = character
        self.key.remove(keyValue)

    def solveFormat(self):
        back = len(self.cipherText) - 1
        self.revert(0, self.knownCheck("F", 0), "F")
        self.revert(1, self.knownCheck("L", 1), "L")
        self.revert(2, self.knownCheck("A", 2), "A")
        self.revert(3, self.knownCheck("G", 3), "G")
        self.revert(4, self.knownCheck("{", 4), "{")
        self.revert(back, self.knownCheck("}", back), "}")

    def stringSolved(self):
        stringOut = ""
        for i in self.solved:
            if not isinstance(i, (int, float)):
                stringOut = stringOut + i
            else:
                if isinstance(i, int):
                    formatted_num = f"-{i:03d}-"
                else:
                    formatted_num = f"-{int(i):03d}-"
                stringOut = stringOut + formatted_num
        return stringOut

    def doneCheck(self):
        return len(self.stringSolved()) == len(self.cipherText)

    def getKeyListSize(self):
        return len(self.key)


def loadFile(filepath):
    result = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # ensure line is not empty
                result.append(ast.literal_eval(line))
    return result


def generatKeyList(ciphertext):
    return list(range(3, (len(ciphertext) + 1) * 3, 3))


def bulkResolve(testList, character, index):
    for i in testList:
        key_val = i.knownCheck(character, index)
        i.revert(index, key_val, character)


cipherTextRaw = loadFile("./../crackme.txt")
keyList = generatKeyList(cipherTextRaw[0])
texts = []

for i in cipherTextRaw:
    texts.append(cipherText(i, keyList[:]))

for i in texts:
    i.solveFormat()

print(texts[0].stringSolved())
curIndex = 5
working = False
while not texts[0].doneCheck():
    failed = True
    for i in range(texts[0].getKeyListSize()):
        guess = texts[0].forceCharacterOut(curIndex, i)
        if guess is not None:
            working = True
            for x in texts:
                if not x.concencusCheck(guess, curIndex):
                    working = False
            if working:
                sleep(0.3)
                bulkResolve(texts, guess, curIndex)
                print(texts[0].stringSolved())
                curIndex += 1
                failed = False
                break
    if failed:
        print("Failed")
        break
