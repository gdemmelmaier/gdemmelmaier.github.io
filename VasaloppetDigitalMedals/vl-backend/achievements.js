const results = require('./vasaloppet18_new.json');

function secondsToHms(d) {
  d = Number(d);
  var h = Math.floor(d / 3600);
  var m = Math.floor((d % 3600) / 60);
  var s = Math.floor((d % 3600) % 60);

  var hDisplay = h > 0 ? h + (h == 1 ? ':' : ':') : '';
  var mDisplay = m > 0 ? m + (m == 1 ? ':' : ':') : '';
  var sDisplay = s > 0 ? s + (s == 1 ? ':' : '') : '';
  return hDisplay + mDisplay + sDisplay;
}

function HmsToSeconds(timeString) {
  var a = timeString.split(':'); // split it at the colons
  var seconds = +a[0] * 60 * 60 + +a[1] * 60 + +a[2];
  return seconds;
}

function parseResults(skier) {
  const achievements = [
    achievedVeteran(skier),
    achievedDownhill(skier),
    achievedFinisher(skier),
    achievedStrongFinish(skier),
    achievedTopOverall(skier),
    achievedTopClass(skier),
    achievedTopSex(skier),
    achievedTopClub(skier),
    achievedTopCity(skier),
    achievedTopCountry(skier),
    achievedSlowStartFastFinish(skier),
    achievedGoodPace(skier),
    //Future medals
    achievedTrippeln(skier),
    achievedYearRound(skier),
    achievedNattvasan(skier)
  ];

  // Sorting medals on ranking and denomination
  var multiplier = 1;
  for (i = 0; i < achievements.length; i++) {
    if (achievements[i].value == 'gold') {
      multiplier = 3;
    } else if (achievements[i].value == 'silver') {
      multiplier = 2;
    } else if (achievements[i].value == 'bronze') {
      multiplier = 1;
    }
    achievements[i].ranking *= multiplier;
  }
  achievements.sort(function(a, b) {
    return b.ranking - a.ranking;
  });

  return achievements.filter(achievement => Boolean(achievement.value));
}

const medals = {
  gold: 'gold',
  silver: 'silver',
  bronze: 'bronze'
};

/*
function getActivement(skier, title,  limits, callback) {

	const value = callback(skier);

	 if (value >= limits.gold) {
      medalValue = medals.gold
    }
    else if (value >= mvSilver) {
      medalValue = 'silver'
    }
    else if (value >= mvBronze) {
      medalValue = 'bronze'
    }	

	return {
		title: title,
		medalValue: medalValue
	}
}

getActivement(skier, "Veteran", {
	gold: 10,
	silver: 5,
	bronze: 3
},function(skier) {
	return skier.lopp.length
})
*/
function achievedSlowStartFastFinish(skier) {
  var medalValue = null;

  const mvGold = 0.94;
  const mvSilver = 0.96;
  const mvBronze = 1;

  //calulating means
  var evertsberg = 0;
  var evertsbergCounter = 0;
  for (i = 0; i < results.length; i++) {
    if (results[i].finish !== '' && results[i].evertsberg !== '') {
      evertsberg += HmsToSeconds(results[i].evertsberg);
      evertsbergCounter += 1;
    }
  }
  const meanEvertsberg = evertsberg / evertsbergCounter;
  const compareEvertsberg = HmsToSeconds(skier.evertsberg) / meanEvertsberg;

  var finish = 0;
  var finishCounter = 0;
  for (i = 0; i < results.length; i++) {
    if (results[i].finish !== '') {
      finish += HmsToSeconds(results[i].finish);
      finishCounter += 1;
    }
  }
  const meanFinish = finish / finishCounter;
  const compareFinish = HmsToSeconds(skier.finish) / meanFinish;
  const fasterQuota = compareFinish / compareEvertsberg;

  //deciding medal value

  if (fasterQuota <= mvGold) {
    medalValue = medals.gold;
  } else if (fasterQuota <= mvSilver) {
    medalValue = medals.silver;
  } else if (fasterQuota <= mvBronze) {
    medalValue = medals.bronze;
  }

  return {
    title: 'Snabbare och snabbare!',
    description:
      'Du avslutade starkare än de andra åkarna, i förhållande till hur du startade!',
    value: medalValue,
    type: 'faster',
    ranking: 3.1
  };
}

function achievedGoodPace(skier) {
  var medalValue = null;
  if (skier.finish == '') {
    return {
      title: '-',
      description: '-',
      value: medalValue,
      type: 'none',
      ranking: 0
    };
  }

  const mvGold = 0.04;
  const mvSilver = 0.08;
  const mvBronze = 0.13;

  var VL1Results = [0, 0, 0, 0, 0, 0, 0, 0, 0];
  var counter = 0;
  var AllVL1 = results.filter(function(entry) {
    if (
      entry.startgroup == 'VL1' &&
      entry.racestatus == 'FNS' &&
      entry.smågan !== '' &&
      entry.mångsbodarna !== '' &&
      entry.risberg !== '' &&
      entry.evertsberg !== '' &&
      entry.oxberg !== '' &&
      entry.hökberg !== '' &&
      entry.eldris !== ''
    ) {
      VL1Results[0] += HmsToSeconds(entry.smågan);
      VL1Results[1] +=
        HmsToSeconds(entry.mångsbodarna) - HmsToSeconds(entry.smågan);
      VL1Results[2] +=
        HmsToSeconds(entry.risberg) - HmsToSeconds(entry.mångsbodarna);
      VL1Results[3] +=
        HmsToSeconds(entry.evertsberg) - HmsToSeconds(entry.risberg);
      VL1Results[4] +=
        HmsToSeconds(entry.oxberg) - HmsToSeconds(entry.evertsberg);
      VL1Results[5] += HmsToSeconds(entry.hökberg) - HmsToSeconds(entry.oxberg);
      VL1Results[6] += HmsToSeconds(entry.eldris) - HmsToSeconds(entry.hökberg);
      VL1Results[7] += HmsToSeconds(entry.finish) - HmsToSeconds(entry.eldris);
      VL1Results[8] += HmsToSeconds(entry.finish);
      counter += 1;
    }
  });
  for (var i = 0; i < VL1Results.length; i++) {
    VL1Results[i] = VL1Results[i] / counter;
  }

  var skierFinishQouta = HmsToSeconds(skier.finish) / VL1Results[8];

  var skierQouta = [0, 0, 0, 0, 0, 0, 0];

  skierQouta[0] =
    (HmsToSeconds(skier.mångsbodarna) - HmsToSeconds(skier.smågan)) /
    (VL1Results[1] * skierFinishQouta);
  skierQouta[1] =
    (HmsToSeconds(skier.risberg) - HmsToSeconds(skier.mångsbodarna)) /
    (VL1Results[2] * skierFinishQouta);
  skierQouta[2] =
    (HmsToSeconds(skier.evertsberg) - HmsToSeconds(skier.risberg)) /
    (VL1Results[3] * skierFinishQouta);
  skierQouta[3] =
    (HmsToSeconds(skier.oxberg) - HmsToSeconds(skier.evertsberg)) /
    (VL1Results[4] * skierFinishQouta);
  skierQouta[4] =
    (HmsToSeconds(skier.hökberg) - HmsToSeconds(skier.oxberg)) /
    (VL1Results[5] * skierFinishQouta);
  skierQouta[5] =
    (HmsToSeconds(skier.eldris) - HmsToSeconds(skier.hökberg)) /
    (VL1Results[6] * skierFinishQouta);
  skierQouta[6] =
    (HmsToSeconds(skier.finish) - HmsToSeconds(skier.eldris)) /
    (VL1Results[7] * skierFinishQouta);

  for (i = 1; i < skierQouta.length; i++) {
    if (Math.abs(skierQouta[i] - 1) > mvBronze) {
      medalValue = null;
      break;
    } else if (Math.abs(skierQouta[i] - 1) > mvSilver) {
      medalValue = medals.bronze;
      break;
    } else if (Math.abs(skierQouta[i] - 1) > mvGold) {
      medalValue = medals.silver;
      break;
    } else {
      medalValue = medals.gold;
    }
  }
  //console.log(skierQouta);
  //console.log(skierFinishQouta);
  return {
    title: 'Väldisponerat lopp',
    description:
      'Du disponerade ditt lopp på samma sätt som elitåkarna. Snyggt!',
    value: medalValue,
    type: 'goodPace',
    ranking: 2.3
  };
}

function achievedTrippeln(skier) {
  var medalValue = null;


  if (skier.id == '9999991678885B0001C3A613') {
    medalValue = medals.gold;
  }
  return {
    title: 'Vasaloppet trippeln!',
    description:
      'Det är inte många som har gjort Vasaloppet med löpskor, skidor och cykel på samma år, men det har du! Not all heroes wear cape.',
    value: medalValue,
    type: 'trippeln',
    ranking: 3.4
  };
}

function achievedYearRound(skier) {
  var medalValue = null;

  if (skier.id == '9999991678885B0001C3A613') {
    medalValue = medals.gold;
  }
  return {
    title: 'Vasaloppet året runt!',
    description:
      'Det finns inget dåligt väder, bara dåliga kläder! Vasaloppet, oavsett årstid – bra jobbat!',
    value: medalValue,
    type: 'yearround',
    ranking: 3.2
  };
}

function achievedDownhill(skier) {
  // Standard intial medal values

  const mvGold = 3420;
  const mvSilver = 4320;
  const mvBronze = 6000;

  var medalValue = null;

  // All medals have one specific value that they measure
  const downhillTime =
    HmsToSeconds(skier.oxberg) - HmsToSeconds(skier.evertsberg);

  // Value decides which value the medal will have
  if (downhillTime <= mvGold) {
    medalValue = medals.gold;
  } else if (downhillTime <= mvSilver) {
    medalValue = medals.silver;
  } else if (downhillTime <= mvBronze) {
    medalValue = medals.bronze;
  }
  // All medals return the same thing
  return {
    title: 'Utförs- \n specialist',
    description:
      'Väl vallat! Du åkte Vasaloppets brantaste nedförssträcka Evertsberg-Oxberg på tiden ' +
      secondsToHms(downhillTime) +
      '! Det är bra, snyggt jobbat.',
    value: medalValue,
    type: 'downhillspecialist',
    ranking: 3
  };
}

function achievedStrongFinish(skier) {
  // Standard intial medal values

  const mvGold = 2500;
  const mvSilver = 3000;
  const mvBronze = 4500;

  var medalValue = null;

  // All medals have one specific value that they measure
  const eldrisToFinishTime =
    HmsToSeconds(skier.finish) - HmsToSeconds(skier.eldris);

  // Value decides which value the medal will have
  if (eldrisToFinishTime <= mvGold) {
    medalValue = medals.gold;
  } else if (eldrisToFinishTime <= mvSilver) {
    medalValue = medals.silver;
  } else if (eldrisToFinishTime <= mvBronze) {
    medalValue = medals.bronze;
  }
  // All medals return the same thing
  return {
    title: 'Upplopps- \n specialist',
    description:
      'Vilken stark avslutning! Du åkte Vasaloppets sista sträcka Eldris-Mora på tiden ' +
      secondsToHms(eldrisToFinishTime) +
      '! Snyggt jobbat.',
    value: medalValue,
    type: 'strongfinish',
    ranking: 3
  };
}

function achievedFinisher(skier) {
  var medalValue = null;

  if (skier.racestatus == 'FNS' || skier.antalVL > 1) {
    medalValue = medals.bronze;
  }
  return {
    title: 'Vasaloppet finisher',
    description:
      'Du har klarat av loppet Gustav Vasa startade 1520. Det är stort. I fäders spår för framtids segrar!',
    value: medalValue,
    type: 'finisher',
    ranking: 3
  };
}

// skier är personen vi räknar ut för och focusVariable är det attribut vi vill ha som krav
// när vi kollar vilken top % personen är.
// Ex. Anna är top X% för alla med samma "city" som henne
function topFraction(skier, focusVariable) {
  var skierPlace = '';
  var matchingDNF = 0;
  var matchingDNS = 0;

  var matchingSkiers = results
    .filter(function(entry) {
      if (entry.racestatus == 'FNS') {
        return skier[focusVariable] == entry[focusVariable];
      } else if (
        entry.racestatus == 'DNF' &&
        skier[focusVariable] == entry[focusVariable]
      ) {
        matchingDNF = matchingDNF + 1;
      } else if (
        entry.racestatus == 'DNS' &&
        skier[focusVariable] == entry[focusVariable]
      ) {
        matchingDNS = matchingDNS + 1;
      }
    })
    .sort((a, b) => a.overallplace - b.overallplace)
    .map(function(entry) {
      return {
        id: entry.id
      };
    });

  matchingSkiers.filter(function(entry, i) {
    if (entry.id == skier.id) {
      skierPlace = i;
    }
  });

  return {
    procentil:
      Math.floor(100 * skierPlace / (matchingSkiers.length + matchingDNF)) + 1,
    total: matchingSkiers.length + matchingDNF
  };
}

function achievedTopClub(skier) {
  const topPercent = topFraction(skier, 'club');
  const topProcentil = topPercent.procentil;

  const mvGold = 10;
  const mvSilver = 30;
  const mvBronze = 50;

  var medalValue = null;
  if (topProcentil <= mvGold) {
    medalValue = medals.gold;
  } else if (topProcentil <= mvSilver) {
    medalValue = medals.silver;
  } else if (topProcentil <= mvBronze) {
    medalValue = medals.bronze;
  }
  if (skier.racestatus !== 'FNS') {
    medalValue = medals.null;
  }

  return {
    title: 'Klubbmästare',
    description:
      'Du gick i mål bland top ' +
      topProcentil +
      '% ifrån din klubb, ' +
      skier.club +
      '.',
    value: medalValue,
    type: 'topClub',
    ranking: 4
  };
}

function achievedTopCity(skier) {
  if (skier.city.length < 2) {
    return {
      value: null
    };
  }
  const topPercent = topFraction(skier, 'city');
  const topProcentil = topPercent.procentil;

  const mvGold = 10;
  const mvSilver = 30;
  const mvBronze = 50;

  var medalValue = null;
  if (topProcentil <= mvGold) {
    medalValue = medals.gold;
  } else if (topProcentil <= mvSilver) {
    medalValue = medals.silver;
  } else if (topProcentil <= mvBronze) {
    medalValue = medals.bronze;
  }
  if (skier.racestatus !== 'FNS') {
    medalValue = medals.null;
  }

  return {
    title: 'Ortens favorit',
    description:
      'Du gick i mål bland top ' +
      topProcentil +
      '% ifrån din stad,  ' +
      skier.city +
      '.',
    value: medalValue,
    type: 'topCity',
    ranking: 2.9
  };
}

function achievedTopCountry(skier) {
  const topPercent = topFraction(skier, 'country');
  const topProcentil = topPercent.procentil;

  const mvGold = 10;
  const mvSilver = 30;
  const mvBronze = 50;

  var medalValue = null;
  if (topProcentil <= mvGold) {
    medalValue = medals.gold;
  } else if (topProcentil <= mvSilver) {
    medalValue = medals.silver;
  } else if (topProcentil <= mvBronze) {
    medalValue = medals.bronze;
  }
  if (skier.racestatus !== 'FNS') {
    medalValue = medals.null;
  }

  return {
    title: 'Främst bland landsmän',
    description:
      'Du gick i mål bland top ' +
      topProcentil +
      '% ifrån ' +
      skier.country +
      '.',
    value: medalValue,
    type: 'topCountry',
    ranking: 3.8
  };
}

function achievedTopSex(skier) {
  var medalValue = null;
  const mvGold = 10;
  const mvSilver = 30;
  const mvBronze = 50;

  const totalSex = results.filter(function(entry) {
    if (entry.racestatus !== 'DNS') {
      return entry.class.charAt(0) == skier.class.charAt(0);
    }
  });
  const topProcentil = Math.floor(100 * skier.sexplace / totalSex.length) + 1;

  if (topProcentil <= mvGold) {
    medalValue = medals.gold;
  } else if (topProcentil <= mvSilver) {
    medalValue = medals.silver;
  } else if (topProcentil <= mvBronze) {
    medalValue = medals.bronze;
  }
  if (skier.racestatus !== 'FNS') {
    medalValue = medals.null;
  }

  if (skier.class.charAt(0) == 'H') {
    return {
      title: 'Bland herrar!',
      description: 'Du är topp ' + topProcentil + '% av tävlande män! Snyggt.',
      value: medalValue,
      type: 'topSex',
      ranking: 2.1
    };
  }

  if (skier.class.charAt(0) == 'D') {
    return {
      title: 'Bland damer!',
      description:
        'Du är topp ' + topProcentil + '% av tävlande kvinnor! Snyggt.',
      value: medalValue,
      type: 'topSex',
      ranking: 2.1
    };
  }
}

function achievedTopOverall(skier) {
  const totalSkiers = Object.keys(results).length;
  const topPercent = Math.floor(100 * skier.overallplace / totalSkiers) + 1;

  var medalValue = null;
  const mvGold = 10;
  const mvSilver = 30;
  const mvBronze = 50;

  if (topPercent <= mvGold) {
    medalValue = medals.gold;
  } else if (topPercent <= mvSilver) {
    medalValue = medals.silver;
  } else if (topPercent <= mvBronze) {
    medalValue = medals.bronze;
  }

  if (skier.racestatus !== 'FNS') {
    medalValue = medals.null;
  }
  return {
    title: 'Better than the rest',
    description: 'Du gick i mål bland top ' + topPercent + '%.',
    value: medalValue,
    type: 'topOverall',
    ranking: 4.3
  };
}
function achievedTopClass(skier) {
  const topPercent = topFraction(skier, 'class');
  const topProcentil = topPercent.procentil;

  const mvGold = 10;
  const mvSilver = 30;
  const mvBronze = 50;

  var medalValue = null;
  if (topProcentil <= mvGold) {
    medalValue = medals.gold;
  } else if (topProcentil <= mvSilver) {
    medalValue = medals.silver;
  } else if (topProcentil <= mvBronze) {
    medalValue = medals.bronze;
  }

  if (skier.racestatus !== 'FNS') {
    medalValue = medals.null;
  }

  return {
    title: 'Bäst i klassen',
    description:
      'Du gick i mål bland top ' +
      topProcentil +
      '% i klassen ' +
      skier.class +
      '.',
    value: medalValue,
    type: 'topClass',
    ranking: 2.2
  };
}

function achievedNattvasan(skier) {
  var medalValue = null;
  if (skier.id == '9999991678885900000C333C') {
    medalValue = medals.gold;
  }
  return {
    title: 'Nattugglan',
    description: 'Du har gått i mål i det mörkaste Vasaloppet - Nattvasan!',
    value: medalValue,
    type: 'nattvasan',
    ranking: 3
  };
}

function achievedVeteran(skier) {
  const raceCount = skier.antalVL;

  const mvGold = 10;
  const mvSilver = 5;
  const mvBronze = 3;

  var medalValue = null;

  if (raceCount >= mvGold) {
    medalValue = medals.gold;
  } else if (raceCount >= mvSilver) {
    medalValue = medals.silver;
  } else if (raceCount >= mvBronze) {
    medalValue = medals.bronze;
  }

  return {
    title: 'Veteran',
    description:
      'Du har klarat av totalt ' +
      raceCount +
      ' Vasalopp, det förtjänar sannerligen en medalj.',
    value: medalValue,
    type: 'veteran',
    ranking: 4.5
  };
}

module.exports = parseResults;
