#!/usr/bin/node
// Script that prints x times “C is fun”

const x = parseInt(process.argv[2]);
if (x * 1 === x) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
