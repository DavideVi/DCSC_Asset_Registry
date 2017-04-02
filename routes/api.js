var express = require('express');
var router = express.Router();

/*
 Models
*/

var model_asset = require('../models/asset');
var asset = new model_asset.Asset();

// Adds an asset
router.post('/asset/add', function(req, res, next) {

  asset.insert(req.db, req.body,
    function(asset_id) {
      return res.json({"status": "ok", "asset_id": asset_id });
    },
    function(code, message) {
      return res.status(code).json({"status": "error", "message": message});
    });

});

// Returns asset information
router.get('/asset/get/:asset_id', function(req, res, next) {

  asset.get(req.db, req.params.asset_id,
    function(asset) {
      return res.json(asset);
    },
    function(code, message) {
      return res.status(code).json({"status": "error", "message": message});
    });

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
