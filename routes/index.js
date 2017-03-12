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

/* GET home page. */
router.get('/feedback', function(req, res, next) {
  res.render('feedback', { title: 'Express' });
});

module.exports = router;
