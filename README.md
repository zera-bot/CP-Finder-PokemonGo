# CP-Finder-PokemonGo

The program has two modes, creating the dictionaries, and finding Pokemon with different IVs and levels that calculated to the target CP.

## Creating Dictionaries
To calculate target CPs, we must first create a dictionary. Our code creates a dictionary with every Pokemon at every level (from 1-51 with 0.5 step) and their minimum and maximum CP at the level in the dictionary. This dictionary will be used in finding Pokemon that are a target CP.

## Finding Pokemon
To find Pokemon with target CPs, we must first look at our variables.
Our variables are:
- The Pokemon
- The Attack IV Stat
- The Defense IV Stat
- The Stamina IV Stat
- The Level

To find matches of Pokemon that fit through our target CP, we search through our dictionary to see if the target CP is less than the maximum CP, and more than the minimum CP. We will store the lists in another list.
We search through our matches list, and brute-force every possible IV combination for the Pokemon at the specified level. Each brute-force action searches through 4,096 combinations of IVs. We then add the matches to a list, and export it as json, csv or both (as specified by an input variable.)
You may also search through an o(ptimized) list (that only contains "Normal" forms of Pokemon) or the f(ull) list. Depending on the processing speed of your computer, it may take a while to process all the results, so be patient.

Have fun!
