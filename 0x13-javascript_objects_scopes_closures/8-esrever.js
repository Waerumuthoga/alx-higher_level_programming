#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let a = 0;

  while ((len - a) > 0) {
    const alt = list[len];
    list[len] = list[a];
    list[a] = alt;
    a++;
    len--;
  }
  return list;
};
