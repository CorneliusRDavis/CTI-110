import os
import random

def prompt():
    print("""
			This is  Lucid Dream!

You must collect all six items 🤷🏿‍♂️  before confronting the boss.

Commands:
    'go {direction}'   -> move (north, south, east, west)
    'get {item}'       -> collect nearby item
    'fight'            -> battle the boss (once all items are collected)
    'exit'             -> quit the game
""")
    input("Press any key to begin your journey...")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_health(health):
    bar_length = 20
    filled = int((health / 100) * bar_length)
    empty = bar_length - filled
    return f"[{'🫶' * filled}{'-' * empty}] {health}/100 HP"

def display_map(current):
    room_symbols = {
        'Church': 'Church',
        'Empty Mall': 'Empty Mall',
        'Shoe House': 'Shoe House',
        'Floating Car': 'Floating Car',
        'Truck Yard': 'Truck Yard',
        'Abandoned House': 'Abandoned House',
        'Forest': 'Forest',
        'Treehouse': 'Treehouse'    }
    for room in room_symbols:
        if room == current:
            room_symbols[room] = f'[*{room}*]'
    print("\n" + "-" * 60)
    print(f"               {room_symbols['Church']}")
    print(f"                    |")
    print(f"{room_symbols['Abandoned House']} -- {room_symbols['Truck Yard']} -- {room_symbols['Empty Mall']} -- {room_symbols['Shoe House']} -- {room_symbols['Floating Car']}")
    print(f"                                      |")
    print(f"                               {room_symbols['Forest']}")
    print(f"                                      |")
    print(f"                             {room_symbols['Treehouse']}")
    print("-" * 60 + "\n")

def battle(player_hp, current_room_name):
    room = rooms[current_room_name]
    boss_hp = room['enemy']["health"]
    boss_name = room['enemy']["name"]
    print(f"\n You engage in battle with the {boss_name}! \n")

    while player_hp > 0 and boss_hp > 0:
        input("Press Enter to attack...")
        player_attack = random.randint(10, 25)
        boss_attack = random.randint(5, 20)

        boss_hp -= player_attack
        player_hp -= boss_attack

        print(f"You hit the {boss_name} for {player_attack} damage!")
        print(f"{boss_name} hits you back for {boss_attack} damage!")
        print(f"Your Health: {display_health(max(player_hp, 0))}")
        print(f"{boss_name}'s Health: {display_health(max(boss_hp, 0))}\n")

    if player_hp > 0:
        print(f"\n You defeated the {boss_name} and completed your quest!")
    else:
        print(f"\n You were defeated by the {boss_name}. Better luck next time!")

    return player_hp


rooms = {
    'Empty Mall': {'North': 'Church', 'South': 'Truck Yard', 'East': 'Shoe House' ,'enemy': {"name":"janitor" ,"health":50,"weapon":"broom", "max_damage":20 }},
    'Church': {'South': 'Empty Mall', 'Item': 'Crystal','enemy': {"name":"tanitor" ,"health":50,"weapon":"broom", "max_damage":20 }},
    'Truck Yard': {'North': 'Empty Mall', 'East': 'Abandoned House', 'Item': 'Staff','enemy': {"name":"tanitor" ,"health":50,"weapon":"broom", "max_damage":20 }},
    'Shoe House': {'West': 'Empty Mall', 'North': 'Forest', 'East': 'Floating Car', 'Item': 'Altoids','enemy': {"name":"tanitor" ,"health":50,"weapon":"broom", "max_damage":20 }},
    'Forest': {'South': 'Shoe House', 'East': 'Treehouse', 'Item': 'Fig','enemy': {"name":"tanitor" ,"health":50,"weapon":"broom", "max_damage":20 }},
    'Treehouse': {'West': 'Forest', 'Item': 'Robe','enemy': {"name":"tanitor" ,"health":50,"weapon":"broom", "max_damage":20 }},
    'Abandoned House': {'West': 'Truck Yard', 'Item': 'Elderberry','enemy': {"name":"tanitor" ,"health":50,"weapon":"broom", "max_damage":20 }},
    'Floating Car': {'West': 'Shoe House', 'Boss': 'Disgruntled Janitor','enemy': {"name":"tanitor" ,"health":50,"weapon":"broom", "max_damage":20 }}
}

inventory = []
current_room = 'Empty Mall'
msg = ""
player_hp = 100

clear()
prompt()

while True:
    clear()
    display_map(current_room)
    print(f" you are in the {current_room}")
    print(f" inventory: {inventory}")
    print(f" health: {display_health(player_hp)}")
    print("-" * 30)


    enemy_name = rooms[current_room]['enemy']['name']
    if msg:
        print(msg + "\n")
    msg = ""

    if "Item" in rooms[current_room]:
        nearby_item = rooms[current_room]["Item"]
        if nearby_item not in inventory:
            article = 'an' if nearby_item[0].lower() in 'aeiou' else 'a'
            print(f"You see {article} {nearby_item} here.")
            
    if 'enemy' in rooms[current_room]:
        if len(inventory) < 1:
            print(f"\n⚠️ you face {enemy_name}, but you're not ready!")
        else:
            print(f"\n {enemy_name} is here!")

    user_input = input("\nEnter your move: go,get,grab,fight").strip().lower().split()

    if not user_input:
        msg = "Please enter a command."
        continue

    action = user_input[0]
    target = ' '.join(user_input[1:]).title() if len(user_input) > 1 else ""

    if action == 'go':
        if target in rooms[current_room]:
            current_room = rooms[current_room][target]
            msg = f"You moved {target}."
        else:
            msg = "You can't go that way."

    elif action == 'get':
        if "Item" in rooms[current_room] and rooms[current_room]["Item"] == target:
            if target not in inventory:
                inventory.append(target)
                msg = f"You picked up {target}."
            else:
                msg = f"You already have {target}."
        else:
            msg = f"There's no {target} here."

    elif action == 'fight':
        if 'enemy' in rooms[current_room]:
            if len(inventory) >= 1:
                enemy_name = rooms[current_room]['enemy']['name']
                player_hp = battle(player_hp, current_room)
                break
            else:
                msg = f"You're not ready yet. Collect all 6 items first!"
        else:
            msg = "There's nothing to fight here."

    elif action == 'exit':
        print("You have Escaped! Goodbye.")
        break

    else:
        msg = "Invalid command. Try 'go', 'get', 'fight', or 'exit'."
