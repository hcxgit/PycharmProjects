import pygal
hist = pygal.Bar()

x= [0,107,348,414,686,698,1684,1912,3437,3980]
y= [0.68,0.79,0.81,0.6,0.67,0.82,0.79,0.75,0.83,0.74]
hist.x_labels = x
hist.x_title = 'ego'
hist.add('NMI',y)
hist.render_to_file('die_visual.svg')
