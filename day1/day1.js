const fs = require('fs');

// Find couple
function findCouple(data) {
  for (let i = 0; i <= data.length; i += 1) {
    const first = data[i];
    const second = data.slice(i, data.length).filter((x) => x === 2020 - first);

    if (data.filter((x) => x === 2020 - first).length === 1) {
      console.log(`The first number is ${first}`);
      console.log(`The second number is ${second}`);
      console.log(`Their multiply is ${first * second}`);
      return;
    }
  }
}

// Find triplet
function findTriplet(data) {
  for (let i = 0; i < data.length - 2; i += 1) {
    const first = data[i];

    for (let j = i + 1; j < data.length - 1; j += 1) {
      const second = data[j];
      const third = data
        .slice(j, data.length)
        .filter((x) => x === 2020 - first - second);

      if (data.filter((x) => x === 2020 - first - second).length === 1) {
        console.log(`The first number is ${first}`);
        console.log(`The second number is ${second}`);
        console.log(`The third number is ${third}`);
        console.log(`Their multiply is ${first * second * third}`);
        return;
      }
    }
  }
}

// Read file to lines
const lines = fs
  .readFileSync('entries.txt', 'utf-8')
  .trim()
  .split('\n')
  .map((x) => Number(x));

// Sort lines
lines.sort((a, b) => a - b);

// Find couple
findCouple(lines);

console.log();

// Find triplet
findTriplet(lines);
