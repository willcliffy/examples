"""
EXAMPLE - picking something up off of a game map

Expected output:
$ python3 example_inventory.py
SUCCESS: Found sword in players inventory! {'x': 2, 'y': 2, 'inventory': [{'x': 2, 'y': 2}]}
SUCCESS: No sword on the map! [[None, None, None], [None, None, None], [None, None, None]]
"""

# Helper function that will pick up an item underneath a player, if there is one.
# I put this in a function because in a real game this would be reused many places.
def pick_up_item(map, player):
    if map[player["x"]][player["y"]]: # Does the tile under the player have anything on it? if so:
        player["inventory"].append(map[player["x"]][player["y"]]) # put item in player's inventory
        map[player["x"]][player["y"]] = None # remove item from the map

# there must something on the map to be picked up:
sword = {
    "x": 2,
    "y": 2,
}

# there must be a map:
map = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

# there must be some player that can carry things:
player = {
    "x": 0,
    "y": 0,
    "inventory": [],
}

# place the sword on the map:
map[sword["x"]][sword["y"]] = sword

# move the player to the sword:
player["x"] = sword["x"]
player["y"] = sword["y"]

# have the player pick up the item
pick_up_item(map, player)

# Check that the player now has the sword
if sword not in player["inventory"]:
    print("FAILURE: Could not find sword in players inventory.")
    exit()
print("SUCCESS: Found sword in players inventory!", player)

# Check that the map doesn't have any items
for tile_row in map:
    if sword in tile_row:
        print("FAILURE: Found sword on the map.")
        exit()
print("SUCCESS: No sword on the map!", map)
