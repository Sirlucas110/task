from flask import Flask, jsonify, request

from model.Usuario import getId, getUsers

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():

    users = getUsers()

    lista_usuarios = [{

        "id": user[0], 
        'name': user[1], 
        'email': user[2]} 
        
        for user in users]
    return jsonify(lista_usuarios)

@app.route('/user', methods=['GET'])

def getUserId():
    user_id = request.args.get('id', type=int)

    user = getId(user_id)

    usuario_id = {

        "id": user[0],
        'name': user[1], 
        'email': user[2]
        }
    return jsonify(usuario_id)



if __name__ == '__main__':
    app.run()