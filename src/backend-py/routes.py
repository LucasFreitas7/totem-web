from flask import Flask, jsonify, request
from ServicoDAO import *
from flask_cors import CORS
import ctypes
from ctypes import *
import os

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
            servico.setIcupom(1)
            strchr = lib.RecargaCelular
            strchr.restype = c_char_p
            string_nova = strchr(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_int(servico.iCupom), c_int(servico.iLeitor))
            if(string_nova[0] == 83 and string_nova[1] == 59 and string_nova[2] == 49 and string_nova[3] == 59 and string_nova[4] == 84 and string_nova[5] == 114 and string_nova[6] == 97 and string_nova[7] == 110 and string_nova[8] == 115 and string_nova[9] == 97 and string_nova[10] == 99 and string_nova[11] == 97 and string_nova
            [12] == 111):
                print("sera processado")
                lib.Confirmar(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_int(servico.iCupom))
                return jsonify({'status' : "Recarga celular processado com sucesso"})

            else:
                print("qualquer erro nao sera processado")
                return jsonify({'status' : "Erro no processamento"})
        except:
            return jsonify({'status' : "Erro no processamento"})
   


@app.route("/vendecredito", methods = ["GET"])

def requisicaoVendeCredito():
        try:
            request.headers['acesso']
            servico.setIcupom(2)
            strchr = lib.VendeCredito
            strchr.restype = c_char_p
            string_nova = strchr(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_double(servico.dValor), c_int(servico.iCupom), c_int(servico.iLeitor))
            print("---------------------------------------------------")
            if(string_nova[0] == 83 and string_nova[1] == 59 and string_nova[2] == 49 and string_nova[3] == 59 and string_nova[4] == 84 and string_nova[5] == 114 and string_nova[6] == 97 and string_nova[7] == 110 and string_nova[8] == 115 and string_nova[9] == 97 and string_nova[10] == 99 and string_nova[11] == 97 and string_nova
            [12] == 111):
                print("sera processado")
                arquivo = open("impressao.txt", "w")
                print("chegou aq teste ")
                tamanho = len(string_nova)
                print(tamanho)
                i = 0
                for i in range(tamanho):
                    teste = chr(string_nova[i])
                    print(teste)
                    arquivo.write(teste)
                
                string_teste = "impressao.txt"
                os.startfile(string_teste, 'print')
                lib.Confirmar(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_int(servico.iCupom))
                return jsonify({'status' : "Venda credito processado com sucesso"})

            else:
                print("qualquer erro nao sera processado")
                return jsonify({'status' : "Erro no processamento"})
            
            
        except:
            return jsonify({'status' : "Erro no processamento"})

@app.route("/vendedebito", methods = ["GET"])

def requisicaoVendeDebito():
        try:
            request.headers['acesso']
            servico.setIcupom(3)
            lib.VendeDebito(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_double(servico.dValor), c_int(servico.iCupom), c_int(servico.iLeitor))
            print("Requisição para chamar a venda debito")
            return jsonify({'status' : "Venda debito processado com sucesso"})
        except:
            return jsonify({'status' : "Erro no processamento"})
        
@app.route("/vendecreditoparcelado", methods = ["GET"])

def vendeCreditoParcelado():
        try:
            request.headers['acesso']
            servico.setIcupom(4)
            lib.VendeCreditoParcLoja(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_int(parcelas.iParcelas), c_double(servico.dValor), c_int(servico.iCupom), c_int(servico.iLeitor))
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
            servico.setIcupom(5)
            lib.Reimpressao(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro),c_double(servico.dValor), c_int(servico.iCupom), c_int(1))
            print("Requisição para reimpressao")
            return jsonify({'status' : "Reimpressao processado com sucesso"})
        except:
            return jsonify({'status' : "Erro no processamento"})

@app.route("/relatorio", methods = ["GET"])

def requisicaoRelatorio():
        try:
            request.headers['acesso']
            servico.setIcupom(6)
            lib.Relatorio(ctypes.c_char_p(new_sCNPJCliente),ctypes.c_char_p(new_sCNPJParceiro), c_int(servico.iCupom), c_int(1))
            print("Requisição para relatorio")
            return jsonify({'status' : "Relatorio processado com sucesso"})
        except:
            return jsonify({'status' : "Erro no processamento"})

app.run()