#!/usr/bin/node
// Function that executes x times a function.

exports.callMeMoby = function (x, callme) {
  for (let i = 0; i < x; i++) {
    callme();
  }
};
