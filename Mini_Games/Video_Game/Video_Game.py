# game.py
from Knight import Knight
from Wizard import Wizard
from Dragon import Dragon

def main():
    print("Choose your character:")
    print("1. Knight")
    print("2. Wizard")
    choice = input("Select your hero (1-2): ")

    if choice == '1':
        player = Knight("Sir Lancelot", 120)
    elif choice == '2':
        player = Wizard("Merlin", 100)
    else:
        print("Invalid choice. Exiting game.")
        return

    dragon = Dragon("Smaug", 120)

    print(f"{player.name} faces off against {dragon.name}!")
    print(f"Starting health - {player.name}: {player.health}, {dragon.name}: {dragon.health}")
    
    while player.health > 0 and dragon.health > 0:
        print(f"\n{player.name} Health: {player.health}, {dragon.name} Health: {dragon.health}")
        print("What will you do?")
        print("1. Attack")
        print("2. Special Move")
        print("3. Flee")
        action = input("Choose an action (1-3): ")

        if action == '1':
            player.attack(dragon)
        elif action == '2':
            if isinstance(player, Knight) or isinstance(player, Wizard):
                player.special_move(dragon)
            else:
                print("This character doesn't have a special move. Regular attack performed.")
                player.attack(dragon)
        elif action == '3':
            print(f"{player.name} flees from battle. Game Over.")
            break
        else:
            print("Invalid action. Turn skipped.")
            continue
        
        if dragon.health <= 0:
            print(f"{dragon.name} has been defeated! You win!")
            break
        
        # Dragon's turn
        if dragon.health > 60 or player.health < 30:
            dragon.attack(player)
        else:
            print(f"{dragon.name} is gathering strength for the next attack.")
        
        if player.health <= 0:
            print(f"{player.name} has fallen in battle. Game Over.")
            break

if __name__ == "__main__":
    main()