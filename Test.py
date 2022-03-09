from flask import Flask
from flask import jsonify
import Model1
import Model1_Title
import Model2_Title
import Model3_Title
import Model2
import Model3


app = Flask(__name__)



@app.route("/<text>/<model_name>")
def Controler(text,model_name):
    if model_name == "Model1":
        d=Model1.Predict(text)
        result=jsonify(d)
        return result
    elif model_name == "Model1_Title":
        d=Model1_Title.Predict(text)
        result=jsonify(d)
        return result
    elif model_name == "Model2_Title":
        d=Model2_Title.Predict(text)
        result=jsonify(d)
        return result
    elif model_name == "Model2":
        d=Model2.Predict(text)
        result=jsonify(d)
        return result
    elif model_name == "Model3":
        d=Model3.Predict(text)
        result=jsonify(d)
        return result
    elif model_name == "Model3_Title":
        d=Model3_Title.Predict(text)
        result=jsonify(d)
        return result
    
    elif model_name == "TrainModel1":
        # Load the model from disk
        path=os.path.abspath(os.getcwd())
        Model1.Train_Model(path+'/train.csv')
        return "Model1 Trained Successfully..."

    elif model_name == "TrainModel1-Title":
        # Load the model from disk
        path=os.path.abspath(os.getcwd())
        Model1_Title.Train_Model(path+'/train.csv')
        return "Model4 Trained Successfully..."

    elif model_name == "TrainModel2-Title":
        # Load the model from disk
        path=os.path.abspath(os.getcwd())
        Model2_Title.Train_Model(path+'/train.csv')
        return "Model2-Title Trained Successfully..."

    elif model_name == "TrainModel3-Title":
        # Load the model from disk
        path=os.path.abspath(os.getcwd())
        Model3_Title.Train_Model(path+'/train.csv')
        return "Model3-Title Trained Successfully..."

if __name__ == '__main__':
    app.run()