#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const fs = require('fs');
const request = require('request');
const url = process.argv[2];

request.get (url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  fs.writeFile(process.argv[3], body, function (error) {
    if (error) {
      console.error('error:', error);
    }
  });
});
