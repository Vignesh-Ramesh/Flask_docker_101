from flask import Flask,request

## POST request and GET Request
app = Flask(__name__)
@app.route('/',methods = ['POST'])

def add():
	
	a = request.form["a"] ## YOU WANT TO CHANGE IT TO FORM, this will take care of the post request, you don't want to enter the parameters in the URl
	a = int(a)
	b = request.form["b"]
	b = int(b)
	return str(a+b)

if __name__ == '__main__':
	app.run(port = 5000)


## How do i expose 	