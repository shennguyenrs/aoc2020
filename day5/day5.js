const fs = require('fs');

// Read file to lines
const lines = fs.readFileSync('entries.txt', 'utf-8').split('\n');

const result = [];

// Calculate seat id
lines.forEach((line) => {
  let top = 127;
  let bot = 0;
  let rgt = 7;
  let lft = 0;
  let col = 0;
  let row = 0;

  for (let i = 0; i < line.length; i += 1) {
    const char = line[i];

    if (char === 'F') {
      row = Math.floor((top + bot) / 2);
      top = row;
    } else if (char === 'B') {
      row = Math.ceil((top + bot) / 2);
      bot = row;
    } else if (char === 'L') {
      col = Math.floor((rgt + lft) / 2);
      rgt = col;
    } else {
      col = Math.ceil((rgt + lft) / 2);
      lft = col;
    }
  }

  result.push(row * 8 + col);
});

// Sort result list
result.sort((a, b) => a - b);

// Part one
console.log(`Part one: ${result[result.length - 1]}`);

// Part two
for (let i = 0; i < result.length; i += 1) {
  if (result[i + 1] - result[i] === 2) {
    console.log(`Part Two (need to be added by 1): ${result[i]}`);
    break;
  }
}
