import pygal

from pygal.style import Style

# Creating a custom style object
custom_style = Style( colors = ('#FF0000' , '#0000FF' , '#00FF00' , '#000000' , '#FFD700'))

# Creating a world map.
worldmap = pygal.maps.world.World(style = custom_style)

# Setting the title of the map.
worldmap.title = 'Some Countries Starting from Specific Letters'

# Hex code of colours are used for every .add() called.
worldmap.add('"E" Countries', ['ec', 'ee', 'eg', 'eh', 'er', 'es', 'et'])
worldmap.add('"F" Countries', ['fr', 'fi'])
worldmap.add('"P" Countries', ['pa', 'pe', 'pg' ,'ph' , 'pk', 'pl', 'pr', 'ps', 'pt', 'py'])
worldmap.add('"Z" Countries', ['zm', 'zw'])
worldmap.add('"A" Countries', ['ad', 'ae', 'af', 'al', 'am', 'ao', 'aq', 'ar', 'at', 'au', 'az'], color = 'black')

# Save into the file.
worldmap.render_to_file('PCL.svg')

print("Success")

