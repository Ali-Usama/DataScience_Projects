import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize = (10, 5))
    plt.scatter(x = 'Year', y='CSIRO Adjusted Sea Level',
               data = df, color = 'b', label='original data')
               
    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    x_det = list(range(1880, 2050))
    y_det = list()
    
    for year in x_det:
    	y_det.append(year*result.slope + result.intercept)
    	
    plt.plot(x_det, y_det, color='r')

    # Create second line of best fit for the data starting from year 2000:
    y_from_2000 = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    x_from_2000 = df[df['Year'] >= 2000]['Year']

    res_2000 = linregress(x_from_2000, y_from_2000)
    x_2000 = list(range(2000, 2050))
    y_2000 = list()
    for each in x_2000:
    	y_2000.append((each*res_2000.slope + res_2000.intercept))
    plt.plot(x_2000, y_2000, 'g')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
