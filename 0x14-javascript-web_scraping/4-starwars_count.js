#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  let count = 0;
  const result = JSON.parse(body).results;
  for (const i in result) {
    const list = result[i].characters;
    for (const j in list) {
      if (list[j].match('/18/')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
