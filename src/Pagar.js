import React, { Component } from 'react';
import Ac7 from './imagens/ac7.jpg'
import Voltar from './imagens/voltar.png'
import Botao from './imagens/botao.png'
import { Link } from 'react-router-dom'
import './Pagar.css'
var teste = "teste"
class Pagar extends Component{
    constructor(){
      super()
      this.state = {
        codigo: ""
      };
      this.onChange = (evento) =>{
        this.setState({codigo: evento.target.value});
      };
      this.onSubmit = (evento) =>{
        evento.preventDefault();
        console.log(this.state)
      }  
     }
    render(){
    return (
        <div className="App">
            <header className="App-header">
                <Link to = "/"><button className = "App-botao-voltar"><img src={Voltar} className="App-voltar" alt="voltar" /></button></Link>
            </header>
            <main ClassName= "main_pagar">
                <img src={Ac7} className="App-Ac7" alt="Ac7" />
                <br>
                </br>
                
                <br>
                </br>
            </main>
            <aside>
            </aside>
            <div className = "info-boleto">
                <br>
                </br>
                <text className = "text-boleto">Digite o código de barras na caixa de texto</text>
                <br></br>
                <text className = "text-boleto">abaixo ou escaneie usando o leitor</text>
                <br></br><br></br><br></br>
                <text>Código de barras: </text>
                <input type = "text" placeholder= "Código" value = {this.state.codigo} onChange = {this.onChange}></input>
                <br></br><br></br>
                <br></br>
                {this.state.codigo == teste ? (
                  <text className="text-error">Código invalido, tente novamente</text>
                ): (<button className = "App-botao-continuar" onClick = {this.onSubmit} ><img src={Botao} className="App-Botao2" alt="Botao2" /></button>)
                }
                
  
            </div>
        </div>
      );
}
}
export default Pagar;