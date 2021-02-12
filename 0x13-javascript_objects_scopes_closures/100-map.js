#!/usr/bin/node
// Script that imports an array and computes a new array

const list = require('./100-data.js').list;
const list_return = list.map((x, i) => x * i);

console.log(list);
console.log(list_return);
