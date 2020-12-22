const fs = require('fs');

// Read file to lines
const lines = fs.readFileSync('entries.txt', 'utf-8').trim().split('\n');

let partOne = 0;
let partTwo = 0;

// Count valid passwords
lines.forEach((line) => {
  const [limit, key, string] = line.split(' ');
  const [lower, upper] = limit.split('-').map((x) => Number(x));

  let found = 0;

  [...string].forEach((c) => {
    found += c === key[0] ? 1 : 0;
  });

  partOne += found >= lower && found <= upper ? 1 : 0;

  const atLower = string[lower - 1] === key[0] ? 1 : 0;
  const atUpper = string[upper - 1] === key[0] ? 1 : 0;

  partTwo += atUpper + atLower === 1 ? 1 : 0;
});

// Print out the result
console.log(`Part One: ${partOne}`);
console.log(`Part Two: ${partTwo}`);
