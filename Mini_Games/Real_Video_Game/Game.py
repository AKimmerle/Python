from Mage import Mage
from Villan import Villan

def main():
    print("Welcome to The Mage's Revolt Against Darkness! Please select an option:")
    print("1. Begin Game")
    print("2. Exit Game")
    choice = input("Select an option (1-2): ")
    
    if choice == '1':
        player = Mage("Bo Bao", 300, 300)
    elif choice == '2':
        print("Exiting game.")
        return 

    villan = Villan("Malakar Shadowbane", 300, 300)

    print(f"{player.name} vs. {villan.name}!")
    print(f"Starting health - {player.name}: {player.health}, {villan.name}: {villan.health}")
    
    while player.health > 0 and villan.health > 0:
        print(f"\n{player.name} Health: {player.health}, {villan.name} Health: {villan.health}")
        print("What will you do?")
        print("1. Firebolt")
        print("2. Fireball")
        print("3. Icebolt")
        print("4. Iceball")
        print("5. Health Potion")
        print("6. Flee")
        
        action = input("Choose an action (1-6): ")

        if action == '1':
            player.Firebolt(villan)
        elif action == '2':
            player.Fireball(villan)
        elif action == '3':
            player.Icebolt(villan)
        elif action == '4':
            player.Iceshard(villan)
        elif action == '5':
            player.Health_Potion(villan)
        elif action == '6':
            print(f"You fled from the battle. Game over.")
            break
        else:
            print("Invalid action. Turn skipped.")
        
        # Check if villain is defeated
        if villan.health <= 0:
            print(f"You have defeated {villan.name}! Congratulations!")
            break

        # Villan's turn
        print(f"{villan.name} takes their turn.")
        if villan.health > 60 or player.health < 30:
            villan.Shadowbolt(player)
        elif villan.health > 100 or player.health < 50:
            villan.Dark_Pulse(player)
        elif villan.health < 60:
            villan.ShadowClaw(player)
        
        # Check if player is defeated
        if player.health <= 0:
            print(f"{player.name} has died. Game Over.")
            break

if __name__ == "__main__":
    main()