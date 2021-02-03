#!/usr/bin/node
// Function that increments and calls a function.

exports.addMeMaybe = function (number, addme) {
  number += 1;
  addme(number);
};
