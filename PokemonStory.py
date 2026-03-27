import FSM

def BeginStory():
    print("Welcome in Pokémon simulator!")
    GameEngine = FSM.FiniteStateMachine()

    CreateCharacter = FSM.State("CreateCharacter")
    Story = FSM.State("Story")
    Exit = FSM.State("Exit")
    PokemonStore = FSM.State("PokemonStore")
    PokemonCenter = FSM.State("PokemonCenter")
    Explore = FSM.State("Explore")
    Battle = FSM.State("Battle")

    GameEngine.add_state(CreateCharacter)
    GameEngine.add_state(Story)
    GameEngine.add_state(Exit)
    GameEngine.add_state(PokemonStore)
    GameEngine.add_state(PokemonCenter)
    GameEngine.add_state(Explore)
    GameEngine.add_state(Battle)

    GameEngine.set_start_state(CreateCharacter)



    GameEngine.add_transition(CreateCharacter, Story)
    GameEngine.add_transition(Story, Exit)
    GameEngine.add_transition(Story, Explore)
    GameEngine.add_transition(Explore, Story)
    GameEngine.add_transition(Explore, Battle)
    GameEngine.add_transition(Battle, Story)
    GameEngine.add_transition(Battle, PokemonCenter)
    GameEngine.add_transition(Story, PokemonCenter)
    GameEngine.add_transition(PokemonCenter, Story)
    GameEngine.add_transition(Story, PokemonStore)
    GameEngine.add_transition(PokemonStore, Story)

    GameEngine.initialize()
    GameEngine.eval_current()
    GameEngine.do_transition(Story)
    GameEngine.eval_current()

    print("Do you want to keep playing? (y/n)")
    choice = (input("> "))
    if choice == "y":
        enterStory()
    elif choice == "n":
        GameEngine.do_transition(Exit)
        GameEngine.eval_current()
    else:
        while choice != "y" and choice != "n":
            print("Do you want to keep playing? (y/n)")
            choice = (input("> "))
            if choice == "y":
                enterStory()
            elif choice == "n":
                GameEngine.do_transition(Exit)
                GameEngine.eval_current()


def enterStory():
    pass











