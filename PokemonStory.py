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
    Battle.outcome = True

    GameEngine.add_state(CreateCharacter)
    GameEngine.add_state(Story)
    GameEngine.add_state(PokemonStore)
    GameEngine.add_state(PokemonCenter)
    GameEngine.add_state(Explore)
    GameEngine.add_state(Battle)
    GameEngine.add_state(Exit)

    GameEngine.add_final_state(Exit)
    GameEngine.set_start_state(CreateCharacter)



    GameEngine.add_transition(CreateCharacter, Story, type = "consequence")
    GameEngine.add_transition(Story, Exit, type = "choice")
    GameEngine.add_transition(Story, Explore, type = "choice")
    GameEngine.add_transition(Explore, Story, type = "choice")
    GameEngine.add_transition(Explore, Battle, type = "consequence", probability = 0.5)
    GameEngine.add_transition(Battle, Story, type = "consequence")
    GameEngine.add_transition(Battle, PokemonCenter, type = "consequence")
    GameEngine.add_transition(Story, PokemonCenter, type = "choice")
    GameEngine.add_transition(PokemonCenter, Story, type = "choice")
    GameEngine.add_transition(Story, PokemonStore, type = "choice")
    GameEngine.add_transition(PokemonStore, Story, type = "choice")

    GameEngine.initialize()

    while GameEngine.state not in GameEngine.final_states:

        GameEngine.eval_current()
        next_state = GameEngine.update()
        if next_state:
            GameEngine.do_transition(next_state)
        else:
            print("No possible transition. Quitting.")
            break

    GameEngine.eval_current()













