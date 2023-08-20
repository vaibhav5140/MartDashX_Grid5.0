from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
import pickle
import random


loaded_prediction_data=None
with open("data.pickle", "rb") as f:
    loaded_prediction_data = pickle.load(f)

def getListOfUser(user_id,top_n,n=10):
  try:
    recommended_items = [item[0] for item in top_n[user_id]]
    print(f"Top recommended items for user {user_id}: {recommended_items}")
    return recommended_items
  except KeyError:
    print(f"User {user_id} not found in the recommendations.")


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/getitemlistforeachuser')
def getitemlistforeachuser():
    try:
        output_list = []

        for key, value in loaded_prediction_data.items():
            user_id = int(key)
            item_list = [int(item[0]) for item in value]
            output_list.append({"user_id": user_id, "item_list": item_list})
        return jsonify(output_list),200
    except Exception as e:
        error_message = f"Something went Wrong on our side!!!"
        return jsonify({"error": error_message}), 500
        

@app.route('/getitemforrandomuser')
def getitemforrandomuser():
    
    
    try:
        
    
        random_user_id=random.choice(list(loaded_prediction_data.keys()))

        

        list_reco=getListOfUser(random_user_id,loaded_prediction_data)
        list_reco = [int(round(x)) for x in list_reco]
        return jsonify({"userid":random_user_id,"items":list_reco}),200
        
    except Exception as e:
        error_message = f"User not found "
        return jsonify({"error": error_message}), 500

@app.route('/getitemforuser',methods=['POST'])
def getitemforuser():
    try:
        user_id=int(request.get_json().get('userid'))
        list_reco=getListOfUser(user_id,loaded_prediction_data)
        list_reco = [int(round(x)) for x in list_reco]
        return jsonify({"userid":user_id,"items":list_reco}),200
    except Exception as e:
        
        error_message = f"User not found "
        return jsonify({"error": error_message}), 500
         

if __name__ == '__main__':
    app.run()