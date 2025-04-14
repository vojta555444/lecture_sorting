import csv
import os

import numpy as np


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    data = {}
    with open(file_path,mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort (arr, direction = "asce"):
    """
    Selection sort
    :param arr:
    :param direction:
    :return:
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        if direction == "asce":
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
        else:
            for j in range(i + 1, n):
                if arr[j] > arr[min_index]:
                    min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort (arr):
    min_index = 0
    max_index = len(arr)
    while min_index < max_index:
        for index in range(min_index, max_index-1):
            if arr[index] > arr[index+1]:
                pom = arr[index]
                arr[index] = arr[index+1]
                arr[index+1] = pom
        max_index -= 1
    return arr

def insertion_sort (arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j +1] = arr[j]
            j=j-1
        arr[j+1]=key
    return arr

def main():
    data = read_data("numbers.csv")
    # pole = selection_sort(data["series_1"])
    pole = insertion_sort(data["series_1"])
    print(pole)
    pass


if __name__ == '__main__':
    main()
