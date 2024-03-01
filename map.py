import os
import keyboard
class gameMap:
    def __init__(self,
        mapHeight: int, mapWidth: int,
        playerY: int, playerX: int,
        mapDetails: dict):


        self.Height = mapHeight
        self.Width = mapWidth
        self.PositionY = playerY
        self.PositionX = playerX

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
        if direction == "w":
            self.PositionY -= 1
        elif direction == "s":
            self.PositionY += 1
        elif direction == "a":
            self.PositionX -= 1
        elif direction == "d":
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
