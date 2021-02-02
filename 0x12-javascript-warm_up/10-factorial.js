#!/usr/bin/node
// Script that computes and prints a factorial

function factorial (a) {
  let number = 1;
  for (let i = 1; i <= a; i++) {
    number *= i;
  }
  return number;
}
console.log(factorial(process.argv[2]));
