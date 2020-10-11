"Pokemon Battle GO!"


class Poketer:
    def __init__(self, name, mood, health, attack):
        self.name = name
        self.mood = mood
        self.health = health
        self.attack = attack

    def __repr__(self):
        return f'Poketer: {self.name} Mood: {self.mood}'


class User:
    def __init__(self, name):
        self.name = name
        self.team = []

    def add_team(self, poketer):
        self.team.append(poketer)

    def __repr__(self):
        return f'Namn: {self.name}, Team: {self.team}'


def main():
    user_pokemon = Poketer("Happy Hasse", "happy", 100, 25)
    cpu_pokemon = Poketer("Aggressive Ada", "angry", 100, 25)

    user = User("Martin")
    cpu = User("CPU")
    user.add_team(user_pokemon)
    cpu.add_team(cpu_pokemon)
    print(f"Du valde {user_pokemon.name}")
    print(f"Din motståndare: {cpu_pokemon.name}")
    print(f"{user.name}, det är din tur! ")
    print(f"Välj en stad du tror att det är mycket {user_pokemon.mood} content i.")


    city_dic = {"Göteborg": 25, "Stockholm": 5} #Namn+gläjde

    city = input("Välj mellan Göteborg eller Stockholm: ")
    print("\nBeräknar mood'content...")

    if city == "Göteborg":
        user_pokemon.health += city_dic["Göteborg"]
        cpu_pokemon.health += city_dic['Stockholm']
        print(f"{user_pokemon.name} valde {city} med mycket happy content!")
        print(f"{user_pokemon.name} hälsa ökade med {city_dic['Göteborg']} livspoäng. Totala hälsa: {user_pokemon.health}")
        print("")
        print(f"{cpu_pokemon.name} valde 'Stockholm' med mindre happy content")
        print(f"{cpu_pokemon.name} hälsa ökade med {city_dic['Stockholm']} livspoäng. Totala hälsa: {cpu_pokemon.health}")
        print("")

    elif city == "Stockholm":
        user_pokemon.health += city_dic["Stockholm"]
        cpu_pokemon.health += city_dic['Göteborg']

        print(f"{user_pokemon.name} valde {city} med inte så mycket happy content")
        print("")
        print(f"{cpu_pokemon.name} valde 'Göteborg' med mycket happy content")
        print("")
        print(f"{user_pokemon.name} hälsa ökade med {city_dic['Stockholm']}. Totala hälsa: {user_pokemon.health}")
        print("")
        print(f"{cpu_pokemon.name} hälsa ökade med {city_dic['Göteborg']}. Totala hälsa: {cpu_pokemon.health}")
        print("")

    print("*** Time to fight! ***")
    while True:
        user_choose = int(input("Choose your move! \n1. Attack\n2. Standby\n>>> "))
        if user_choose == 1:
            cpu_pokemon.health -= user_pokemon.attack
            print(f"You ==> attacked ==> {cpu_pokemon.name}!")
            print(f"{cpu_pokemon.name} health: {cpu_pokemon.health}")
        elif user_choose == 2:
            print(f"You =/= Standby =/= {cpu_pokemon.name}")
        user_pokemon.health -= cpu_pokemon.attack
        print(f"Aggressive Ada ==> attacked ==> you!\nYour health: {user_pokemon.health}\n")

        if user_pokemon.health <= 0:
            print("Oh no! You died!")
            break

        elif cpu_pokemon.attack <= 0:
            print("Wo hoo! You won!")
            break


if __name__ == '__main__':
    main()
