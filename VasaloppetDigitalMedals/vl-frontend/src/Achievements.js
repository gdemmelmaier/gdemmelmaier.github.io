import React from 'react';
import MedalComponent from './MedalComponent';
import {
  Icon,
  Table,
  Label,
  Flag,
  Grid,
  Segment,
  Divider
} from 'semantic-ui-react';

function status(res) {
  if (!res.ok) {
    throw new Error(res.statusText);
  }
  return res;
}

class Achivements extends React.Component {
  state = {
    isLoading: true
  };

  componentDidMount() {
    const id = this.props.match.params.id;

    //fetch(`/api/skiers?id=${id}`)
    fetch(`http://localhost:8080/api/skiers?id=${id}`)
      .then(status)
      .then(res => res.json())
      .then(data => {
        this.setState({
          isLoading: false,
          data: data
        });
      })
      .catch(e => {
        this.setState({
          error: e,
          isLoading: false
        });
      });
  }

  render() {
    if (this.state.isLoading) return <h1>Loading...</h1>;
    else if (this.state.error)
      return <h1>Något gick fel, finns någon med det valda ID?</h1>;
    else {
      const name = this.state.data.firstname + ' ' + this.state.data.lastname;
      const achievements = this.state.data.achievements;
      if (achievements.length > 0) {
        return (
          <div>
            <h1 className="name-title">{name}</h1>
            <div className="name-under-title">
              <Label color={'blue'}>
                <Flag name="se" />
                {this.state.data.club}
              </Label>
              <Label color={'blue'}>
                <Icon name="clock" />
                <Label.Detail>{this.state.data.finish}</Label.Detail>
                <Label.Detail>{this.state.data.class}</Label.Detail>
              </Label>
            </div>
            <h2 className="welldone-title">
              Bra jobbat! Här är dina finaste prestationer (än så länge).
            </h2>
            <MedalComponent achievements={achievements} />
          </div>
        );
      } else {
        return (
          <div>
            <h1 className="name-title">{name}</h1>
            <MedalComponent achievements={achievements} />
            <h2 className="welldone-title">
              Anmäl dig till nästa års lopp för nya chanser till medaljer!
            </h2>
          </div>
        );
      }
    }
  }
}

export default Achivements;
