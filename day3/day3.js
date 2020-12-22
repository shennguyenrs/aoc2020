const fs = require('fs');

// Read file to lines
const lines = fs.readFileSync('entries.txt', 'utf-8').trim().split('\n');

const countTree = (rSlope, dSlope) => {
  let linePos = 0;
  let counter = 0;
  let xPos = 0;

  while (linePos < lines.length) {
    counter += lines[linePos][xPos] === '#' ? 1 : 0;
    linePos += dSlope;
    xPos = (xPos + rSlope) % lines[0].length;
  }

  return counter;
};

// Part one
console.log(`Part One: ${countTree(3, 1)}`);

// Part Two
const result = [
  [1, 1],
  [3, 1],
  [5, 1],
  [7, 1],
  [1, 2],
]
  .map(([right, down]) => countTree(right, down))
  .reduce((a, b) => a * b);

console.log(`Part Two: ${result}`);
