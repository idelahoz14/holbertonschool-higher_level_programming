#!/usr/bin/node
// Script that print a number

const argument = parseInt(process.argv[2]);
if (argument * 1 === argument) {
  console.log('My number: ' + argument);
} else {
  console.log('Not a number');
}
