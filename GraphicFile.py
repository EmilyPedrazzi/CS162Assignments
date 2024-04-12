#Emily Pedrazzi
#Graphic File
#4-11-24
#CS 162

import matplotlib.pyplot as plot
# set up your lists
numlist = [5, 6, 5, 3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['orchid', 'palevioletred', 'hotpink', 'thistle' ]
explodelist = [0.0, 0.1, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 60)
plot.axis('equal')
plot.savefig('piechart.png')
