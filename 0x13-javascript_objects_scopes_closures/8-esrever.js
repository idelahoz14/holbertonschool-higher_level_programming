#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const list_return = [];

  for (let i = (list.length - 1); i >= 0; i--) {
    list_return.push(list[i]);
  }

  return (list_return);
};
