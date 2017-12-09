# MatPlotLib  
## Import MatPlotLib - Show a Graph
> Importing a MatPlotLib is easy. The trick is printing a graph! Import the MatPlotLib define a plot and show it. This is the simple procedures of how to make a plot.

* Importing MatPlotLib as plt because of clean coding purpose
`import matplotlib.pyplot as plt`
  
* Make a line plot:  x-axis, y-axis  
`plt.plot(data#1, data#2)`  

* Make a scatter plot;   
`plt.scatter(data#1, data#2)`
 
* Make x-axis logarithmic scale  
`plt.xscale('log')`
  
* Display the plot with plt.show()  
`plt.show()`

![MatPlotLib Example](https://github.com/musatoktas/My-Python-Works/blob/master/MatPlotLib-3.png)

## MatPlotLib Histograms

> Histogram is a type of visualization that very useful for overview and analyze your data. Building a histogram is easy beside you can specify a lot of arguments. First of all set a list or dictionary that include your data. After that type your bin amount. Bin is a field piece that shows data pile. Let's see the codes!

* Enter the Data  
`values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]`

* Assign a histogram, spesify 3 bins.  
`plt.hist(values, bins = 3)`

* Display the plot.  
`plt.show()`

* Clean the plot scene.  
`plt.clf()`  
![Histogram Sample](https://github.com/musatoktas/My-Python-Works/blob/master/MatPlotLib-1.png)
## Customizing the Plots

> For the first look on your plot, people confuse about what is the X-axis, and y-axis mean, also generally what is the purpose of the plot for general? To spesify labels and titles for our data we have bunch of codes. Let's check out them!  
Note: MatPlotLib has been imported as `plt`

* Assigning the axis Labels  
`plt.xlabel('labelname')`  
`plt.ylabel('labelname')`  

* Specify Title of Plot  
`plt.title('title1')`

* Adding 'B' sign represents the Billion to the Y-Axis  
`plt.yticks([0, 2, 4, 6, 8, 10], [0, 2B, 4B, 6B, 8B, 10B])`

 ![Before and After Plot with Customizing](https://github.com/musatoktas/My-Python-Works/blob/master/MatPlotLib-2.png) 
