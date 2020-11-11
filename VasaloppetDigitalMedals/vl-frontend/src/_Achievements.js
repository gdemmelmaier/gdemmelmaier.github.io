import React, { Component } from 'react';
import results from './skiers';
import MedalComponent from './MedalComponent';
import { NavLink } from 'react';

// Content page 3
class Achievements extends Component {
  constructor(props) {
    super(props);
    this.state = {
      result: undefined
    };
  }

  componentWillMount() {
    const tempResult = results.find(result => {
      return result.id == this.props.match.params.id;
    });
    this.setState({
      result: tempResult
    });
  }

  secondsToHms(d) {
    d = Number(d);
    var h = Math.floor(d / 3600);
    var m = Math.floor((d % 3600) / 60);
    var s = Math.floor((d % 3600) % 60);

    var hDisplay = h > 0 ? h + (h == 1 ? ':' : ':') : '';
    var mDisplay = m > 0 ? m + (m == 1 ? ':' : ':') : '';
    var sDisplay = s > 0 ? s + (s == 1 ? ':' : '') : '';
    return hDisplay + mDisplay + sDisplay;
  }

  getRaceTimes(idYear) {
    for (var i = 0; i < this.state.result.lopp.length; i++) {
      if (
        this.state.result.lopp[i].id[0] == idYear[0] &&
        this.state.result.lopp[i].id[1] == idYear[1]
      ) {
        const getTimes = this.state.result.lopp[i].data;
        return getTimes;
      }
    }
  }

  getRaceCount() {
    return this.state.result.lopp.length;
  }

  achievedVeteran() {
    const medalName = 'Veteran';
    const medalIcon = '';
    var medalResultTime = '';
    var deserveMedalGold = false;
    var deserveMedalSilver = false;
    var deserveMedalBronze = false;

    const medalValueGold = 10;
    const medalValueSilver = 5;
    const medalValueBronze = 3;
    var raceDataList = [];

    if (this.getRaceCount() >= medalValueGold) {
      deserveMedalGold = true;
      deserveMedalSilver = true;
      deserveMedalBronze = true;
    } else if (this.getRaceCount() >= medalValueSilver) {
      deserveMedalSilver = true;
      deserveMedalBronze = true;
    } else if (this.getRaceCount() >= medalValueBronze) {
      deserveMedalBronze = true;
    }
    medalResultTime =
      'You have finished ' +
      this.getRaceCount().toString() +
      ' Vasalopp in total!';
    return [
      medalName,
      medalResultTime,
      deserveMedalGold,
      deserveMedalSilver,
      deserveMedalBronze
    ];
  }

  // Här vill vi loopa och jämföra lopp med samma id. Checka ifall det finns ett "streak" eller konstant ökning.
  achievedUAC() {
    const medalName = 'Up-and-coming';
    const medalIcon = '';
    var storedMedalResultValue = [''];
    var medalResultValue = [];
    var deserveMedalGold = false;
    var deserveMedalSilver = false;
    var deserveMedalBronze = false;

    const raceID = 1;
    const medalValueGold = 4;
    const medalValueSilver = 3;
    const medalValueBronze = 2;
    var raceDataList = [];

    for (var i = 0; i < this.state.result.lopp.length; i++) {
      if (this.state.result.lopp[i].id[0] == raceID) {
        raceDataList.push([
          this.state.result.lopp[i].id[1],
          this.getRaceTimes(this.state.result.lopp[i].id)[2]
        ]);
      }
    }
    raceDataList.sort();
    for (var i = 0; i < raceDataList.length - 1; i++) {
      if (raceDataList[i][1] > raceDataList[i + 1][1]) {
        medalResultValue.push(raceDataList[i][0]);
        medalResultValue.push(raceDataList[i + 1][0]);
      } else {
        if (medalResultValue.length > storedMedalResultValue.length) {
          storedMedalResultValue = medalResultValue;
          medalResultValue = [];
        }
      }
    }
    if (medalResultValue.length > storedMedalResultValue.length) {
      storedMedalResultValue = medalResultValue;
    }

    storedMedalResultValue = [...new Set(storedMedalResultValue)];
    storedMedalResultValue.sort();
    if (storedMedalResultValue.length >= medalValueGold) {
      deserveMedalGold = true;
      deserveMedalSilver = true;
      deserveMedalBronze = true;
    } else if (storedMedalResultValue.length >= medalValueSilver) {
      deserveMedalSilver = true;
      deserveMedalBronze = true;
    } else if (storedMedalResultValue.length >= medalValueBronze) {
      deserveMedalBronze = true;
    }
    if (storedMedalResultValue.length > 1) {
      storedMedalResultValue =
        storedMedalResultValue[0].toString() +
        ' – ' +
        Math.max(...storedMedalResultValue).toString();
    }
    return [
      medalName,
      storedMedalResultValue,
      deserveMedalGold,
      deserveMedalSilver,
      deserveMedalBronze
    ];
  }

  // Deserved for skiers who have done race X and completed the
  // downhill-only-distance (between Y and Z) under the time T.
  achievedDownhill() {
    //Big six
    const medalName = 'Downhill Specialist';
    const medalIcon = '';
    var medalResultTime = [];
    var deserveMedalGold = false;
    var deserveMedalSilver = false;
    var deserveMedalBronze = false;

    // Medal specific constants and variables
    const raceID = 1;
    const startCheckpoint = 3;
    const endCheckpoint = 4;
    const medalValueGold = 8000;
    const medalValueSilver = 15800;
    const medalValueBronze = 250000;
    var raceDataList = [];

    // Loops through the races with ID=raceID, saves the time-data for these in an array
    for (var i = 0; i < this.state.result.lopp.length; i++) {
      if (this.state.result.lopp[i].id[0] == raceID) {
        raceDataList.push(this.getRaceTimes(this.state.result.lopp[i].id));
      }
    }

    // Checks so the array for the specific race isn't empty
    if (!raceDataList == []) {
      // Checks if each race and its time between checkpoints deserves a medal.
      for (var i = 0; i < raceDataList.length; i++) {
        if (
          raceDataList[i][endCheckpoint] - raceDataList[i][startCheckpoint] <
          medalValueGold
        ) {
          deserveMedalGold = true;
          deserveMedalSilver = true;
          deserveMedalBronze = true;
          medalResultTime.push(
            raceDataList[i][endCheckpoint] - raceDataList[i][startCheckpoint]
          );
        } else if (
          raceDataList[i][endCheckpoint] - raceDataList[i][startCheckpoint] <
          medalValueSilver
        ) {
          deserveMedalSilver = true;
          deserveMedalBronze = true;
          medalResultTime.push(
            raceDataList[i][endCheckpoint] - raceDataList[i][startCheckpoint]
          );
        } else if (
          raceDataList[i][endCheckpoint] - raceDataList[i][startCheckpoint] <
          medalValueBronze
        ) {
          deserveMedalBronze = true;
          medalResultTime.push(
            raceDataList[i][endCheckpoint] - raceDataList[i][startCheckpoint]
          );
        }
      }
      medalResultTime = this.secondsToHms(Math.min(...medalResultTime));
    }
    return [
      medalName,
      medalResultTime + ' between Evertsberg and Oxberg',
      deserveMedalGold,
      deserveMedalSilver,
      deserveMedalBronze
    ];
  }

  achievedVasaloppetFinisher() {
    const medalName = 'Vasaloppet Finisher';
    const medalIcon = '';
    var medalResultYears = [];
    var deserveMedalGold = false;
    var deserveMedalSilver = false;
    var deserveMedalBronze = false;
    const raceID = 1;

    for (var i = 0; i < this.state.result.lopp.length; i++) {
      if (this.state.result.lopp[i].id[0] == raceID) {
        deserveMedalBronze = true;
        medalResultYears.push(this.state.result.lopp[i].id[1]);
      }
    }
    medalResultYears.sort();
    medalResultYears = medalResultYears.join(', ');
    console.log([
      medalName,
      medalResultYears,
      deserveMedalGold,
      deserveMedalSilver,
      deserveMedalBronze
    ]);
    return [
      medalName,
      medalResultYears,
      deserveMedalGold,
      deserveMedalSilver,
      deserveMedalBronze
    ];
  }

  checkAchievements() {
    var achievements = [
      this.achievedDownhill(),
      this.achievedVeteran(),
      this.achievedUAC(),
      this.achievedVasaloppetFinisher()
    ];
    for (var i = 0; i < achievements.length; i++) {
      if (achievements[i][4] == false) {
        achievements.splice(i, 1);
        i--;
        console.log(achievements);
      }
    }
    return achievements;
  }

  render() {
    if (!this.state.result) {
      return (
        <div>
          <h1 className="compNotFound">
            Competitor not found. Please press the Vasaloppet logo to go back to
            home page.
          </h1>
        </div>
      );
    }

    return (
      <div>
        <h1 class="name-title">{this.state.result.name}</h1>
        <h2 class="welldone-title">
          Well done! Here are your best achievements.
        </h2>

        <MedalComponent achievements={this.checkAchievements()} />
      </div>
    );
  }
}

export default Achievements;
