"""
CS 2302
Emilio Ramirez
Lab 5 B
Diego Aguirre,  Manoj Saha
Last Date Modified: Novemeber 28th, 2018
Purpose:  Use a heap data structure to implement heapsort
"""
from Heap import Heap
def get_numbers(filename):
    """
    This method reads a file and creates a list that contains all the numbers present in that file
    To work properly the file must be formated in a particular way such that the numbers are split only by commas

    Parameters:
        filename: name of the file that is to be read
    Returns:
        number_list: a list that contains all of the numbers in the file with the given name
    """
    number_list= []
    with open(filename)as file:
        for line in file:
            values = line.split(",")
            for i in range(len(values)):
                number_list.append(values[i])
    return number_list

def heap_sort(num_list):
    """
    This method makes use of the Heap data structure in order to implement heap sort.

    Parameter:
        num_list: list of numbers to be sorted
    Returns:
        sorted_list: orderd list of numbers

    """
    New_heap = Heap()
    sorted_list = []
    for i in range(len(num_list)):
        New_heap.insert(int(num_list[i]))
#    New_heap.prints()      Uncomment to see Heap after all elements have been added
    while New_heap.is_empty() == False:
        sorted_list.append(New_heap.extract_min())
    return sorted_list

def print_list(listt):
    """
    This method prints the contents of a list

    Parameters:
        listt: list that contains elements that are to be printed
    Returns:
        Nothing.
    """
    for i in range(len(listt)):
        print( listt[i])

def main ():
    number_list = get_numbers("list_of_numbers.txt") #file name
    number_list =  heap_sort(number_list) 
    print_list(number_list)  
main()