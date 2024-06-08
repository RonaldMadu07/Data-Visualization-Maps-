import pygal

# Creating a world map.
worldmap = pygal.maps.world.SupranationalWorld()

# Setting the title of the map.
worldmap.title = 'Continents'

# adding the continents
worldmap.add('Africa', [('africa')])
worldmap.add('North america', [('north_america')])
worldmap.add('Oceania', [('oceania')])
worldmap.add('South america', [('south_america')])
worldmap.add('Asia', [('asia')])
worldmap.add('Europe', [('europe')])
worldmap.add('Antartica', [('antartica')])

# Save into the file.
worldmap.render_to_file('PC.svg')

print("Success")