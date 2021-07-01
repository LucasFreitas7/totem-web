from flask import Flask, jsonify, request
from ctypes import *
from flask_cors import CORS
import ctypes


lib = WinDLL(r".\\TefClientmc.dll")

ctypes.c_wchar_p()
sCNPJCliente = "60177876000130"
sCNPJParceiro = "61492096000147"
new_sCNPJCliente = sCNPJCliente.encode('utf-8')
new_sCNPJParceiro = sCNPJParceiro.encode('utf-8')

#var = lib.VendeCredito(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_double(30.5),c_int(1), c_int(1))

#  print(f"{lib.VendeCredito}")

app = Flask("BackTotem")
CORS(app)
@app.route("/recargacelular", methods = ["GET"])

def requisicaoRecarga():
        try:
            request.headers['acesso']
            lib.RecargaCelular(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_int(1), c_int(1))
            print("Requisição para chamar a dll")
            return jsonify({'status' : "Processado com sucesso"});
        except:
            return jsonify({'status' : "Erro no processamento"});
   
app.run()
