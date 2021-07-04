# Author - Dvir Sadon
import pandas as pd
import numpy as np


def read_data():
    mycsv = pd.read_csv("winequality-red.csv")
    print(mycsv.head())
    return mycsv


def main():
    read_data()


main()
