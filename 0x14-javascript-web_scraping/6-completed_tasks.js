#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const Dict = {};
  const x = JSON.parse(body);
  for (const i in x) {
    if (x[i].completed === true) {
      if (Dict[x[i].userId] === undefined) {
        Dict[x[i].userId] = 1;
      } else {
        Dict[x[i].userId]++;
      }
    }
  }
  console.log(Dict);
});
