from flask import Flask, render_template, request                     
app = Flask(__name__,template_folder="template")          
                                                        
@app.route("/")
def hello():
    return 'Hello world' 


if __name__ == "__main__":
      app.run(debug=True ,port=8080,use_reloader=True) 
