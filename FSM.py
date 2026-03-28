import networkx as nx
import matplotlib.pyplot as plt
from PKGame import *
from PkClasses import *
from Database import PokemonDatabase as Pk_db
import random


# Template of the State class for the FSM
class State:
    def __init__(self, name=None):
        self.name = name
        self.outcome = None
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

    # Method to perform the operation of the current state of the FSM
    # (used by .eval_current() method of the FSM)
    def run(self, *args, **kargs):
        fsm = kargs.get('fsm')
        match self.name:
            case "CreateCharacter":
                fsm.trainer = createCharacter()
                print("You just created the trainer and selected your first pokemon!")
            case "Story":
                print("You just entered the story!")
            case "Exit":
                print("You just exited the story. By!")
            case "PokemonStore":
                print("You just entered the pokemon store!")
                fsm.trainer = DoSomething(BuyItems,fsm.trainer)
            case "PokemonCenter":
                print("You just entered the pokemon center!")
                fsm.trainer = DoSomething(HealPokemons,fsm.trainer)
            case "Explore":
                print("You just entered the JUNGLE!")
                prob = 0
                transitions = list(fsm.G.out_edges(self, data=True))
                for s, n_state, attr in transitions:
                    if n_state.name == "Battle":
                        prob = attr.get("probability")
                choice = "y"
                while choice != "n":
                    outcome_explore = ExploreJungle(prob)
                    if outcome_explore:
                        print("\nA wild Pokemon has appeared")
                    else:
                        print("\nStill no pokemon in sight!")
                    self.outcome = outcome_explore
                    print("Do you want to keep exploring?")
                    choice = (input("> ")).strip().lower()

            case "Battle":
                print("You just entered the Battle!")
                pass
            case _:
                print("Not possible")
                pass

    # Method to select the next state of the FSM
    # (used by .update() method of the FSM)
    def update(self, choices, *args, **kargs):
        fsm = kargs.get('fsm')
        if not choices:
            print("No transition possible, machine halting.")
            return None

        if fsm.state.name == "Explore":
            Battle_state = None
            for s in choices:
                if s.name == "Battle":
                    Battle_state = s
            if self.outcome:
                return Battle_state


        if fsm.state.name == "Battle":
            pass



        valid_choices = []
        for state in choices:
            edge_data = fsm.G[fsm.state][state][0]
            if edge_data.get('type') == 'choice':
                valid_choices.append(state)

        print(f"You are currently in: {self.name}")
        print("Where do you want to go? (Possible destinations):")

        for state in valid_choices:
            print(f"--> {state.name}")

        while True:
            choice_input = input("> ").strip()
            for state in valid_choices:
                if state.name == choice_input:
                    return state
            print("Can't go here! Chose from the list.")


class FiniteStateMachine:
    def __init__(self):
        self.G = nx.MultiDiGraph()
        self.state = None
        self.start_state = None
        self.final_states = set()
        self.trainer = None

    # Method to initialize the FSM to the start state
    def initialize(self):
        self.state = self.start_state

    # Method to add a state to the FSM
    def add_state(self, state, **kargs):
        self.G.add_node(state, **kargs)

    # Method to add a transition between two states of the FSM
    def add_transition(self, state1, state2, **kargs):
        self.G.add_edge(state1, state2, **kargs)

    # Method to remove a state from the FSM
    def remove_state(self, state):
        if state not in list(self.G):
            print("State", state, "is not present!")
            return False
        self.G.remove_node(state)

    # Method to remove a transition from the FSM
    def remove_transition(self, state1, state2):
        if state1 not in list(self.G):
            print("State", state1, "is not present!")
            return False
        if state2 not in list(self.G):
            print("State", state2, "is not present!")
            return False
        if (state1, state2) not in [e for e in self.G.edges]:
            print("Transition", (state1, state2), "is not present!")
            return False
        self.G.remove_edge(state1, state2)

    # Method to set the start state of the FSM
    def set_start_state(self, state):
        if state not in list(self.G):
            print("State", state, "is not present!")
            return False
        self.start_state = state

    # Method to set the final states of the FSM
    def set_final_states(self, states):
        for s in states:
            if s not in list(self.G):
                print("State", s, "is not present!")
                return False
        self.final_states = set(states)

    # Method to add a final state to the FSM
    def add_final_state(self, state):
        if state not in list(self.G):
            print("State", state, "is not present!")
            return False
        self.final_states.add(state)

    # Method to remove a final state from the FSM
    def remove_final_state(self, state):
        if state not in self.final_states:
            print("State", state, "is not present!")
            return False
        self.final_states.remove(state)

    # Method to reset the final states of the FSM
    def clear_final_states(self):
        self.final_states = set()

    # Method to extract one or more attributes from the current state of the FSM
    def get_state_attributes(self, attr=None):
        if not attr:
            return self.G.nodes[self.state]
        else:
            return self.G.nodes[self.state][attr]

    # Method to extract one or more attributes from the transition between
    # the current state and the target state
    def get_transition_attributes(self, target, attr=None):
        if not attr:
            return self.G[self.state][target][0]
        else:
            return self.G[self.state][target][0][attr]

    # Method to run the current state of the FSM
    def eval_current(self, *args, run='run', **kargs):
        method = getattr(self.state, run, None)
        if callable(method):
            method(*args,fsm = self, **kargs)

    # Method to perform the transition between the current state and the target state
    def do_transition(self, target, *args, attr='fun', **kargs):
        if attr in self.G[self.state][target][0]:
            self.G[self.state][target][0][attr](*args, **kargs)
        self.state = target

    # Method that returns the list of possible transitions from the current state
    def possible_transitions(self):
        return [n for n in self.G.neighbors(self.state)]

    # Method to identify the next transition of the FSM using the state update method
    def update(self, *args, update='update', **kargs):
        choices = self.possible_transitions()
        if not choices:
            print("No transition possible, machine halting.")
            return None
        elif len(choices) == 1:
            return choices[0]
        elif callable(getattr(self.state, update, None)):
            method = getattr(self.state, update, None)
            return method(choices, *args,fsm=self, **kargs)
        else:
            print("Update rule is undefined, machine halting.")
            return None

    # Method to draw the FSM and, eventually, visualize the current state of the FSM
    def draw(self, show_current_state=True, **kwds):
        pos = nx.spring_layout(self.G)
        if show_current_state:
            nodes = list(self.G)
            colors = ['b']*len(nodes)
            colors[nodes.index(self.state)] = 'g'

            nx.draw(self.G,pos, with_labels=True,
                    node_color = colors,
                    connectionstyle='arc3, rad = 0.1', **kwds)
        else:
            nx.draw(self.G,pos, with_labels=True,
                    connectionstyle='arc3, rad = 0.1', **kwds)
        plt.show()




def createCharacter():
    trainer_name = input("What's your name: ")
    trainer = PokemonTrainerClass(trainer_name, [], [])
    print("Select your starter pokémon:")
    starterPokemon = [create_playable_pokemon(Pk_db.PokemonList[0], 5),
                      create_playable_pokemon(Pk_db.PokemonList[3], 5),
                      create_playable_pokemon(Pk_db.PokemonList[6], 5)]
    for pokemon, opt in enumerate(starterPokemon):
        print(pokemon + 1, ':', opt.name)
    choice = (input("> "))

    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(starterPokemon):
        print("Select between 1 and " + str(len(starterPokemon)) + ":")
        for pokemon, opt in enumerate(starterPokemon):
            print(pokemon + 1, ':', opt.name)
        choice = (input("> "))
    trainer.pk_list.append(starterPokemon[int(choice) - 1])
    heals = [HealClass("Potion", 10)]
    pokeballs = [PokeBallClass("PokeBall", 10)]
    trainer.items = {"heals": heals,
                     "pokeballs": pokeballs}

    print(f"you selected {trainer.pk_list[0].name}!")
    print(trainer)
    return trainer

def DoSomething(function, trainer):
    trainer_done = trainer
    choice = "y"
    while choice != "n":
        trainer_done = function(trainer_done)
        print("Do you want to do something else? (y/n)")
        choice = (input("> ")).strip().lower()

    return trainer_done

def BuyItems(trainer):
    print(f"Welcome to Market ! ")
    print(f"Your current inventory:\n{trainer.str_items()}")
    print("Do you want to buy something? (y/n)")
    choice = (input("> ")).strip().lower()
    if choice == "y":
        print("What do you want to buy?")
        categories = list(trainer.items.keys())
        for items,cat in enumerate(categories):
            print(f"{items+1}: {trainer.items[cat]}")

        choice = input("> ")
        if not choice.isdigit() or int(choice) not in range(1, len(categories) + 1):
            print("We don't have that category here.")
            return trainer

        selected_category = categories[int(choice) - 1]
        if selected_category == "heals":
            item_name = "Potion"  #to be updated in order to choose between the ones available in database
            print(f"How many {item_name} do you want to buy?")
            qty_input = input("> ")

            if qty_input.isdigit() and int(qty_input) > 0:
                qty = int(qty_input)

                found = False
                for item in trainer.items["heals"]:
                    if item.name == item_name:
                        item.number += qty
                        found = True
                        break

                if not found:
                    new_item = HealClass(item_name, qty)
                    trainer.items["heals"].append(new_item)

                print(f"You received {qty} {item_name}!")
            else:
                print("Not a valid quantity.")

        elif selected_category == "pokeballs":
            item_name = "PokeBall" #to be updated in order to choose between the ones available in database
            print(f"How many {item_name} do you want to buy?")
            qty_input = input("> ")

            if qty_input.isdigit() and int(qty_input) > 0:
                qty = int(qty_input)

                found = False
                for item in trainer.items["pokeballs"]:
                    if item.name == item_name:
                        item.number += qty
                        found = True
                        break

                if not found:
                    new_item = HealClass(item_name, qty)
                    trainer.items["pokeballs"].append(new_item)

                print(f"You received {qty} {item_name}!")
            else:
                print("Not a valid quantity.")

    print(f"\nYour current inventory:\n{trainer.str_items()}")
    return trainer

def HealPokemons(trainer):
    print(f"\nNurse Joy: 'Hi {trainer.name}, welcome to the Pokemon Center!'")
    print("Do you want to heal your pokemons? (y/n)")
    choice = input("> ").strip().lower()
    if choice != "n":
        for pokemon in trainer.pk_list:
            pokemon.currentHP = int(pokemon.stats["hp"])
        print("Your Pokemons have now been healed!")

    return trainer

def ExploreJungle(prob):
    enemy = random.uniform(0, 1.0)
    return prob >= enemy



