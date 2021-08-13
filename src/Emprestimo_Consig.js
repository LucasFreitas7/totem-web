import React, { Component } from 'react';
import Ac7 from './imagens/ac7.jpg'
import Voltar from './imagens/voltar.png'
import { Link } from 'react-router-dom'
import './Emprestimo_Consig.css'
import Propaganda from './imagens/propaganda.png'
import QRcode_Consig from './imagens/qrcode_consig.png'
class Emprestimo_Consig extends Component{
    render(){
        return(
            <div className = "App">
                <header >
                    <Link to  = "/">
                        <button className = "App-botao-voltar">
                            <img src={Voltar} className="App-voltar" alt="voltar" />
                        </button>
                    </Link>
                </header>
                <main>
                    <img src={Ac7} className="App-Ac7" alt="Ac7" />
                </main>
                <aside className = "Teste">
                </aside>
                <div className = "div_info_pag2">
                    <div className = "div_info_text">
                    <text className = "App-text1">EMPRÉSTIMO SEM BUROCRACIA</text><br></br>
                    <text className = "App-text3">Conheça nossas soluções de crédito e contrate seu</text><br></br>
                    <text className = "App-text3">empréstimo online, de forma rápida, fácil e segura.</text><br></br>
                    <text className = "App-text3">● Empréstimo Consignado</text><br></br>
                    <text className = "App-text3">● Refinanciamento</text><br></br>
                    <text className = "App-text3">● Cartão Consignado</text><br></br>
                    <text className = "App-text3">● Saque Aniversário FGTS</text><br></br>
                    <text className = "App-text3">● Crédito Pessoal</text>
                    </div>
                    <div className = "div_info_img">
                        <img src={Propaganda} className="App-Propaganda" alt="Propaganda" />
                    </div>
                </div>
                <div>

                </div>
                <div>
                    <p className = "App-text3"><text className= "App-text1">Como fazer sua solitcitação?</text> Basta apontar a camera do seu celular para o QRCode abaixo, você será apontado diretamente para nosso site de Emprestimo Consignado, FGTS e outros do AC7 Pay, simule na hora e já faça seu pedido pelo celular.</p>
                    <img src={QRcode_Consig} className="App-QRcode_Consig" alt="QRcode_Consig" />
                    <p className = "App-text4"><text className = "App-text1">Link: </text>  https://cobrancas.ac7pay.com/emprestimos/</p>
                </div>
            </div>
        )
    }
}
export default Emprestimo_Consig