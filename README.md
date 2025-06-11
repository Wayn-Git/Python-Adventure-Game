# 🌲 Forest Adventure

A classic text-based adventure game written in Python where you explore a mysterious forest, battle enemies, collect treasures, and complete an epic quest!

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 🎯 Game Overview

You are an adventurer on a quest to find legendary treasures hidden deep within a mysterious forest. Navigate through different locations, collect items, fight enemies, and uncover the secrets that await you!

### 🏆 Objective
Find both the **Golden Amulet** and **Ancient Sword** to complete your quest and win the game!

## ✨ Features

- **Immersive Text-Based Gameplay** - Rich descriptions and atmospheric storytelling
- **Interactive World** - Multiple interconnected locations to explore
- **Inventory System** - Collect and manage items throughout your journey
- **Combat System** - Fight dangerous creatures with strategic gameplay
- **Health Management** - Monitor your health as you face challenges
- **Dynamic Exploration** - Locations reveal new details on first visit

## 🗺️ Game World

### Locations
- **Forest Entrance** - Your starting point
- **Forest Path** - A winding trail through dense trees
- **Clearing** - A peaceful sunlit area
- **Cave Entrance** - Gateway to underground mysteries
- **Cave Interior** - Dark depths filled with danger
- **Treasure Room** - The ultimate destination

### Items to Discover
- 🗝️ **Shiny Key** - Might unlock something important
- 🗺️ **Old Map** - Navigate with ancient wisdom
- 🔦 **Torch** - Light up the darkness
- 🏺 **Golden Amulet** - One of the legendary treasures
- ⚔️ **Ancient Sword** - Powerful weapon and quest item

### Enemies
- 🐺 **Wolf** - A fierce predator in the forest
- 🦇 **Bat** - Cave-dwelling creature

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No external dependencies required!

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/forest-adventure.git
cd forest-adventure
```

2. Run the game:
```bash
python forest_adventure.py
```

## 🎮 How to Play

### Commands
- **Movement**: `north`, `south`, `east`, `west`, `in`, `out`, `deeper`, `back`
- **Exploration**: `look` - Examine your surroundings
- **Items**: `get [item]` or `take [item]` - Pick up items
- **Inventory**: `inventory` or `inv` - Check what you're carrying
- **Combat**: `fight [enemy]` or `attack [enemy]` - Battle creatures
- **Help**: `help` - Display all available commands
- **Exit**: `quit` - End the game

### Gameplay Tips
- Explore thoroughly - items and enemies are scattered throughout the world
- The Ancient Sword makes combat much more effective
- Keep an eye on your health during battles
- Some locations may have multiple items to collect
- Type commands exactly as shown (case doesn't matter)

### Sample Gameplay
```
What is your name, adventurer? Hero

========================================
Location: Forest Entrance
========================================
You stand at the entrance to a dark, mysterious forest.
You can go: north

What do you want to do? north
You moved.

You are at the Forest Path.
You can go: south, east
There is a wolf here!

What do you want to do? fight wolf
You fought the wolf but took 15 damage! Health: 85
```

## 🏗️ Code Structure

### Classes
- **Player**: Manages player state (name, inventory, health, location)
- **Location**: Represents game locations with descriptions, connections, items, and enemies

### Key Functions
- `create_world()`: Initializes the game world and connections
- `display_location()`: Shows location information to the player
- `handle_command()`: Processes player input and executes actions
- `main()`: Game loop and initialization

## 🤝 Contributing

Contributions are welcome! Here are some ideas for enhancements:

- Add more locations and expand the world
- Implement a save/load game feature
- Add more enemy types and combat mechanics
- Create more complex puzzles and quests
- Add sound effects or ASCII art
- Implement character stats and leveling

### How to Contribute
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments

- Inspired by classic text-based adventure games like Zork and Adventure
- Built as a learning project to demonstrate Python game development concepts
- Perfect for beginners learning Python programming

---

*Happy adventuring! 🌲⚔️*
