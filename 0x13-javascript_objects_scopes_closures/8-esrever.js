#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const x = [];

  for (let i = (list.length - 1); i >= 0; i--) {
    x.push(list[i]);
  }

  return (x);
};