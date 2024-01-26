# Created by Kaelen Cook
# Jan 2024
# table of sin & x with x between 0 and 2π, 1000 entries

# import packages
import numpy as np
from texttable import Texttable     # package for printing tables in terminal prettily
# def main function
def main():
    # initialize x between 0 and 2π with 1000 values and sin each of those vals
    x_vals = np.linspace(0, 2*np.pi, 1000)
    sin_x = np.sin(x_vals)
    # generate the table
    i = 0       # index of each value
    table = Texttable()         # initialize table from class
    table.header(["num", "x", "sin(x)"])        # labels of headings for each column
    table.set_precision(30)         # how deep do we want floats to go
    for val in x_vals:
        # add each value from x and sinx of each index
        table.add_row([i+1, x_vals[i], sin_x[i]])
        i += 1      # increment index
    # draw
    print(table.draw())

# execute main
main()