#!/usr/bin/node
// script that display the status code of a GET request.

const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  console.log(JSON.parse(body).title);
});
