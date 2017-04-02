'use strict';

function Validator() {
    this.errors = [];
    this.decoratorsList = [];
}

Validator.decorators = {};

Validator.prototype.decorate = function(name) {  
    this.decoratorsList.push(name);
};

Validator.decorators.validate_text(text) {

}

Validator.decorators.validate_url(url) {

}

Validator.decorators.validate_list(list) {

}

module.exports.Validator = Validator;
