const fs = require('fs');

// Read lines to data
const lines = fs.readFileSync('./entries.txt', 'utf-8').split('\n');

const charSet = new Set();
let countAns = 0;

// Calculate part one
lines.forEach((line) => {
  if (line.length !== 0) {
    [...line].forEach((char) => {
      charSet.add(char);
    });
  } else {
    countAns += charSet.size;
    charSet.clear();
  }
});

console.log(`Part one: ${countAns}`);

// Calculate part two
countAns = 0;
const charMap = new Map();
let countLine = 0;

lines.forEach((line) => {
  if (line.length !== 0) {
    countLine += 1;
    [...line].forEach((char) => {
      if (charMap.has(char)) {
        const newValue = charMap.get(char) + 1;
        charMap.delete(char);
        charMap.set(char, newValue);
      } else {
        charMap.set(char, 1);
      }
    });
  } else {
    charMap.forEach((value, key) => {
      countAns += value === countLine ? 1 : 0;
    });
    countLine = 0;
    charMap.clear();
  }
});

console.log(`Part two: ${countAns}`);
