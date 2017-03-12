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
router.get('/asset/get', function(req, res, next) {
  return res.json({"status": "ok"});
});

// Returns a list of assets
router.get('/asset/list', function(req, res, next) {

});

// Updates information regarding an asset
router.put('/asset/update', function(req, res, next) {

});

module.exports = router;
