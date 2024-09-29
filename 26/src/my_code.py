
#Write class and imports here!
class Observation:
    def __init__(self, species, number_of_birds, observation_time, position, additional_info):
        self.species = species
        self.number_of_birds = number_of_birds
        self.observation_time = observation_time
        self.position = position
        self.additional_info = additional_info

    def __str__(self):
        return f"{self.species} {self.number_of_birds} {self.observation_time} {self.position} {self.additional_info}"

    def get_species(self):
        print("getter")
        return self.species

    def set_species(self, species):
        print("setter")
        self.species = species

    def get_number_of_birds(self):
        print("getter")
        return self.number_of_birds

    def set_number_of_birds(self, number_of_birds):
        print("setter")
        if number_of_birds < 0:
            self.number_of_birds = 0
        else:
            self.number_of_birds = number_of_birds

    def get_observation_time(self):
        print("getter")
        return self.observation_time

    def set_observation_time(self, observation_time):
        print("setter")
        self.observation_time = observation_time

    def get_position(self):
        print("getter")
        return self.position

    def set_position(self, position):
        print("setter")
        self.position = position

    def get_additional_info(self):
        print("getter")
        return self.additional_info

    def set_additional_info(self, additional_info):
        print("setter")
        self.additional_info = additional_info

if __name__ == "__main__":
    #Write main program below this line
    Observation1 = Observation("crow", 32, "31.01.2020", "Savilahti", "Wind, north 5m/s")
    print(Observation1)
    for i in range(11):
        Observation1.set_additional_info(Observation1.get_additional_info())
        Observation1.set_observation_time(Observation1.get_observation_time())
        Observation1.set_species(Observation1.get_species())
        Observation1.set_number_of_birds(Observation1.get_number_of_birds())