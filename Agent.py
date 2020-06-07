from random import randint

class Agent():

    def __init__(self):
        self.name = "randomAgent"

    def act(self, stateObs, actions):
        print("AAA")
        action_id = randint(0,len(actions)-1)
        return action_id
