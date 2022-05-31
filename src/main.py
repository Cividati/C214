from flask import Flask, render_template, request        
import algorithms as algorithms

app = Flask(__name__,template_folder="template")          
                                                        
@app.route("/")
def hello():
    return 'Hello world' 

@app.route("/bubblesort")
def bubblesort():
      array = request.args.get('array')
  
      new_array = algorithms.Sorting.bubbleSort(array.split(','))

      response = f"Your array: {array.split(',')} Bubble sort: {new_array}"
 
      return response

if __name__ == "__main__":
      app.run(debug=True ,port=80,use_reloader=True) 
