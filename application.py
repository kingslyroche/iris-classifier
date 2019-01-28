from flask import Flask,render_template,request
from joblib import dump, load
import numpy as np

from werkzeug import datastructures


model=load('iris.joblib')


application = Flask(__name__)

application.config["TEMPLATES_AUTO_RELOAD"] = True



@application.route("/" , methods=["GET", "POST"])
def index():
        request.parameter_storage_class =datastructures.ImmutableOrderedMultiDict

        if request.method == "POST":
                list=[]
                
                for _,values in request.form.items():
                    list.append(values)

                

                pred = model.predict(np.array(list).reshape(1, -1))[0]
                
                return render_template('index.html',pred=pred,data=request.form)

        return render_template('index.html')


if __name__ == '__main__':
   application.run(debug=True)
