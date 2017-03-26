var express = require('express');
var router = express.Router();

function validate_req_body(to_validate){
  for (var key_name in to_validate)
  {
    if (to_validate[key_name] === undefined) {
      console.log(key_name);
      return key_name;
    }
  }
  console.log("ok:" + key_name);
  return null;
}

function validate_string(string_to_validate){
  for (var string_value in string_to_validate)
  {
    if ( typeof string_to_validate[string_value] !== 'string') {
      console.log(string_value);
      return string_value;
    }
  }
  console.log("ok:" + string_value);
  return null;
}

// Adds an asset
router.post('/asset/add', function(req, res, next) {
    var asset_name = req.body.asset_name;
    var asset_purpose = req.body.asset_purpose;
    var author_ids = req.body.author_ids;
    var technologies = req.body.technologies;
    var stability = req.body.stability;
    var scm_link =req.body.scm_link;
    var wiki_link = req.body.wiki_link;

    // var string_data = {asset_name,
    //                    asset_purpose,
    //                    scm_link,
    //                    wiki_link
    // };

    if (technologies.constructor !== Array){
      technologies = [];
    }
    if (author_ids.constructor !== Array){
      author_ids = [];
    }
    if (wiki_link === undefined) {
      wiki_link = "";
    }
    var asset_data = {"asset_name": asset_name,
                      "asset_purpose": asset_purpose,
                      "author_ids": author_ids,
                      "technologies": technologies,
                      "stability": stability,
                      "scm_link": scm_link,
                      "wiki_link": wiki_link
    };

    var string_name = validate_string(string_data);
    if (string_name !== null) {
      return res.status(400).json({"error": string_name + " is not a string type."});
    }
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
        return res.json(doc[0]);
      }
  })
});

// Returns a list of assets
router.get('/list', function(req, res, next) {

  var collection = req.db.get('assets');
  collection.find({}, '-asset_purpose -author_ids -technologies -stability -scm_link -wiki_link', function (err, doc) {

      if (err) {
        return res.status(500).json({"status": "error", "message": err});
      }
      else {
        return res.json(doc);
      }
  }).limit(10)
});

// Updates information regarding an asset
router.put('/asset/update', function(req, res, next) {

});

module.exports = router;
