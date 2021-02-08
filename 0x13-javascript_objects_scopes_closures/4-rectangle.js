#!/usr/bin/node
// class Rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log(('X'.repeat(this.width)));
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const container = this.width;
    this.width = this.height;
    this.height = container;
  }
}
module.exports = Rectangle;
