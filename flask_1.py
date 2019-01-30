from flask import Flask,request

app = Flask(__name__)
@app.route('/')

def add():
	
	a = request.args.get("a")
	a = int(a)
	b = request.args.get("b")
	b = int(b)
	return str(a+b)

if __name__ == '__main__':
	app.run()


## How do i expose 	