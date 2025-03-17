import random

def introduction():
    
    print("Overseer, the great houses rest in your hands. Choose the rightful heir to lead the great houses to peace...")

def select_house():
    
    houses = {
        "1": ("House Obsidian", "Princess Kaelia", {"Agility": 5, "Intelligence": 5, "Strength": -5, "Willpower": 3}),
        "2": ("House Bonekeep", "Prince Drakon", {"Agility": -5, "Intelligence": -5, "Strength": 10, "Willpower": 0}),
        "3": ("House Everstead", "Prince Kaelos", {"Agility": 0, "Intelligence": 5, "Strength": 5, "Willpower": 5})
    }
    
    print("Choose an heir to face the trial:")
    for key, (house, heir, stats) in houses.items():
        print(f"{key}: {heir} of {house}")
    
    while True:
        choice = input("Enter the number of your chosen heir: ")
        if choice in houses:
            return houses[choice]
        print("Invalid choice. Please try again.")

def initialize_stats(base_stats):
    
    return {"Health": 100, **base_stats}

def pre_trial_choice(player_stats):
    
    print("Before the next trial, you may prepare:")
    print("1) Sharpen your sword (+10 Strength)")
    print("2) Pray to the gods (+10 Willpower)")
    print("3) Stretch (+10 Agility)")
    print("4) Eat and sleep (+10 Health)")
    
    while True:
        choice = input("Choose your preparation: ")
        if choice == "1":
            player_stats["Strength"] += 10
            print("You sharpen your sword. Strength +10!")
            break
        elif choice == "2":
            player_stats["Willpower"] += 10
            print("You pray to the gods. Willpower +10!")
            break
        elif choice == "3":
            player_stats["Agility"] += 10
            print("You stretched. Agility +10!")
            break
        elif choice == "4":
            player_stats["Health"] += 10
            print("You eat and rest. Health +10!")
            break
        else:
            print("Invalid choice. Please try again.")

def trial_combat(player_stats):
    
    pre_trial_choice(player_stats)
    print("You've awakened in the trial arena and an Orc with a Battle axe is preparing to thrust their axe in your direction! Do you counter their attack or dodge?")
    enemy_health = 25
    while player_stats["Health"] > 0 and enemy_health > 0:
        action = input("Attack (A) or Dodge (D)? ").upper()
        if action == "A":
            damage = random.randint(5, 15) + player_stats["Strength"]
            enemy_health -= damage
            print(f"You strike for {damage} damage! Orc health: {enemy_health}, The orc charges you with another swing, do you counter or dodge?")
        elif action == "D":
            dodge_chance = random.randint(1, 10) + player_stats["Agility"]
            if dodge_chance > 10:
                print("You successfully dodge the attack!")
            else:
                player_stats["Health"] -= 10
                print(f"You fail to dodge and take damage! Heir Health: {player_stats['Health']}, The orc charges you with another swing, do you counter or dodge?")
                
        if enemy_health <= 0:
            print("You have won the trial!")
            return True
        elif player_stats["Health"] <= 0:
            print("You have fallen in the trial...")
            return False

def trial_walk_of_sacrifice(player_stats):
    
    pre_trial_choice(player_stats)
    print("You are tasked with carrying a heavy load of food across a fragile bridge. On the other side, a starving family awaits.")
    print("The wind howls and the bridge sways dangerously under your feet.")
    
    print("1) Push forward despite the burden")
    print("2) Drop some food to lighten the load")
    print("3) Drop all the food and run")
    
    while True:
        choice = input("What do you do? ")
        if choice == "1":
            if player_stats["Willpower"] >= 8:
                print("Through sheer determination, you push forward and deliver the food. The family rejoices at your sacrifice!")
                return True
            else:
                print("Your willpower falters, and you stumble, dropping some of the food.")
                return True
        elif choice == "2":
            if player_stats["Willpower"] >= 4:
                print("You lighten the load and manage to cross, but the family receives less than they need.")
                return True
            else:
                print("Your willpower falters, and you drop too much food, barely making it across")
                return True
        elif choice == "3":
            print("Overcome by fear, you abandon the food and run. The overseer expels you from the trial chamber.")
            return False
        else:
            print("Invalid choice. Please try again.")

def agility_trial(player_stats):
    
    pre_trial_choice(player_stats)
    print("A boulder suddenly drops behind you, slowly inching towards you faster and faster!")
    print("1) Attempt to stop the boulder from moving")
    print("2) Attempt to outrun the boulder")
    print("3) Accept your fate")
    
    while True:
        choice = input("What do you do? ")
        if choice == "1":
            if player_stats["Strength"] >= 10:
                print("Through sheer strength, you're able to stop the boulder in its tracks!")
                return True
            else:
                print("The weight of the boulder overcomes you. You perish.")
                return False
        elif choice == "2":
            if player_stats["Agility"] >= 5:
                print("You manage to outrun the boulder!")
                return True
            else:
                print("You attempt to run, but the boulder catches up to you.")
                return False
        elif choice == "3":
            print("The weight of the boulder overcomes you. You perish.")
            return False
        else:
            print("Invalid choice. Please try again.")

def trial_loyalty(player_stats):
    
    pre_trial_choice(player_stats)
    print("You encounter a wounded ally and a treasure chest. You can only carry one.")
    print("1) Save your ally.")
    print("2) Take the treasure.")
    
    while True:
        choice = input("What do you do? ")
        if choice == "1":
            print("You save your ally, earning their eternal gratitude. The Overseer approves of your loyalty.")
            return True
        elif choice == "2":
            print("You take the treasure, but the Overseer judges you as selfish. You fail the trial.")
            return False
        else:
            print("Invalid choice. Please try again.")

def game_over(outcome):
    
    if outcome == "Victory":
        print("Congratulations! You have proven yourself worthy. The great houses celebrate your triumph!")
    elif outcome == "Death":
        print("Your journey has ended in tragedy. The great houses mourn your loss.")
    else:
        print("The trials have left your fate uncertain. The great houses await your return.")

def main():
    introduction()
    heir_data = select_house()
    if not heir_data:
        print("Invalid choice. Exiting game.")
        return
    
    house, heir, stats = heir_data
    print(f"You have chosen {heir} of {house}.")
    player_stats = initialize_stats(stats)
    
    
    if trial_combat(player_stats):
        if trial_walk_of_sacrifice(player_stats):
            if agility_trial(player_stats):
               
                if trial_loyalty(player_stats):
                    game_over("Victory")
                else:
                    game_over("Death")
            else:
                game_over("Death")
        else:
            game_over("Death")
    else:
        game_over("Death")

if __name__ == "__main__":
    main()