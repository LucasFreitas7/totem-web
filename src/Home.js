import React from 'react'
import Ac7 from './imagens/ac7.jpg'
import Botao_Pagar from './imagens/botao_pagar.jpg'
import Menu from './imagens/menu.png'
import Playstore from './imagens/play_store.jpg'
import Appstore from './imagens/app_store.png'
import QRcode1 from './imagens/qrcode_appstore.png'
import QRcode2 from './imagens/qrcode_playstore.png'
import { Link } from 'react-router-dom'
import './Home.css'
function Home() {
  return (
    <div className="App">
      <header className="App-header">
         <img src={Menu} className="App-Menu" alt="Menu" />
      </header>
      <main ClassName= "App-corpo">
        <img src={Ac7} className="App-Ac7" alt="Ac7" />
      </main>
      <aside>
      </aside>
      <footer>
        <Link to="/pagar">  <button className="App-botao-pagar"><img src={Botao_Pagar} className="App-Pagar" alt="Pagar" />
        </button></Link>
        <br>
        </br>
        <text className="App-label-text">Abre AGORA sua conta digital GRÁTIS,  Escaneie o QRcode e CADASTRE-SE</text>
        <br>
        </br>
        <img src={Playstore} className="App-Playstore" alt="Playstore" />
        <img src={Appstore} className="App-Appstore" alt="Appstore" />
        <br>
        </br>
        <img src={QRcode2} className="App-QRCODE2" alt="qrcode2" />
        <img src={QRcode1} className="App-QRCODE1" alt="qrcode1" />
      </footer>
    </div>
  );
}

export default Home;
