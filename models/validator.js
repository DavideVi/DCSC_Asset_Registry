'use strict';

/*
  Decorator pattern
*/
function Validator () {
    this.errors = [];
    this.decoratorsList = [];
}

Validator.prototype.decorate = function(name) {
    if (name.constructor === Array) {
      for (var index in name) {
        this.decoratorsList.push({ name: name[index] });
      }
    }
    else {
      this.decoratorsList.push({ name: name });
    }
};

Validator.prototype.undecorate = function(name) {
  this.decoratorsList.pop({ name: name });
};

Validator.prototype.undecorate_all = function() {
    this.decoratorsList = [];
};

Validator.decorators = {};

/*
  Actual decorations / validations
*/
Validator.decorators.mandatory = {
    validate: function(field, name) {
      if (field === undefined) {
        this.errors.push(field + ' cannot be underfined');
      }
    }
};

Validator.decorators.is_string = {
    validate: function(field, name) {
      if (field instanceof String) {
        this.errors.push(name + ' must be a string');
      }
    }
};

Validator.decorators.text_format = {
    validate: function(field, name) {
      if (field.replace(" ","") === "") {
        this.errors.push(name + ' cannot be empty or all spaces');
      }
      if (/^\d+$/.test(field)) {
        this.errors.push(name + ' cannot be all numbers');
      }
      if(/^[a-zA-Z0-9- ]*$/.test(field) == false) {
        this.errors.push(name + ' must contains some letters');
      }
    }
};

Validator.decorators.title = {
    validate: function(field, name) {
        this.errors.push(name + ' not a title');
    }
};

Validator.decorators.is_list = {
    validate: function(field, name) {
        this.errors.push(name + ' not a list');
    }
};

Validator.decorators.is_url = {
    validate: function(field, name) {
        this.errors.push(name + ' not a URL');
    }
};

/*
  Method that calls all the decorators to perform validation
*/
Validator.prototype.validate = function(field, field_name) {
    var i,
        max,
        temp,
        name,
        field_name;

    this.field = field;

    max = this.decoratorsList.length;
    for (i = 0; i < max; i++) {
        temp = this.decoratorsList[i];
        name = temp.name;
        Validator.decorators[name].validate.call(this, field, field_name);
    };
};

module.exports.Validator = Validator;
