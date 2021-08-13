import React from 'react';
import { BrowserRouter, BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Home from './Home'
import Pagar from './Pagar'
import Recarga from './Recarga'
import Emprestimo from './Emprestimo'
import Emprestimo_Consig from './Emprestimo_Consig';

export default function Routes(){
    return(
        <BrowserRouter>
           <Switch>
               <Route exact path = '/' component= {Home}/>
               <Route path = '/pagar' component= {Pagar}/>
               <Route path = '/Recarga' component = {Recarga}/>
               <Route path = '/Emprestimo' component = {Emprestimo}/>
               <Route path = '/EmprestimoConsignado' component = {Emprestimo_Consig}/>
           </Switch>
        </BrowserRouter>

    )
}