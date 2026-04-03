import PokemonStory



if __name__ == "__main__":
    number_cycles = 151
    story = {"Bulbasaur": [],
             "Charmander": [],
             "Squirtle": []}
    end_story = None
    for i in range(number_cycles):
        print(f"{i}")
        if i < 50:
            PokemonStory.BeginStory("1",i,story)
        if i < 100:
            PokemonStory.BeginStory("2",i,story)
        if i < 150:
            PokemonStory.BeginStory("3",i,story)
        if i == 150:
            story = PokemonStory.BeginStory("1",i,story)

