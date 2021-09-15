# Sea Level Predictor

## Introduction

In this project, we have anaylized a dataset of the global average sea level change since 1880. We have used the data to predict the sea level change through year 2050.

## Tasks performed

Used the data to complete the following tasks:
* Used Pandas to import the data from `epa-sea-level.csv`.
* Used matplotlib to create a scatter plot using the "Year" column as the x-axis and the "CSIRO Adjusted Sea Level" column as the y-axix.
* Used the `linregress` function from `scipy.stats` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
* Plotted a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Made the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
* The x label should be "Year", the y label should be "Sea Level (inches)", and the title should be "Rise in Sea Level".


Unit tests are written for you under `test_module.py`.

### Development

For development, you can use `main.py` to test your functions. Click the "run" button and `main.py` will run.


