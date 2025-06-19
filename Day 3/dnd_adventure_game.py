import random
from typing import List, Dict

class Character:
    def __init__(self, name: str, character_class: str):
        self.name = name
        self.character_class = character_class
        self.health = self._set_initial_health()
        self.is_alive = True

    def _set_initial_health(self) -> int:
        health_points = {
            "warrior": 15,
            "mage": 10,
            "rogue": 12,
            "cleric": 12
        }
        return health_points.get(self.character_class.lower(), 10)

    def roll_dice(self, sides: int = 20) -> int:
        return random.randint(1, sides)

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            self.health = 0

class DungeonAdventure:
    def __init__(self):
        self.players: List[Character] = []
        self.current_scene = "start"

    def add_player(self):
        print("\n=== Create New Character ===")
        name = input("Enter character name: ").strip()
        print("\nAvailable Classes:")
        print("1. Warrior (High HP, Good at Combat)")
        print("2. Mage (Low HP, Powerful Spells)")
        print("3. Rogue (Medium HP, Good at Stealth)")
        print("4. Cleric (Medium HP, Healing Abilities)")
        
        while True:
            class_choice = input("Choose your class (1-4): ").strip()
            class_map = {"1": "warrior", "2": "mage", "3": "rogue", "4": "cleric"}
            if class_choice in class_map:
                character_class = class_map[class_choice]
                break
            print("Invalid choice. Please choose 1-4.")

        player = Character(name, character_class)
        self.players.append(player)
        print(f"\nWelcome, {name} the {character_class.title()}!")

    def check_party_status(self) -> bool:
        alive_players = [p for p in self.players if p.is_alive]
        return len(alive_players) > 0

    def display_status(self):
        print("\n=== Party Status ===")
        for player in self.players:
            print(f"{player.name} ({player.character_class.title()}) - HP: {player.health}")

    def group_skill_check(self, difficulty: int) -> bool:
        print("\nRolling for the group...")
        success_count = 0
        for player in self.players:
            if not player.is_alive:
                continue
            roll = player.roll_dice()
            print(f"{player.name} rolled: {roll}")
            if roll >= difficulty:
                success_count += 1
        return success_count >= len([p for p in self.players if p.is_alive]) / 2

    def combat_encounter(self, enemy_name: str, enemy_hp: int, enemy_damage: int):
        print(f"\n=== Combat with {enemy_name} ===")
        while enemy_hp > 0:
            self.display_status()
            print(f"\n{enemy_name} HP: {enemy_hp}")
            
            # Players' turn
            for player in self.players:
                if not player.is_alive:
                    continue
                roll = player.roll_dice()
                damage = max(roll // 3, 1)  # Ensure at least 1 damage
                enemy_hp -= damage
                print(f"{player.name} attacks for {damage} damage!")
                
                if enemy_hp <= 0:
                    print(f"\n{enemy_name} has been defeated!")
                    return True

            # Enemy's turn
            for player in self.players:
                if not player.is_alive:
                    continue
                player.take_damage(enemy_damage)
                print(f"\n{enemy_name} attacks {player.name} for {enemy_damage} damage!")
                
                if not self.check_party_status():
                    print("\nThe entire party has fallen!")
                    return False
        
        return True

    def play_game(self):
        print("""
    ╔═══════════════════════════════════════════╗
    ║          The Dungeon of Shadows          ║
    ╚═══════════════════════════════════════════╝
    """)
        
        # Get number of players
        while True:
            try:
                num_players = int(input("Enter the number of players (1-4): "))
                if 1 <= num_players <= 4:
                    break
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        # Create characters for each player
        for i in range(num_players):
            print(f"\nPlayer {i+1}")
            self.add_player()

        print("\nYour party stands at the entrance of an ancient dungeon...")
        
        # Main game loop
        while self.current_scene != "end" and self.check_party_status():
            if self.current_scene == "start":
                print("\nYou encounter a fork in the path.")
                choice = input("Do you take the (1) mysterious portal or (2) dark corridor? ").strip()
                
                if choice == "1":
                    print("\nYour party approaches the swirling portal...")
                    if self.group_skill_check(12):
                        print("You successfully navigate through the portal!")
                        self.current_scene = "treasure_room"
                    else:
                        print("The portal's magic damages your party!")
                        for player in self.players:
                            player.take_damage(5)
                        self.current_scene = "monster_room"
                else:
                    self.current_scene = "monster_room"

            elif self.current_scene == "monster_room":
                print("\nA fearsome Shadow Dragon appears!")
                if self.combat_encounter("Shadow Dragon", 30, 4):
                    self.current_scene = "treasure_room"
                else:
                    self.current_scene = "end"

            elif self.current_scene == "treasure_room":
                print("\nYou've reached the legendary treasure room!")
                choice = input("Do you (1) carefully inspect for traps or (2) rush to grab the treasure? ").strip()
                
                if choice == "1":
                    if self.group_skill_check(15):
                        print("\nCongratulations! You've successfully claimed the treasure and completed your quest!")
                    else:
                        print("\nDespite your caution, you trigger a trap!")
                        for player in self.players:
                            player.take_damage(3)
                else:
                    print("\nYou trigger multiple traps!")
                    for player in self.players:
                        player.take_damage(8)
                
                self.current_scene = "end"

        # Game end
        self.display_status()
        if self.check_party_status():
            alive_count = len([p for p in self.players if p.is_alive])
            print(f"\nQuest completed! {alive_count} heroes survived the dungeon!")
        else:
            print("\nGame Over - The entire party has fallen!")

if __name__ == "__main__":
    game = DungeonAdventure()
    game.play_game()
