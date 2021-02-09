#!/usr/bin/node
// script that display the status code of a GET request.

const request = require('request');
request(process.argv[2], function (error, response, body) {
  console.log('code:', response && response.statusCode);
});
