import os
import keyboard
class gameMap:
    def __init__(self,
        mapHeight: int, mapWidth: int,
        playerY: int, playerX: int,
        mapDetails: dict,
        playerItems: list):


        self.Height = mapHeight
        self.Width = mapWidth
        self.PositionY = playerY
        self.PositionX = playerX
        self.items = playerItems
        self.item = "None"

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in range(self.Height):
            print("\n", end="")
            for col in range(self.Width):
                if (row == self.PositionY and col == self.PositionX):
                    print("█", end="")
                else:
                    print("#", end="")


    def move(self, direction: str):
        if "w" in direction:
            self.PositionY -= 1
        if "s" in direction:
            self.PositionY += 1
        if "a" in direction:
            self.PositionX -= 1
        if "d" in direction:
            self.PositionX += 1


        # Boundary conditions
        if self.PositionX < 0:
            self.PositionX = self.Width - 1
        elif self.PositionX >= self.Width:
            self.PositionX = 0

        if self.PositionY < 0:
            self.PositionY = self.Height - 1
        elif self.PositionY >= self.Height:
            self.PositionY = 0

    def inventory(self, items: list):
        print("Current Items: ")
        for i in range(len(items)):
            print(str(i + 1) + ". " + items[i])
        try:
            self.item: str = items[int(input("Select an item:"))-1]
        except:
            self.item = "None"


    def action(self, action):
        if ("w" in action) or ("a" in action) or ("s" in action) or ("d" in action):
            self.move(action)
        if "i" in action:
            self.inventory(self.items)
