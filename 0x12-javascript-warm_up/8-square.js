#!/usr/bin/node
const n = parseInt(process.argv[2]);
if (Number.isNaN(n)) {
  console.log('Missing size');
} else {
  for (let a = 0, s; a < n; a++) {
    s = '';
    for (let j = 0; j < n; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
