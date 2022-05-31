from flask import Flask, render_template, request        
import algorithms as algorithms

app = Flask(__name__,template_folder="template")          
                                                        
@app.route("/")
def hello():
    return 'Hello world' 

@app.route("/bubblesort")
def bubblesort():
	arg_string = request.args.get('array')
	converted_array = algorithms.convert(arg_string)
	sorted_array = algorithms.Sorting().bubbleSort(converted_array)

	return f"Your array: {arg_string} <br>Bubble sort: {sorted_array}"

@app.route("/insertionsort")
def insertionSort():
	arg_string = request.args.get('array')
	converted_array = algorithms.convert(arg_string)
	sorted_array = algorithms.Sorting().insertionSort(converted_array)

	return f"Your array: {arg_string} <br>Insertion sort: {sorted_array}"

@app.route("/heapsort")
def heapSort():
	arg_string = request.args.get('array')
	converted_array = algorithms.convert(arg_string)
	sorted_array = algorithms.Sorting().heapSort(converted_array)

	return f"Your array: {arg_string} <br>Heap sort: {sorted_array}"

@app.route("/mergesort")
def mergeSort():
	arg_string = request.args.get('array')
	converted_array = algorithms.convert(arg_string)
	sorted_array = algorithms.Sorting().mergeSort(converted_array)

	return f"Your array: {arg_string} <br>Merge sort: {sorted_array}"

@app.route("/bogosort")
def bogoSort():
	arg_string = request.args.get('array')
	converted_array = algorithms.convert(arg_string)
	sorted_array = algorithms.Sorting().bogoSort(converted_array)

	return f"Your array: {arg_string} <br>Bogo sort: {sorted_array}"

if __name__ == "__main__":
      app.run(debug=True ,port=80,use_reloader=True) 