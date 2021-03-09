from flask import Flask, jsonify, request, render_template, Markup
app = Flask(__name__)

carros = [
    {
        'modelo': 'HB20',
        'velocidade_max': '180.0',
        'motor': '1.6',
        'marca': 'Hyundai'
    },

    {
        'modelo': 'XC60',
        'velocidade_max': '175.0',
        'motor': '2.0',
        'marca': 'Volvo'
    },

    {
        'modelo': 'Compass',
        'velocidade_max': '195.0',
        'motor': '2.0',
        'marca': 'Jeep'
    },

    {
        'modelo': 'Fox',
        'velocidade_max': '160.0',
        'motor': '1.6',
        'marca': 'Volkswagen'
    },

    {
        'modelo': 'Evoque',
        'velocidade_max': '185.0',
        'motor': '2.0',
        'marca': 'Land Rover'
    },

    {
        'modelo': 'Polo',
        'velocidade_max': '195.0',
        'motor': '1.6',
        'marca': 'Volkswagen'
    }


]


@app.route('/')
def inicio():
    return render_template('web/inicio.html', carros=carros)


@app.route('/carros', methods=['GET'])
def home():
    return jsonify(carros), 200


@app.route('/carros/<string:motor>', methods=['GET'])
def MotorCarro(motor):
    MotorCarro = [dev for dev in carros if dev['motor'] == motor]
    return jsonify(MotorCarro), 200


@app.route("/carros/<string:modelo>", methods=['PUT'])
def mudar_modelos(modelo):
    for dev in carros:
        if dev['modelo'] == modelo:
            dev['motor'] = request.get_json().get('motor')

            return jsonify(dev), 200

    return jsonify({'error': 'modelo nao encontrado'}), 404


@app.route('/carros', methods=['POST'])
def salvar_carros():
    data = request.get_json()
    carros.append(data)

    return jsonify(data), 201


@app.route('/carros/<string:modelo>', methods=['DELETE'])
def remove_car(modelo):
    index = modelo
    del carros[index]

    return jsonify({'message': 'Carro deletado com sucesso'}), 200


if __name__ == '__main__':
    app.run(debug=True)
