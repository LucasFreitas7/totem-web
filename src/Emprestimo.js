import React, { Component } from 'react';
import Ac7 from './imagens/ac7.jpg'
import Voltar from './imagens/voltar.png'
import { Link } from 'react-router-dom'
import Analise from './imagens/analise.png'
import JurosBaixos from './imagens/jurosbaixos.png'
import Digital from './imagens/digital.png'
import Receba from './imagens/receba.png'
import './Emprestimo.css'
import QRcode from './imagens/qrcode.png'
class Emprestimo extends Component{
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
                <div className = "div_qrcode">
                    <div className = "div_imagens">
                        <img src={Receba} className="App-Receba" alt="Receba" />
                        <img src={JurosBaixos} className="App-JurosBaixos" alt="JurosBaixos" />
                        <br>
                        </br>
                        <img src={Analise} className="App-Analise" alt="Analise" />
                        <img src={Digital} className="App-Digital" alt="Digital" />
                    </div>
                    <div className = "div_info">
                        <br></br>
                        <text className= "App-text1">EMPRÉSTIMO PESSOA JURÍDICA</text>
                        <br></br>
                        <p className= "App-text3"><text className = "App-text2">Crédito à jato</text> para as pequenas e médias empresas  retomarem a dinâmica de seus negócios, disponibilizando capital de giro de forma rápida, desburocratizada e simples.</p>
                        <br></br>
                        <text className= "App-text1">EMPRÉSTIMO PESSOAL</text>
                        <br></br>
                        <p className= "App-text3"><text className = "App-text2">Ajuda rápida nas decisões de reorganizar a sua vida pessoal:</text> Reformar a casa, reorganizar as finanças, abrir seu negócio, fazer a viagem dos sonhos, com o nosso empréstimo pessoal sorria para o mundo e ele sorri de volta pra você.</p>
                    </div>    
                </div>
                <div>
                </div>
                <div>
                    <p className = "App-text3"><text className= "App-text1">Como fazer sua solitcitação de empréstimo?</text> Basta apontar a camera do seu celular para o QRCode abaixo, você será apontado diretamente para nosso site de micro crédito do AC7 Pay, simule na hora e já faça seu pedido pelo celular.</p>
                    <img src={QRcode} className="App-QRcode" alt="QRcode" />
                    <p className = "App-text7"><text className = "App-text6">Link: </text>  https://ac7pay.caas.digital/</p>
                </div>
            </div>
        )
    }
}
export default Emprestimo