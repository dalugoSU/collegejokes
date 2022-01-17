from flask import Flask
from flask import Flask
from flask_restful import Api, Resource, reqparse
from jokes import jokes
import random


class Joke(Resource):
    
    def get(self, id_=0):
        if id_==0:
            return {"joke": random.choice(jokes)}, 200
        
        for joke in jokes:
            if joke["id"] == id_:
                return {"joke": joke}, 200
        
        return "ID out of bounds...", 404
    
    def post(self, id_):
        parser = reqparse.RequestParser()
        parser.add_argument("joke")
        parser.add_argument("joke_response")
        params = parser.parse_args()
        
        for joke in jokes:
            if id_ == joke["id"]:
                return f"Joke with id {id_} already exists", 400
        
        joke = {
            "id": int(id_),
            "joke": params["joke"],
            "joke_response": params["joke_response"]
        }
        
        jokes.append(joke)
        return joke, 201
    
    def put(self, id_):
        parser = reqparse.RequestParser()
        parser.add_argument("joke")
        parser.add_argument("joke_response")
        params = parser.parse_args()
        
        for joke in jokes:
            if id_ == jokes["id"]:
                joke["joke"] = params["joke"]
                joke["joke_response"] = params["joke_response"]
                return joke, 200
        
        joke = {
            "id": id_,
            "joke": params["joke"],
            "joke_response": params["joke_response"]
        }
        
        jokes.append(joke)
        return joke, 201
    
    def delete(self, id_):
        global jokes
        jokes = [joke for joke in jokes if joke["id"] != id_]
        return f"Joke with id {id_} is deleted", 200
        

app = Flask(__name__)
api = Api(app)

api.add_resource(Joke, "/jokes", "/jokes", "/jokes/<int:id>")

if __name__ == "__main__":
    app.run(debug=False)
