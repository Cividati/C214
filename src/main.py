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
	new_array = algorithms.Sorting().bubbleSort(converted_array)
	response = f"Your array: {arg_string} <br>Bubble sort: {new_array}"

	return response


if __name__ == "__main__":
      app.run(debug=True ,port=80,use_reloader=True) 