#!/usr/bin/node
let a = parseInt(process.argv[2]);
if (Number.isNaN(a)) {
  console.log('Missing number of occurrences');
} else {
  while (a > 0) {
    console.log('C is fun');
    a--;
  }
}
