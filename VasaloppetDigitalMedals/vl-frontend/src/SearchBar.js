import React, { Component } from 'react';
import { withRouter } from 'react-router';
import { Header, Search, Label, Grid, Segment, Flag } from 'semantic-ui-react';
import _ from 'lodash';

const resultRenderer = ({ title, startClass, club, nationality }) => (
  <div className="result-ind-design">
    <p>
      <Grid columns="equal" relaxed stretched>
        <Grid.Column className="result-ind-nationality">
          <Segment basic>
            <Flag name="se" />
            {/*<Label content={nationality} />*/}
          </Segment>
        </Grid.Column>
        <Grid.Column width={8}>
          <Segment basic>
            <p>
              <strong className="result-ind-title">{title}</strong>
            </p>
            <p>{club}</p>
          </Segment>
        </Grid.Column>
        <Grid.Column>
          <Segment basic>
            <Label className="result-ind-class" content={startClass} />
          </Segment>
        </Grid.Column>
      </Grid>
    </p>
  </div>
);

class SearchBar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      id: ''
    };
    this.handleSearchChange = this.handleSearchChange.bind(this);
  }

  componentWillMount() {
    this.resetComponent();
  }

  resetComponent = () =>
    this.setState({ isLoading: false, results: [], value: '' });

  handleResultSelect = (e, result) => {
    this.props.history.push('/achievements/' + result.id);
  };

  handleSearchChange = (e, value) => {
    const validLength = value.length > 2;

    this.setState({
      value: value,
      isLoading: validLength
    });

    if (!validLength) return;

    fetch(`http://localhost:8080/api/skiers?n=${value}`)
      //fetch(`/api/skiers?n=${value}`)
      .then(res => res.json())
      .then(data => {
        this.setState({
          isLoading: false,
          results: data.slice(0,14).map(s => ({              // Slice to limit results
            ...s,
            key: s.id,
            startClass: s.class,
            club: s.club,
            title: s.name,
            nationality: s.nationality
          }))
        });
      })
      .catch(e => console.warn(e));
  };

  render() {
    const { isLoading, value, results } = this.state;

    return (
      <div className="search-bar">
        <Search
          loading={isLoading}
          noResultsMessage={null}
          placeholder="Sök åkare"
          onResultSelect={this.handleResultSelect}
          onSearchChange={_.debounce(this.handleSearchChange, 10)}
          minCharacters={3}
          results={results}
          value={value}
          size={'medium'}
          resultRenderer={resultRenderer}
          {...this.props}
        />
      </div>
    );
  }
}

export default withRouter(SearchBar);
