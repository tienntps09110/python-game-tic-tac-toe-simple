import os
from modules.mess.mess import*

class Core:
    def __init__(self, boxs):
        self.boxs = boxs

    def clearConsole():
        # Clear console
        os.system('cls' if os.name=='nt' else 'clear')

    def draw(self):
        boxs = self.boxs
        data1 = [boxs[0],boxs[1],boxs[2]]
        data2 = [boxs[3],boxs[4],boxs[5]]
        data3 = [boxs[6],boxs[7],boxs[8]]

        Mess.box(data1)
        Mess.box(data2)
        Mess.box(data3)

    def checkWin(self, name_box):
        boxs = self.boxs
        win1 = [boxs[0], boxs[1], boxs[2]]
        win2 = [boxs[3], boxs[4], boxs[5]]
        win3 = [boxs[6], boxs[7], boxs[8]]
        win4 = [boxs[0], boxs[4], boxs[8]]
        win5 = [boxs[6], boxs[4], boxs[2]]
        win6 = [boxs[0], boxs[3], boxs[6]]
        win7 = [boxs[1], boxs[4], boxs[7]]
        win8 = [boxs[2], boxs[5], boxs[8]]
        if Core.checkBox(name_box, win1):
            return True
        elif Core.checkBox(name_box, win2):
            return True
        elif Core.checkBox(name_box, win3):
            return True
        elif Core.checkBox(name_box, win4):
            return True
        elif Core.checkBox(name_box, win5):
            return True
        elif Core.checkBox(name_box, win6):
            return True
        elif Core.checkBox(name_box, win7):
            return True
        elif Core.checkBox(name_box, win8):
            return True
        else:
            return False

    def checkBox(box, data):
        if data[0] == box and data[1] == box and data[2] == box:
            return True
        return False
        
    def isInt(value):
        if type(value) == int:
            return True
        return False
    
    def checkYouBot(box):
        if Core.isInt(box):
            return False
        return True
    
    def checkYouBotPoint(boxs):
        map_boxs = map(Core.checkYouBot, boxs)
        check_count = 0
        for box in list(map_boxs):
            if box:
                check_count +=1
        if check_count == 9:
            return True
        return False

