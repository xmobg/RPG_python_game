import random

player_hp = 100
player_attack = 15
player_level = 1
player_xp = 0
inventory = []

monter_hp = 60
monster_attack = 10
monster_xp_reward = 30

def show_stats():
    print(f"Player HP: {player_hp}")
    print(f"Attack: {player_attack}")
    print(f"Level: {player_level}")
    print(f"XP: {player_xp}")

def level_up():
    global player_level,player_xp,player_attack,player_hp

    if player_xp >= 100:
        player_level += 1
        player_xp -= 100
        player_attack += 5
        player_hp = 100
        print("Level up!")

def show_inventory():
    print("Inventory:")
    if not inventory:
        print("Empty")
    else:
        for item in inventory:
            print(f"Item: {item}")

print("Game Start")

while True:
    print("\n1. Attack Monster")
    print("2. Heal")
    print("3. Show Stats")
    print("4. Show Inventory")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        damage = random.randint(player_attack - 3, player_attack + 3)
        monster_hp -= damage
        print(f"\n You hit monster for {damage} damage!")

        if monster_hp <= 0:
            print(" Monster defeated!")

            player_xp += monster_xp_reward
            print(f" You gained {monster_xp_reward} XP!")


            loot = random.choice(["Sword", "Shield", "Potion", None])

            if loot:
                inventory.append(loot)
                print(f" You found: {loot}")

            monster_hp = 60 + (player_level * 10)

            level_up()


    elif choice == "2":
        heal = random.randint(10, 25)
        player_hp += heal
        print(f"You healed for {heal} HP!")


    elif choice == "3":
        show_stats()


    elif choice == "4":
        show_inventory()


    elif choice == "0":
        print("Goodbye adventurer!")
        break

    else:
        print(" Invalid choice")
