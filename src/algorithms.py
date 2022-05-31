class Sorting:

    def bubbleSort(array):
        for i in range(len(array)):
            already_sorted = True

            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

                    already_sorted = False

            if already_sorted:
                break

        return array