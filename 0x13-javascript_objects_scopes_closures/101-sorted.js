#!/usr/bin/node
// Script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const dict = require('./101-data.js').dict;
const x = {};

for (const index in dict) {
  if (x[dict[index]] === undefined) {
    x[dict[index]] = [];
  }
  x[dict[index]].push(index);
}
console.log(x);
