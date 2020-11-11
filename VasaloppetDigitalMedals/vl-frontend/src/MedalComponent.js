import React from 'react';
import { Icon, Popup, Button } from 'semantic-ui-react';

import GoldIcon from './img/gold_fresh.svg';
import SilverIcon from './img/silver_fresh.svg';
import BronzeIcon from './img/unique/flag_bronze.svg';

import starsBronze from './img/unique/stars_bronze.svg';
import starsSilver from './img/unique/stars_silver.svg';
import starsGold from './img/unique/stars_gold.svg';
import crownBronze from './img/unique/crown_bronze.svg';
import crownSilver from './img/unique/crown_silver.svg';
import crownGold from './img/unique/crown_gold.svg';
import flagBronze from './img/unique/flag_bronze.svg';
import flagSilver from './img/unique/flag_silver.svg';
import flagGold from './img/unique/flag_gold.svg';
import muscleBronze from './img/unique/muscle_bronze.svg';
import muscleSilver from './img/unique/muscle_silver.svg';
import muscleGold from './img/unique/muscle_gold.svg';
import owlBronze from './img/unique/owl_bronze.svg';
import owlSilver from './img/unique/owl_silver.svg';
import owlGold from './img/unique/owl_gold.svg';
import handBronze from './img/unique/hand_bronze.svg';
import handSilver from './img/unique/hand_silver.svg';
import handGold from './img/unique/hand_gold.svg';
import arrowBronze from './img/unique/arrow_bronze.svg';
import arrowSilver from './img/unique/arrow_silver.svg';
import arrowGold from './img/unique/arrow_gold.svg';
import sexBronze from './img/unique/sex_bronze.svg';
import sexSilver from './img/unique/sex_silver.svg';
import sexGold from './img/unique/sex_gold.svg';
import vetBronze from './img/unique/vet_bronze.svg';
import vetSilver from './img/unique/vet_silver.svg';
import vetGold from './img/unique/vet_gold.svg';
import mountainBronze from './img/unique/mountain_bronze.svg';
import mountainSilver from './img/unique/mountain_silver.svg';
import mountainGold from './img/unique/mountain_gold.svg';
import houseBronze from './img/unique/house_bronze.svg';
import houseSilver from './img/unique/house_silver.svg';
import houseGold from './img/unique/house_gold.svg';

class MedalComponent extends React.Component {
  render() {
    let icon;

    if (this.props.achievements.length === 0)
      return <h2>Du har inga medaljer</h2>;
    var medalList = this.props.achievements.map(function(medalData, index) {
      const { type, value } = medalData;
      if (type == 'veteran') {
        if (value === 'gold') icon = vetGold;
        else if (value === 'silver') icon = vetSilver;
        else if (value === 'bronze') icon = vetBronze;
      } else if (type === 'downhillspecialist') {
        if (value === 'gold') icon = mountainGold;
        else if (value === 'silver') icon = mountainSilver;
        else if (value === 'bronze') icon = mountainBronze;
      } else if (type === 'faster') {
        if (value === 'gold') icon = arrowGold;
        else if (value === 'silver') icon = arrowSilver;
        else if (value === 'bronze') icon = arrowBronze;
      } else if (type === 'goodpace') {
        if (value === 'gold') icon = crownGold;
        else if (value === 'silver') icon = crownSilver;
        else if (value === 'bronze') icon = crownBronze;
      } else if (type === 'trippeln') {
        if (value === 'gold') icon = starsGold;
        else if (value === 'silver') icon = starsSilver;
        else if (value === 'bronze') icon = starsBronze;
      } else if (type === 'yearround') {
        if (value === 'gold') icon = handGold;
        else if (value === 'silver') icon = handSilver;
        else if (value === 'bronze') icon = handBronze;
      } else if (type === 'strongfinish') {
        if (value === 'gold') icon = flagGold;
        else if (value === 'silver') icon = flagSilver;
        else if (value === 'bronze') icon = flagBronze;
      } else if (type === 'finisher') {
        if (value === 'gold') icon = vetGold;
        else if (value === 'silver') icon = vetSilver;
        else if (value === 'bronze') icon = vetBronze;
      } else if (type === 'topClub') {
        if (value === 'gold') icon = houseGold;
        else if (value === 'silver') icon = houseSilver;
        else if (value === 'bronze') icon = houseBronze;
      } else if (type === 'topCountry') {
        if (value === 'gold') icon = vetGold;
        else if (value === 'silver') icon = vetSilver;
        else if (value === 'bronze') icon = vetBronze;
      } else if (type === 'topSex') {
        if (value === 'gold') icon = sexGold;
        else if (value === 'silver') icon = sexSilver;
        else if (value === 'bronze') icon = sexBronze;
      } else if (type === 'topOverall') {
        if (value === 'gold') icon = vetGold;
        else if (value === 'silver') icon = vetSilver;
        else if (value === 'bronze') icon = vetBronze;
      } else if (type === 'topClass') {
        if (value === 'gold') icon = vetGold;
        else if (value === 'silver') icon = vetSilver;
        else if (value === 'bronze') icon = vetBronze;
      } else if (type === 'nattvasan') {
        if (value === 'gold') icon = owlGold;
        else if (value === 'silver') icon = owlSilver;
        else if (value === 'bronze') icon = owlBronze;
      } else if (type === 'topCity') {
        if (value === 'gold') icon = owlGold;
        else if (value === 'silver') icon = owlSilver;
        else if (value === 'bronze') icon = owlBronze;
      } else if (type === 'goodPace') {
        if (value === 'gold') icon = crownGold;
        else if (value === 'silver') icon = crownSilver;
        else if (value === 'bronze') icon = crownBronze;
      }

      return (
        <li key="index">
          <div
            style={{ animationDelay: `${(index + 1) * 200}ms` }}
            className="ind-medal"
          >
            <div className="medal-inner">
              <div className="medal-image">
                <img alt="medal-should-show-here" src={icon} />
                <div className="share-info">
                  <Button animated="fade" color="facebook" size="mini">
                    <Button.Content visible>
                      <Icon name="facebook" /> Share!
                    </Button.Content>
                    <Button.Content hidden>
                      <Icon name="send" />
                    </Button.Content>
                  </Button>
                </div>
                <h3 className="medal-title">
                  <span>{medalData.title} </span>
                  {false && (
                    <Popup
                      key={index}
                      trigger={<Icon name="info circle" />}
                      content={medalData.description}
                      position="bottom center"
                      on="hover"
                      inverted
                    />
                  )}
                </h3>
              </div>

              <p className="medal-undertitle">{medalData.description}</p>
            </div>
          </div>
        </li>
      );
    });

    return (
      <div className="medal-box">
        <ul>{medalList}</ul>
      </div>
    );
  }
}

export default MedalComponent;
