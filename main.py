import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.current_location = None

    def add_item(self, item):
        self.inventory.append(item)
        print(f"You picked up: {item}")

    def has_item(self, item_name):
        return item_name in self.inventory

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}  # direction: location_name
        self.items = []
        self.enemies = []
        self.visited = False

def create_world():
    # Create locations
    locations = {
        "forest_entrance": Location("Forest Entrance", 
                                  "You stand at the entrance to a dark, mysterious forest."),
        "forest_path": Location("Forest Path", 
                              "A narrow path winds through the dense trees."),
        "clearing": Location("Clearing", 
                           "A small clearing with sunlight streaming through the canopy."),
        "cave_entrance": Location("Cave Entrance", 
                                "A dark cave mouth opens before you."),
        "cave_interior": Location("Cave Interior", 
                                "The dark, damp interior of the cave."),
        "treasure_room": Location("Treasure Room", 
                                "A small chamber with a gleaming treasure chest.")
    }
    
    # Set connections
    locations["forest_entrance"].connections = {"north": "forest_path"}
    locations["forest_path"].connections = {"south": "forest_entrance", "east": "clearing"}
    locations["clearing"].connections = {"west": "forest_path", "north": "cave_entrance"}
    locations["cave_entrance"].connections = {"south": "clearing", "in": "cave_interior"}
    locations["cave_interior"].connections = {"out": "cave_entrance", "deeper": "treasure_room"}
    locations["treasure_room"].connections = {"back": "cave_interior"}
    
    # Add items
    locations["clearing"].items = ["shiny key", "old map"]
    locations["cave_entrance"].items = ["torch"]
    locations["treasure_room"].items = ["golden amulet", "ancient sword"]
    
    # Add enemies
    locations["forest_path"].enemies = ["wolf"]
    locations["cave_interior"].enemies = ["bat"]
    
    return locations

def display_location(player, locations):
    loc = player.current_location
    location = locations[loc]
    
    if not location.visited:
        print("\n" + "=" * 40)
        print(f"Location: {location.name}")
        print("=" * 40)
        print(f"{location.description}")
        location.visited = True
    else:
        print(f"\nYou are at the {location.name}.")
    
    # Show available directions
    directions = list(location.connections.keys())
    if directions:
        print("You can go: " + ", ".join(directions))
    
    # Show items
    if location.items:
        print("You see: " + ", ".join(location.items))
    
    # Show enemies
    if location.enemies:
        for enemy in location.enemies:
            print(f"There is a {enemy} here!")

def handle_command(command, player, locations):
    words = command.lower().split()
    
    if not words:
        return "Please enter a command."
    
    action = words[0]
    
    # Movement
    if action in locations[player.current_location].connections:
        player.current_location = locations[player.current_location].connections[action]
        return "You moved."
    
    # Look around
    if action == "look":
        return "look"
    
    # Get item
    if action == "get" or action == "take":
        if len(words) > 1:
            item_name = " ".join(words[1:])
            current_loc = locations[player.current_location]
            if item_name in current_loc.items:
                player.add_item(item_name)
                current_loc.items.remove(item_name)
                return f"You picked up the {item_name}."
            else:
                return f"There's no {item_name} here."
        else:
            return "What do you want to get?"
    
    # Check inventory
    if action == "inventory" or action == "inv":
        if player.inventory:
            return "You are carrying: " + ", ".join(player.inventory)
        else:
            return "Your inventory is empty."
    
    # Fight enemy
    if action == "fight" or action == "attack":
        if len(words) > 1:
            enemy_name = " ".join(words[1:])
            current_loc = locations[player.current_location]
            if enemy_name in current_loc.enemies:
                if "ancient sword" in player.inventory:
                    current_loc.enemies.remove(enemy_name)
                    return f"You defeated the {enemy_name} with your ancient sword!"
                else:
                    damage = random.randint(10, 20)
                    player.health -= damage
                    return f"You fought the {enemy_name} but took {damage} damage! Health: {player.health}"
            else:
                return f"There's no {enemy_name} here."
        else:
            return "What do you want to fight?"
    
    # Help
    if action == "help":
        return """Available commands:
- north, south, east, west, in, out, etc. (move in that direction)
- look (look around)
- get/take [item] (pick up an item)
- inventory/inv (check what you're carrying)
- fight/attack [enemy] (fight an enemy)
- help (show this help)
- quit (exit the game)"""
    
    return "I don't understand that command. Type 'help' for a list of commands."

def main():
    print("=" * 40)
    print("FOREST ADVENTURE")
    print("=" * 40)
    print("You are on a quest to find a legendary treasure hidden in the forest.")
    print("Type 'help' for commands.")
    
    player_name = input("\nWhat is your name, adventurer? ")
    player = Player(player_name)
    
    locations = create_world()
    player.current_location = "forest_entrance"
    
    display_location(player, locations)
    
    while True:
        if player.health <= 0:
            print("\nYou have been defeated! Game over.")
            break
            
        if "golden amulet" in player.inventory and "ancient sword" in player.inventory:
            print("\nCongratulations! You found the legendary treasures and completed your quest!")
            break
            
        command = input("\nWhat do you want to do? ")
        
        if command.lower() == "quit":
            print("Thanks for playing!")
            break
            
        result = handle_command(command, player, locations)
        
        if result == "look":
            display_location(player, locations)
        else:
            print(result)

if __name__ == "__main__":
    main()