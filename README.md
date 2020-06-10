# Various scripts and python libraries for my final year project

/lib/ is the where the actual neurons, synapses and simulation is defined. (Should probably be renamed, turns out that /lib/ is a special folder name in Python-land)

/scripts/ are the various... scripts that use the simulation to do "interesting" (my mother, 2020) things.

The various `.p` files at the root of the repository are `pickled` results files, that were saved in order to separate the process of generating results to analysing them. 

# TODO
 - Remove pickle files and get the results and graphs into a easily repeatable state.
 - Add a "pickle" directory that caches results by parameter.
 - Move network generation boilerplate into a helper class for scenarios where parameters are arbitrary
 
