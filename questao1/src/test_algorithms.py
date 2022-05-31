import algorithms as algorithms

unsorted_array = [5,4,3,2,1]
pre_sorted_array = [1,2,3,4,5]

def test_bubbleSort():
    sorted_array = algorithms.Sorting().bubbleSort(unsorted_array)
    assert sorted_array == pre_sorted_array
    
def test_insertionSort():
    sorted_array = algorithms.Sorting().insertionSort(unsorted_array)
    assert sorted_array == pre_sorted_array

def test_heapSort():
    sorted_array = algorithms.Sorting().heapSort(unsorted_array)
    assert sorted_array == pre_sorted_array

def test_heapSort():
    sorted_array = algorithms.Sorting().heapSort(unsorted_array)
    assert sorted_array == pre_sorted_array

def test_mergeSort():
    sorted_array = algorithms.Sorting().mergeSort(unsorted_array)
    assert sorted_array == pre_sorted_array

def test_bogoSort():
    sorted_array = algorithms.Sorting().bogoSort(unsorted_array)
    assert sorted_array == pre_sorted_array

