
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


    @property
    def species(self):
        print("getter")
        return self._species

    @species.setter
    def species(self, value):
        print("setter")
        self._species = value

    @property
    def number_of_birds(self):
        print("getter")
        return self._number_of_birds

    @number_of_birds.setter
    def number_of_birds(self, value):
        print("setter")
        self._number_of_birds = value if value >= 0 else 0


    @property
    def observation_time(self):
        print("getter")
        return self._observation_time

    @observation_time.setter
    def observation_time(self, value):
        print("setter")
        self._observation_time = value


    @property
    def position(self):
        print("getter")
        return self._position

    @position.setter
    def position(self, value):
        print("setter")
        self._position = value

    @property
    def additional_info(self):
        print("getter")
        return self._additional_info

    @additional_info.setter
    def additional_info(self, value):
        print("setter")
        self._additional_info = value

if __name__ == "__main__":
    #Write main program below this line
    Observation1 = Observation("crow", 32, "31.01.2020", "Savilahti", "Wind, north 5m/s")

    for i in range(11):
        Observation1.additional_info = Observation1.additional_info
        Observation1.observation_time = Observation1.observation_time
        Observation1.species = Observation1.species
        Observation1.number_of_birds = Observation1.number_of_birds
  
    print(f'{Observation1.additional_info} {Observation1.number_of_birds} {Observation1.observation_time} {Observation1.position} {Observation1.additional_info}')