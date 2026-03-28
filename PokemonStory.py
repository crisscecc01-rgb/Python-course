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
        KeepPlaying(GameEngine)
    elif choice == "n":
        GameEngine.do_transition(Exit)
        GameEngine.eval_current()
    else:
        while choice != "y" and choice != "n":
            print("Do you want to keep playing? (y/n)")
            choice = (input("> "))
            if choice == "y":
                KeepPlaying(GameEngine)
            elif choice == "n":
                GameEngine.do_transition(Exit)
                GameEngine.eval_current()


def KeepPlaying(GameEngine):
    #GameEngine.draw(show_current_state=True, node_size = 3000, arrowsize = 10)
    print(f"\nYou are in {GameEngine.state.name}")
    print("Where do you want to go? (Possible destinations)")
    next_states = list(GameEngine.G.successors(GameEngine.state))
    for i,n_state in enumerate(next_states):
        print("--> ",n_state.name)
    choice = (input("> "))
    while 1==1:
        match choice:

            case "CreateCharacter":
                print("Can't go here!")
            case "Story":
                Story_state = None
                for s in next_states:
                    if s.name == "Story":
                        Story_state = s
                        break
                if Story_state:
                    GameEngine.do_transition(Story_state)
                    GameEngine.eval_current()
                else:
                    print("Can't go here!")

            case "PokemonStore":
                PokemonStore_state = None
                for s in next_states:
                    if s.name == "PokemonStore":
                        PokemonStore_state = s
                        break
                if PokemonStore_state:
                    GameEngine.do_transition(PokemonStore_state)
                    GameEngine.eval_current()
                    print("Do you want to do something else? (y/n)")
                    choice = (input("> "))
                    while choice != "n":
                        GameEngine.eval_current()
                        print("Do you want to do something else? (y/n)")
                        choice = input("> ")
                else:
                    print("Can't go here!")

            case "PokemonCenter":
                PokemonCenter_state = None
                for s in next_states:
                    if s.name == "PokemonCenter":
                        PokemonCenter_state = s
                        break
                if PokemonCenter_state:
                    GameEngine.do_transition(PokemonCenter_state)
                    GameEngine.eval_current()
                    print("Do you want to do something else? (y/n)")
                    choice = (input("> "))
                    while choice != "n":
                        GameEngine.eval_current()
                        print("Do you want to do something else? (y/n)")
                        choice = input("> ")
                else:
                    print("Can't go here!")

            case "Explore":
                Explore_state = None
                for s in next_states:
                    if s.name == "Explore":
                        Explore_state = s
                        break
                if Explore_state:
                    GameEngine.do_transition(Explore_state)
                    GameEngine.eval_current()
                    print("Do you want to do something else? (y/n)")
                    choice = (input("> "))
                    while choice != "n":
                        GameEngine.eval_current()
                        print("Do you want to do something else? (y/n)")
                        choice = input("> ")
                else:
                    print("Can't go here!")

            case "Exit":
                Exit_state = None
                for s in next_states:
                    if s.name == "Exit":
                        Exit_state = s
                        break
                if Exit_state:
                    GameEngine.do_transition(Exit_state)
                    GameEngine.eval_current()
                    break
                else:
                    print("Can't go here!")

            case "Battle":
                Battle_state = None
                for s in next_states:
                    if s.name == "Battle":
                        Battle_state = s
                if Battle_state:
                    GameEngine.do_transition(Battle_state)
                    GameEngine.eval_current()
                else:
                    print("Can't go here!")

            case _:
                print("Can't go here!")

        print(f"\nYou are in {GameEngine.state.name}")
        print("Where do you want to go? (Possible destinations)")
        next_states = list(GameEngine.G.successors(GameEngine.state))
        for i, n_state in enumerate(next_states):
            print("--> ", n_state.name)
        choice = (input("> "))













