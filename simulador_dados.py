import random
import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("credenciais.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://iot-monitor-5ca0c-default-rtdb.firebaseio.com/"
})

ref = db.reference("leituras")

while True:
    temperatura = round(random.uniform(20, 30), 2)
    umidade = round(random.uniform(50, 80), 2)
    dados = {
        "temperatura": temperatura,
        "umidade": umidade,
        "timestamp": datetime.now().isoformat()
    }
    ref.push(dados)
    print("Enviado:", dados)
    time.sleep(2)
