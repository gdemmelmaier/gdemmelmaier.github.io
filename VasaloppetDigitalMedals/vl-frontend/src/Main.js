import React, { Component } from 'react';
import { Route, NavLink, HashRouter } from 'react-router-dom';
import VLlogo from './img/vl_logo.svg';
import './styles.css';

// Importera respektive "component-set" från de andra modulerna(?)
import Home from './Home';
import Achievements from './Achievements';

// We have our app frame here.
// There is a close correlation between what URL your navigation links
// specify and the content that ultimately gets loaded.
class Main extends Component {
  render() {
    let icon = VLlogo;

    return (
      <HashRouter>
        <div>
          <div className="top-of-page">
            <NavLink to="/">
              <img id="vl-logo" alt="vasa-logo-should-show-here" src={icon} />
            </NavLink>
            <div id="powered-by-ibm">
              Powered by <strong>IBM</strong>
            </div>
          </div>
          <div className="content">
            <Route exact path="/" component={Home} />
            <Route path="/achievements/:id" component={Achievements} />
          </div>
        </div>
      </HashRouter>
    );
  }
}

export default Main;
