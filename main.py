from map import *

mapDet = {}
items = ["Test1", "Test2"]
map = gameMap(10, 40, 4, 2, mapDet, items)

while True:
    map.draw()
    print('''\n
w - up, a - left, s - down, d - right.

x - attack, i - inventory, q - quit.
          ''')
    print("\nItem: " + map.item)
    map.action(input("\nAction: ").lower())
