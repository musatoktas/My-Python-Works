# Import MatPlotLib - Show a Graph
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

<image's will add/>

## MatPlotLib Histograms

> Histogram is a type of visualization that very useful for overview and analyze your data. Building a histogram is easy beside you can specify a lot of arguments. First of all set a list or dictionary that include your data. After that type your bin amount. Bin is a field piece that shows data pile. Let's see the codes!

* Enter the Data
`values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]`
* Assign a histogram, spesify 3 bins.
`plt.hist(values, bins = 3)`
* Showing the plot.
`plt.show()`
