#!/usr/bin/node
// inherits from Rectangle of 4-rectangle.js
const Square1 = require('./5-square.js');

class Square extends Square1 {
  charPrint (c) {
    const container = c;
    if (container === 'C') {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      super.print();
    }
  }
}
const Square2 = Square;
module.exports = Square2;
