'use strict';

// Constructor
function Asset() {}

// Add an asset
Asset.prototype.insert = function(db, payload, success, error) {

  // Processing payload
  var new_doc = {"asset_name": payload["asset_name"],
                    "asset_purpose": payload["asset_purpose"],
                    "author_ids": payload["author_ids"],
                    "technologies": payload["technologies"],
                    "stability": payload["stability"],
                    "scm_link": payload["scm_link"],
                    "wiki_link": payload["wiki_link"]
  };

  // Validating form
  var errors = this.validate(new_doc);
  if (errors.length > 0) {
    error(400, errors);
    return;
  }

  // Inserting form data into DB
  var collection = db.get('assets');

  console.log(new_doc);
  collection.insert(new_doc, function (err, doc) {

    if (err) {
      error(500,"There was a problem creating a session");
      return;
    }
    else {
      success(doc._id);
    }
  });
}

Asset.prototype.get = function(db, asset_id, success, error) {

  // Validation
  if (asset_id === undefined) {
    error(400, "asset_id has not been set");
    return;
  }

  // DB Retrieval
  var mongo = require('mongodb');
  var asset_id = new mongo.ObjectID(asset_id);

  var collection = db.get('assets');
  collection.find({
    _id: asset_id
  }, function (err, doc) {

      if (err) {
        error(500,"Invalid ID has been provided");
      }
      else {
        success(doc[0]);
      }
  })
}

// Helper method, validates for for insert and update
Asset.prototype.validate = function(payload) {

  var validator = require('./validator');
  var validator = new validator.Validator();

  // Text
  validator.decorate(['mandatory','is_string','text_format']);
  validator.validate(payload["asset_purpose"], "Asset purpose");
  validator.decorate('title');
  validator.validate(payload["asset_name"], "Asset name");

  // Lists
  validator.undecorate_all();
  validator.decorate('is_list');
  validator.validate(payload["technologies"], "Technologies");
  validator.decorate('mandatory');
  validator.validate(payload["author_ids"], "Author IDs");

  // URLs
  validator.undecorate_all();
  validator.decorate('is_url');
  validator.validate(payload["scm_link"], "SCM Link");
  validator.decorate('mandatory');
  validator.validate(payload["wiki_link"], "Wiki Link");

  return validator.errors;
}

module.exports.Asset = Asset;
