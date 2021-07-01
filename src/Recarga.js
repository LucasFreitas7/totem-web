import React, { Component } from 'react';
import Ac7 from './imagens/ac7.jpg'
import Voltar from './imagens/voltar.png'
import Botao_Iniciar from './imagens/botao_iniciar.png'
import { Link } from 'react-router-dom'
import './Recarga.css'
import api from './api';
class Recarga extends Component{
    state = {
        recarga: [],
    }
    render(){
        return(
            <div className="App">
                <header className="App-header">
                <Link to  = "/">
                    <button className = "App-botao-voltar">
                        <img src={Voltar} className="App-voltar" alt="voltar" />
                    </button>
                </Link>
                </header>
                <main ClassName= "Main_recarga">
                   <img src={Ac7} className="App-Ac7" alt="Ac7" />
                    <br>
                    </br>
                    <br>
                    </br>
                </main>
                <aside>
                </aside>
                <div className = "Info-recarga">
                    <text className = "Text">Para iniciar o processo de recarga no celular, clique no botão iniciar abaixo.</text>
                    <br></br>
                    <button className = "App-botao-iniciar"onClick={(e) => {
                      e.preventDefault();
                      const response = api.get('');
                      this.setState({recarga: response.data});
                    }}><img src={Botao_Iniciar} className="App-Iniciar" alt="Iniciar" /></button>
                </div>
            </div>
            
        )
    }
}
export default Recarga;