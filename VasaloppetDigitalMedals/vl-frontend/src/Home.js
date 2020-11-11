import React, { Component } from 'react';
import SearchBar from './SearchBar.js';

// Content page 1
class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div className="homeArea">
        <h1 className="home-title">Hämta dina digitala medaljer</h1>
        <SearchBar />
      </div>
    );
  }
}

export default Home;
