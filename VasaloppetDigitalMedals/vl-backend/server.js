const Fuse = require('fuse.js');

// BASE SERVER SETUP
// =============================================================================

var parseAchievements = require('./achievements.js');

var express = require('express'); // call express
var app = express(); // define our app using express
var bodyParser = require('body-parser');

/*var mongoose   = require('mongoose');
mongoose.connect('mongodb://node:node@novus.modulusmongo.net:27017/Iganiq8o'); */ app.use(
  bodyParser.urlencoded({ extended: true })
);
app.use(bodyParser.json());

// get all skier data
const results = require('./vasaloppet18_new.json');

var port = process.env.PORT || 8080; // set our port

// ROUTES FOR OUR API
// =============================================================================
var router = express.Router(); // get an instance of the express Router

// This is called middleware. It can be used to authenticate that user access to API
router.use(function(req, res, next) {
  // do logging
  console.log('Middleware is happening');
  next(); // make sure we go to the next routes and don't stop here
});

// ROUTE FOR TESTING THAT EVERYTHING IS WORKING
router.get('/', function(req, res) {
  res.json({
    message: 'Welcome to our API!'
  });
});

// ENDPOINT /skiers RETURNS ALL SKIERS OR SEARCH RESULT AS QUERY N
// E.G. /skiers?n=Kelly will return all skiers whos name include "Kelly"
// =============================================================================

router
  .route('/skiers')

  .get(function(req, res) {
    try {
      // SEARCH QUERY NAME N=
      if (req.query.n) {
        // Filters through results for names matching query
        // and then loops through that array in order to make a new partial JSON response with name + id
        var options = {
          keys: ['fullName', 'firstname', 'lastname'],
          caseSensitive: true,
          threshold: 0.2,
          minMatchCharLength: 3
        };
        var fuse = new Fuse(results, options);

        const skierNameIncludes = fuse.search(req.query.n).map(skier => ({
          id: skier.id,
          name: skier.firstname + ' ' + skier.lastname,
          club: skier.club,
          nationality: skier.country,
          class: skier.class
        }));
        // Returns the skier variable as a response
        res.json(skierNameIncludes);
      }

      // QUERY EXACT ID=
      else if (req.query.id) {
        const chosenSkier = results.find(skier => skier.id == req.query.id);
        if (!chosenSkier) {
          res.status(404).send({
            message: 'Kan inte hitta åkare'
          });
        } else {
          chosenSkier.achievements = parseAchievements(chosenSkier);
          res.json(chosenSkier);
        }
      }

      // ENDPOINT IF NO QUERYS ARE SPECIFIED – RETURNS ALL SKIERS
      else {
        res.json(results);
      }
    } catch (e) {
      res.status(500).json({
        message: e.message
      });
    }
  })

  .post(function(req, res) {
    var skier = new Skier(); // create a new instance of the skier model
    skier.name = req.body.name; // set the skiers name (comes from the request)

    // save the skier and check for errors
    skier.save(function(err) {
      if (err) res.send(err);

      res.json({ message: 'Skier created!' });
    });
  });

// ROUTES THAT END WITH /ID
// =============================================================================
/*
router.route('/skiers/:skier_id')

    .get(function(req, res) {
        const skier = results.find(skier => skier._id == req.params.skier_id);
        if(!skier) {
            res.send("ERROR 420: Missing skier!")
        }
        else {
            res.json(skier.name)
        }
    });

// ROUTES THAT END WITH /ID
// =============================================================================

router.route('/skiers?n=urlname')

    .get(function(req, res) {
        const skier = results.find(skier => skier.name == req.query.urlname);
        if(!skier) {
            res.send("ERROR 420: Missing skier with name " + req.query.urlname)
        }
        else {
            res.json(skier.name + skier._id)
        }
    });
*/

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Magic happens on port ' + port);
