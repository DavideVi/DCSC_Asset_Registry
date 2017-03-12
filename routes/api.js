var express = require('express');
var router = express.Router();

function validate_req_body(to_validate){
  for (var key_name in to_validate)
  {
    if (to_validate[key_name] === undefined) {
      return key_name;
    }
  }
  return null;
}

// Adds an asset
router.post('/asset/add', function(req, res, next) {
    var asset_data = {"asset_name": req.body.asset_name,
                            "asset_purpose": req.body.asset_purpose,
                            "author_ids": req.body.author_ids,
                            "technologies": req.body.technologies,
                            "stability": req.body.stability,
                            "scm_link": req.body.scm_link,
                            "wiki_link": req.body.wiki_link
    };

    var key_name = validate_req_body(asset_data);
    if (key_name !== null) {
      return res.status(400).json({"error": key_name + " has not been set"});
    }

    var collection = req.db.get('assets');

    collection.insert(asset_data, function (err, doc) {

      if (err) {
        return res.status(500).json({"status": "error", "message": "There was a problem creating a session"});
      }
      else {
        return res.json({"status": "ok", "asset_id": doc._id });
      }
    });

});

// Returns asset information
router.get('/asset/get/:asset_id', function(req, res, next) {

  if (req.params.asset_id === undefined) {
    return res.status(400).json({"error": asset_id + " has not been set or is invalid"});
  }

  var mongo = require('mongodb');
  var asset_id = new mongo.ObjectID(req.params.asset_id);

  var collection = req.db.get('assets');
  collection.find({
    _id: asset_id
  }, function (err, doc) {

      if (err) {
        return res.status(500).json({"status": "error", "message": "Invalid ID"});
      }
      else {
        return res.json(doc);
      }
  })
});

// Returns a list of assets
router.get('/asset/list', function(req, res, next) {

  var collection = req.db.get('assets');
  collection.find({}, '-asset_purpose -author_ids -technologies -stability -scm_link -wiki_link', function (err, doc) {

      if (err) {
        return res.status(500).json({"status": "error", "message": err});
      }
      else {
        return res.json(doc);
      }
  })
});

// Updates information regarding an asset
router.put('/asset/update', function(req, res, next) {

});

module.exports = router;
