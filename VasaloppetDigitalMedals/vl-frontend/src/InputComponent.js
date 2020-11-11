import React, { Component } from 'react';
import { Route, NavLink, HashRouter } from "react-router-dom";

export class InputComponent extends Component {
	
	constructor(props) {
		super();
		this.state = {
			inputText: props.searchValue,
		};
	}

	onInputChange(eventObject) {	
		this.setState({	
			inputText: eventObject.target.value
		});
	}

	onSearchClick() {
		console.log(this.state.inputText)
	}

	render() {
		return (
			<div className="input-box">
				<input 
					type="text" 
					onChange = { (e) => this.onInputChange(e)} 
					value={this.state.inputText} 
				/>
				<NavLink to="/Stuff">
					<button
						onClick = { this.onSearchClick.bind(this) } >
						{this.props.buttonValue}
					</button>
				</NavLink>
			</div>
		);
	}
}

export default InputComponent;