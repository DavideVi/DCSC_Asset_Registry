var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

/* GET home page. */
router.get('/add', function(req, res, next) {
  res.render('add', { title: 'Express' });
});

router.get('/asset/:id', function(req, res, next) {
  res.render('asset', { asset_id: req.params.id });
});

router.get('/browse', function(req, res, next) {
  res.render('list', { asset_id: req.params.id });
});

/* GET home page. */
router.get('/feedback', function(req, res, next) {
  res.render('feedback', { title: 'Express' });
});

module.exports = router;
