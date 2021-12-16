from flask import Flask, render_template, request
import pickle
import os
import numpy as np

#DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'model.pkl')
#def multi():
def create_app():
   
   model = pickle.load(open('model.pkl', 'rb'))
   app = Flask(__name__)
#app.register_blueprint(model.bp)
 
   @app.route('/')
   def index():
    return render_template('index.html')

   @app.route('/result', methods=['POST'])
   def home():
      asetscp = request.form['asetscp']
      bctotam = request.form['bctotam']
      capt = request.form['capt']
      array = np.array([[asetscp, bctotam, capt]])
      predict = model.predict(array)
      return render_template('result.html', predict=predict)

   if __name__ =='__main__':
      app.run(debug=True)
   
   return app
'''with open('model.pkl','rb') as pickle_file:
   model = pickle.load(pickle_file)'''