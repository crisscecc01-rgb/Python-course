import PokemonStory



if __name__ == "__main__":
    number_cycles = 1500
    story = {"Bulbasaur": [],
             "Charmander": [],
             "Squirtle": []}
    end_story = None
    for i in range(number_cycles):
        if i < 500:
            PokemonStory.BeginStory(1,i,story)
        if i < 1000:
            PokemonStory.BeginStory(2,i,story)
        if i < 1500:
            PokemonStory.BeginStory(3,i,story)
        if i == 1500:
            story = PokemonStory.BeginStory(1,i,story)
