import pickle

from flask import Flask,request
import numpy as np 
import xgboost as xgb 
#loads up the model file object
with open('./xgb.pkl','rb') as model_file:
	model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/predict',methods = ['GET'])

def predict_iris():

	s_length = request.args.get("s_length")
	s_length = float(s_length)
	s_width = request.args.get("s_width")
	s_width = float(s_width)
	p_length = request.args.get("p_length")
	p_length = float(p_length)
	p_width = request.args.get("p_width")
	p_width = float(p_width)

	data_f = np.array([[s_length,s_width,p_length,p_width]])
	pred_f = xgb.DMatrix(data_f)

	prediction = model.predict(pred_f)

	flower_pred = str(np.argmax(prediction))

	if flower_pred == '0':
		return ('The flower is most likely to be setosa' + '\U0001f600')
	elif flower_pred == '1':
		return ('The flower is most likely to be versicolor' + '\U0001f600')
	else:
		return('The flower is most likely to be virginica' + '\U0001f600')


if __name__ == '__main__':
	app.run()


