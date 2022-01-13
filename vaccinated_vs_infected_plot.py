2#!/usr/bin/env python

'''
graph.py
  Author(s): Joshua Komonen (1150389), Sukhman Brar (1102371), Armaan Mattu , Matthew Parra (1105933)

  Project: Milestone III
  Date of Last Update: March 31, 2021

  Compilation Example: python vaccinated_vs_infected_plot.py plot4.txt plot4.pdf

'''


#
#   Packages and modules
#
import sys

# pandas is a (somewhat slow) library to do complicated
# things with CSV files. We will use it here to identify
# data by column
import pandas as pd

# seaborn and matplotlib are for plotting.  The matplotlib
# library is the actual graphics library, and seaborn provides
# a nice interface to produce plots more easily.
import seaborn as sns
from matplotlib import pyplot as plt


def main(argv):

    '''
    Create a plot using ranks
    '''

    #
    #   Check that we have been given the right number of parameters,
    #
    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    #
    if len(argv) != 3:
        print("Usage:",
                "create_name_plot.py <data file> <graphics file>")
        sys.exit(-1)

    csv_filename = argv[1]
    graphics_filename = argv[2]


    #
    # Open the data file using "pandas", which will attempt to read
    # in the entire CSV file
    #
    try:
        csv_df = pd.read_csv(csv_filename)

    except IOError as err:
        print("Unable to open source file", csv_filename,
                ": {}".format(err), file=sys.stderr)
        sys.exit(-1)


    # A this point in the file, we begin to do the plotting

    # We must get the figure before we plot to it, or nothing will show up.
    # The matplotlib "figure" is the data environment that we are drawing
    # our plot into.  The seaborn library will draw onto this figure.
    # We don't see seaborn directly refer to "fig" because it is internally
    # drawing on "the current figure" which is the same one we are
    # referencing on this line.
    fig = plt.figure()


    # This creates a lineplot using seaborn.  We simply refer to
    # the various columns of data we want in our pandas data structure.
    #sns.lineplot(x = "report_date", y = "total_individuals_fully_vaccinated",data=csv_df)

    sns.lineplot(x = "Reported Date", y = "Total Individuals Fully Vaccinated",data=csv_df)
    sns.lineplot(x = "Reported Date", y = "Total Individuals Infected",data=csv_df)
    plt.title("Vaccinated vs Infected")
    plt.ylabel('Total Individuals Fully Vaccinated/Infected')
    plt.tick_params(axis='x', which='major', labelsize=5)
    fig.autofmt_xdate()

    fig.savefig(graphics_filename, bbox_inches="tight")

    # Function add a legend  
    plt.legend(('Total Individuals Fully Vaccinated','Total Individuals Infected'))
      
    # function to show the plot
    plt.show()

main(sys.argv)

