from map import *

mapDet = {}

map = gameMap(5, 20, 4, 2, mapDet)

while True:
    map.draw()
    print('''\n
w - up, a - left, s - down, d - right.

x - attack, i - inventory, q - quit.
          ''')
    map.move(input("\nAction: ").lower())
