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

@app.route('/webhook', methods=['POST'])
def webhook():
    print("APP - Consulta entrando...")
    print(datetime.now())
    print("")

    print("Pregunta por POST?")
    if request.method == 'POST':
        print("Si..")
        print("Que viene viajando")
        print(request.__dict__.items())
         # request.form returns an ImmutableMultiDict of keys and values
        req = request.form
        print(req)
        # Get individual form values based on the name attribute
        verify_token = request.form.get("token")
        print(verify_token)
        event = request.form.get("event")
        print(event)
        # Finaliza respondiendo Ok
        return jsonify({"success": True}), 200

    else:
        print("No Datos POST...")
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
