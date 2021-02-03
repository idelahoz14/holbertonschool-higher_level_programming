#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2);
  numbers.map(number => Number.parseInt(number)).sort((a, b) => a - b);
  console.log(numbers[numbers.length - 2]);
}
