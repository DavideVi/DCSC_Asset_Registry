var express = require('express');
var router = express.Router();

// Adds an asset
router.post('/asset/add', function(req, res, next) {

    //
    // if (req.body.username === undefined) {
    //   return res.status(400).json({"error": "'username' has not been set"});
    // }

    // var username = req.body.username;
    var collection = req.db.get('assets');

    collection.insert({

    }, function (err, doc) {
      if (err) {
        // return res.status(500).json({"status": "error", "message": "There was a problem creating a session"});
      }
      else {
        // return res.json({"status": "ok", "session_id": doc._id });
      }
    });

});

// Returns asset information
router.get('/asset/get', function(req, res, next) {

});

// Returns a list of assets
router.get('/asset/list', function(req, res, next) {

});

// Updates information regarding an asset
router.put('/asset/update', function(req, res, next) {

});

module.exports = router;
