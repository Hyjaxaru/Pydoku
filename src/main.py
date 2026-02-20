import flet as ft
import random

class Cell:
    def __init__(self, expectedValue=0, value=0, isGiven=False, isSolved=False): # Creates a cell object to store information for
        self.value = value
        self.isGiven = isGiven
        self.expectedValue = expectedValue
        self.isSolved = isSolved


    def getInfo(self):
        return self.value, self.isGiven, self.expectedValue, self.isSolved


class PydokuGame:
    def __init__(self):
        self.board = [[Cell(value=random.randint(1,9)) for _ in range(9)] for _ in range(9)]
    ''' for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                print(f"x: {x}, y: {y}, value: {cell.value}")
                pass'''
    
    def getCell(self,x,y):
        cell = self.board[y][x]
        return cell

    def getColumn(self,y):
        return self.board[y]
    
    def getRow(self,x):
        rows = []
        for y, row in enumerate(self.board):
            cell = row[x]
            rows.append(cell)
        return rows
        
    def getBoard(self):
        return self.board

    
    def getBox(self, x, y): # Gets the 3x3 box of the given cell -- i can NOT figure this out for the life of me
        start = 0
        end = 2
        box = []
        for y in range(3):
            for x in range(3):
                box.append(self.getCell(y+start,x+end))
                print(f'y={y+start}, x={x+end}, value={cell.value}')


    def canWriteNumberToCell(x, y, value) -> True:
        pass

def createGame(): # Create the game and render the board
    game = PydokuGame()
    board = []
    for i in range(9): # Get all columns
        column = game.getColumn(i)
        display = []
        for cell in column:
            display.append(
                ft.Container(
                    content=ft.Text(f'{cell.value}'),
                    margin=0,
                    padding=0,
                    width=25,
                    height=25,
                    border=ft.Border.all(1,ft.Colors.DEEP_PURPLE_ACCENT)
                )
            )
        board.append(
            ft.Column(
                width=225,
                height=225,
                controls=display)
        )
    
    return game,board


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.title = 'Pydoku'
    game, board = createGame()
    for column in board:
        page.add(column)



#ft.run(main)


if __name__ == "__main__":
    test = PydokuGame()
    print('-------------')
    for cell in test.getColumn(0):
        print(cell.getInfo())
    #print(test.getColumn(0))
    print('-------------')
    print(test.getCell(1,1))
    print('------')
    for cell in test.getRow(0):
       print(cell.getInfo())
    print('--------')
    test.getBox(0,0)
    #for cell in test.getBox(0,0):
    #    print(cell.getInfo())