import React from 'react';
import { BrowserRouter, BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Home from './Home'
import Pagar from './Pagar'

export default function Routes(){
    return(
        <BrowserRouter>
           <Switch>
               <Route exact path = '/' component= {Home}/>
               <Route path = '/pagar' component= {Pagar}/>
           </Switch>
        </BrowserRouter>

    )
}