#!/usr/bin/node
class Rectangle {
    constructor(w,h) {
        if ((w > 0) && (h > 0)) {
            this.width = w;
            this.height = h;
        }
    }

    print() {
        for (let a = 0; a < h; a++){
            for (b = 0; b < w; b++){
                s += 'X';
            }
            s += '\n';
            console.log(s);
        }
    }
}

module.exports = Rectangle;
