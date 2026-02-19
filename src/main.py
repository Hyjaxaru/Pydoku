import flet as ft

class Cell:
    def __init__(self, expectedValue=-1, value=0, isGiven=False):
        self.value = value
        self.isGiven = isGiven
        self.expectedValue = expectedValue


    def getInfo(self):
        return self.value, self.is_given


class PydokuGame:
    def __init__(self):
        self.board = [[Cell() for _ in range(9)] for _ in range(9)]
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                print(f"x: {x}, y: {y}, value: {cell.value}")
    
    def canWriteNumberToCell(x, y, value) -> True:
        pass


def main(page: ft.Page):
    column = ft.Column(width=220,height=220,)
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )



#ft.run(main)

if __name__ == "__main__":
    test = PydokuGame()