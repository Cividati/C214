from flask import Flask, render_template, request   
import algorithms as algorithms     

app = Flask(__name__,template_folder="template")          
                                                        
@app.route("/")
def hello():
	arg_frase = request.args.get('frase')
	
	return f'''Input: {arg_frase}<br>
			   Numero de palavras: {algorithms.wordCount(arg_frase)} <br>
			   Numero de palavras pares: {algorithms.pairWords(arg_frase)} '''

if __name__ == "__main__":
      app.run(debug=True ,port=80,use_reloader=True) 