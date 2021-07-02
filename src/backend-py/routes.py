from flask import Flask, jsonify, request
from ctypes import *
from ServicoDAO import *
from flask_cors import CORS
import ctypes

servico =  Servicos("60177876000130", "61492096000147", 30, 1, 1)
parcelas = Parcelas("60177876000130", "61492096000147", 2,  30, 1, 1)
lib = WinDLL(r".\\TefClientmc.dll")

ctypes.c_wchar_p()
new_sCNPJCliente = servico.sCNPJCliente.encode('utf-8')
new_sCNPJParceiro = servico.sCNPJParceiro.encode('utf-8')
#var = lib.VendeCredito(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_double(30.5),c_int(1), c_int(1))

#  print(f"{lib.VendeCredito}")

app = Flask("BackTotem")
CORS(app)
@app.route("/recargacelular", methods = ["GET"])

def requisicaoRecarga():
        try:
            request.headers['acesso']
            lib.RecargaCelular(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_int(servico.iCupom), c_int(servico.iLeitor))
            servico.iCupom + 1
            print("Requisição para chamar a Recarga")
            return jsonify({'status' : "Recarga processada com sucesso"})
        except:
            return jsonify({'status' : "Erro no processamento"})
   


@app.route("/vendecredito", methods = ["GET"])

def requisicaoVendeCredito():
        try:
            request.headers['acesso']
            lib.VendeCredito(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_double(servico.dValor), c_int(servico.iCupom), c_int(servico.iLeitor))
            servico.iCupom + 1
            print("Requisição para chamar a venda credito")
            return jsonify({'status' : "Venda credito processado com sucesso"})
        except:
            return jsonify({'status' : "Erro no processamento"})

@app.route("/vendedebito", methods = ["GET"])

def requisicaoVendeDebito():
        try:
            request.headers['acesso']
            lib.VendeDebito(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_double(servico.dValor), c_int(servico.iCupom), c_int(servico.iLeitor))
            servico.iCupom + 1
            print("Requisição para chamar a venda debito")
            return jsonify({'status' : "Venda debito processado com sucesso"})
        except:
            return jsonify({'status' : "Erro no processamento"})
        
@app.route("/vendecreditoparcelado", methods = ["GET"])

def vendeCreditoParcelado():
        try:
            request.headers['acesso']
            lib.VendeCreditoParcLoja(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_int(parcelas.iParcelas), c_double(servico.dValor), c_int(servico.iCupom), c_int(servico.iLeitor))
            servico.iCupom + 1
            print("Requisição para chamar a venda credito parcelado")
            return jsonify({'status' : "Venda credito parcelado processado com sucesso"})
        except:
            return jsonify({'status' : "Erro no processamento"})

@app.route("/cancelar", methods = ["GET"])

def requisicaoCancelamento():
        try:
            request.headers['acesso']
            lib.Cancelar(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro), c_double(servico.dValor))
            print("Requisição para cancelamento")
            return jsonify({'status' : "Cancelamento processado com sucesso"})
        except:
            return jsonify({'status' : "Erro no processamento"})


@app.route("/reimpressao", methods = ["GET"])

def requisicaoReimpressao():
        try:
            request.headers['acesso']
            lib.Reimpressao(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_double(servico.dValor), c_int(servico.iCupom), c_int(1))
            print("Requisição para reimpressao")
            return jsonify({'status' : "Reimpressao processado com sucesso"})
        except:
            return jsonify({'status' : "Erro no processamento"})

@app.route("/relatorio", methods = ["GET"])

def requisicaoRelatorio():
        try:
            request.headers['acesso']
            lib.Relatorio(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro), c_int(servico.iCupom), c_int(1))
            print("Requisição para relatorio")
            return jsonify({'status' : "Relatorio processado com sucesso"})
        except:
            return jsonify({'status' : "Erro no processamento"})

app.run()