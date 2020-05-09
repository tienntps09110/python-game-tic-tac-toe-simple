from random import*
from modules.core.core import*
def main():
    boxs = [
        i + 1 for i in range (10)
    ]
    # boxs = [
    #     'O','X','O',
    #     'O','X','X',
    #     'X','O','O'
    # ]
    core = Core(boxs)
    core.draw()
    
    while True:
        check_bot = 0
        # YOU PLAY
        choose_box = input('Choose box: ')
        if choose_box.isdigit() and 1 <= int(choose_box) <= 9:
            number = int(choose_box)
            if Core.isInt(boxs[number - 1]):
                boxs[number - 1] = 'O'
                core = Core(boxs)
                Core.clearConsole()
                core.draw()
                check_bot = 1

        core = Core(boxs)
        if core.checkWin('O'):
            print ('Result: you win')
            break
            
        if Core.checkYouBotPoint(boxs):
            print('Result: you - bot draw')
            break

        core = Core(boxs)
        Core.clearConsole()
        core.draw()
        
        # BOT PLAY
        choose_box = randint(1,9)
        if check_bot == 1:
            number = int(choose_box)

            while True:
                number = randint(1,9)
                if Core.isInt(boxs[number - 1]):
                    boxs[number - 1] = 'X'
                    core = Core(boxs)
                    Core.clearConsole()
                    core.draw()
                    break

        core = Core(boxs)
        if core.checkWin('X'):
            print ('Result: bot win')
            break
        if Core.checkYouBotPoint(boxs):
            print('Result: you - bot draw')
            break
        core = Core(boxs)
        Core.clearConsole()
        core.draw()
main()