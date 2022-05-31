from sorting_techniques import pysort

def convert(string):
    print(string)
    new_array = []
    for i in string.split(','):
        new_array.append(int(i))
    print(new_array)
    return new_array

class Sorting:
    sortObj = pysort.Sorting()
    def bubbleSort(self, array):
        return self.sortObj.bubbleSort(array)

    def insertionSort(self, array):
        return self.sortObj.insertionSort(array)

    def heapSort(self, array):
        return self.sortObj.heapSort(array)

    def mergeSort(self, array):
        return self.sortObj.mergeSort(array)

    def bogoSort(self, array):
        return self.sortObj.bogoSort(array)
