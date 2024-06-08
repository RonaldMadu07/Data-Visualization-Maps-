import pygal

# Creating a world map
worldmap = pygal.maps.world.World()

# Setting the title of the map
worldmap.title = 'Countries'

# Adding the countries
worldmap.add('Random Data', {
    'aq'    : 10,
    'cd'    : 30,
    'de'    : 40,
    'eg'    : 50,
    'ga'    : 45,
    'hk'    : 23,
    'in'    : 70,
    'jp'    : 54,
    'nz'    : 41,
    'kz'    : 32,
    'us'    : 66
})

# Saving into the file
worldmap.render_to_file('PCBD.svg')

print("Success")