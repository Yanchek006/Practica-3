import requests
import time

SECRET_KEY: str = 'vyspPq/jHxq0Q7flIKWrXw==4cVRGPMFFCyPzsUZ'


class CityGame:
    def __init__(self):
        self.cities = []
        self.players = ['Player 1', 'Player 2']
        self.scores = {player: 0 for player in self.players}

    def is_valid_city(self, city):
        return self.get_city_by_name(city) is not None

    def add_city(self, city):
        if self.is_valid_city(city) and not self.check_city_exists(city):
            self.cities.append(city)

    def check_city_exists(self, city):
        return city in self.cities

    @staticmethod
    def get_city_by_name(name: str):
        api_url = f'https://api.api-ninjas.com/v1/city?name={name}'
        response = requests.get(api_url, headers={'X-Api-Key': SECRET_KEY})
        if response.status_code == requests.codes.ok:
            json = response.json()
            if len(json) != 0:
                return json[0]["name"]
            else:
                print(f"Error: city: {name} not found")
        else:
            print("Error:", response.status_code, response.text)

        return None

    def play_round(self, player):
        print(f"{player}, your turn! You have 10 seconds to enter a city.")
        start_time = time.time()
        while time.time() - start_time < 10:
            city = input("Enter a city: ").strip()
            if self.is_valid_city(city) and not self.check_city_exists(city):
                self.add_city(city)
                self.scores[player] += 1
                print(f"{player} scored a point! Total score: {self.scores[player]}")
                return
        print(f"{player}, time's up!")

    def play_game(self):
        for round_num in range(1, 11):
            print(f"Round {round_num}")
            self.play_round(self.players[round_num % 2])

        if self.scores[self.players[0]] > self.scores[self.players[1]]:
            print(f"{self.players[0]} wins with a score of {self.scores[self.players[0]]}!")
        elif self.scores[self.players[0]] < self.scores[self.players[1]]:
            print(f"{self.players[1]} wins with a score of {self.scores[self.players[1]]}!")
        else:
            print("It's a tie!")
