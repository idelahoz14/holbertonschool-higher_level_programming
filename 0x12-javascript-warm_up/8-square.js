#!/usr/bin/node
// Script that print a square

const length = parseInt(process.argv[2]);
if (length * 1 !== length) {
  console.log('Missing size');
} else {
  for (let i = 0; i < length; i++) {
    console.log('X'.repeat(length));
  }
}
