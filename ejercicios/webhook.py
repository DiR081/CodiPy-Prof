import os
from datetime import datetime, timedelta
from flask import Flask, request, abort, jsonify

def temp_token():
    import binascii
    temp_token = binascii.hexlify(os.urandom(24))
    return temp_token.decode('utf-8')

WEBHOOK_VERIFY_TOKEN = os.getenv('WEBHOOK_VERIFY_TOKEN', default='DiRo-api-key')
CLIENT_AUTH_TIMEOUT = 240 # in Hours
NOMBRE_ARCHIVO = "/home/Soporte1/AmbientesPy/requestWaBox/raiz/logwebhook.txt"

app = Flask(__name__)

authorised_clients = {'54.38.177.76': 1 }

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    print("APP - Consulta entrando...")
    print(datetime.now())

    print("Pregunta por GET?")
    if request.method == 'GET':
        print("Si.")
        verify_token = request.args.get('token')
        if verify_token == WEBHOOK_VERIFY_TOKEN:
            print("- Token Key Correcta")
            authorised_clients[request.remote_addr] = datetime.now()
            # Guardamos en el archivo IP Conexión
            archivo = open(NOMBRE_ARCHIVO, 'a')
            archivo.write(str(request.remote_addr) + " : " + str(datetime.now()) + "\n")
            archivo.close()
            return jsonify({'status':'success'}), 200
        else:
            print("- Token Key Incorrecta")
            print(authorised_clients)
            return jsonify({'status':'token errado'}), 401
    else:
        print("No.")

    print("Pregunta por POST?")
    if request.method == 'POST':
        print("Si..")
        verify_token = request.args.get('token')
        client = request.remote_addr
        print("El Token de verificación enviado es: %s" %verify_token)
        print("La IP del cliente es %s" %client)
        archivo = open(NOMBRE_ARCHIVO, 'r')
        datos_archivo = archivo.read() # IPs
        archivo.close()
        #if client in authorised_clients:
        print("Pregunta por Cliente en Listado?")
        if client in datos_archivo:
                print("Si.")
                print("Son JSON los datos?", request.is_json)
                print("Los datos pasados por el Cliente get_json:")
                content = request.get_json()
                print(content)
                print("Los datos pasados por el Cliente args.get:")
                print(request.json)
                print(request.args.get('event'))
                print(request.args.get('uid'))
                print(request.args.get('cuid'))
                print(request.args.get('ack'))

                return jsonify({'status':'success'}), 200
        else:
            print("No.")
            return jsonify({'status':'No Autorizado'}), 401

    else:
        print("No..")
        abort(400)
    # Fin

if __name__ == '__main__':
    if WEBHOOK_VERIFY_TOKEN is None:
        print('WEBHOOK VERIFY TOKEN no se ha configurado en el entorno.\nGenerando token aleatorio ...')
        token = temp_token()
        print('Token Iniciado, con valor:\n %s' % token)
        WEBHOOK_VERIFY_TOKEN = token
    print("El Token esperado es %s" %WEBHOOK_VERIFY_TOKEN)
    print("APP - Iniciada.")
    print("")
    app.run(debug=True, host='149.56.143.149')

#
