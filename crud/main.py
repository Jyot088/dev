from flask import Flask,jsonify,request
import  json
app= Flask(__name__)
  
with open('main.json') as f:
    data=json.load(f)


#get all users
@app.route('/users', methods=['GET'])
def get_users():
     return jsonify(data['users'])

#get the user by specific id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in data['users']:
       if user['id']==user_id:
            return user
    return {'error':'User not found'}
       
        
#create the user
@app.route('/users', methods=['POST'])
def create_user():
    new_user={"id":len(data['users'])+1, 'name':request.json['name'], 'email':request.json['email'], 'age':request.json['age']}
    data['users'].append(new_user)
    return new_user
    
#update the user
@app.route('/users/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    for user in data['users']:
        if user['id']==user_id:
            user['name']=request.json['name']
            user['email']=request.json['email']
            user['age']=request.json['age']
            return user
    return {'error':'User not found'}


#delete the user
@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    for user in data['users']:
        if user['id']==user_id:
            data['users'].remove(user)
            return {"data":"User is Deleted successfully"}
    return{'error':'Book not found'}

#run the application
if __name__ =='__main__':
  app.run(debug=True)
