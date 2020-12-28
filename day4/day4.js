const fs = require('fs');

// Read file to lines
const lines = fs.readFileSync('entries.txt', 'utf-8').split('\r\n');

const conditions = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'];
let fieldsOne = 0;
let fieldsTwo = 0;
let countOne = 0;
let countTwo = 0;
let dataLen = lines.length;

const validateNumber = (number, min, max) => number >= min && number <= max;

const fieldsValidator = {
  byr: (value) => validateNumber(Number(value), 1920, 2002),
  iyr: (value) => validateNumber(Number(value), 2010, 2020),
  eyr: (value) => validateNumber(Number(value), 2020, 2030),
  hgt: (value) => {
    const cm = /^(\d+)cm$/.exec(value);
    if (cm) return validateNumber(Number(cm[1]), 150, 193);

    const inch = /^(\d+)in/.exec(value);
    if (inch) return validateNumber(Number(inch[1]), 59, 76);

    return false;
  },
  hcl: (value) => /^#([0-9a-f]){6}$/.test(value),
  ecl: (value) => /^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$/.test(value),
  pid: (value) => /^[0-9]{9}$/.test(value),
  cid: () => false,
};

// Count Part One
lines.forEach((line) => {
  const lineLen = line.length;
  dataLen -= 1;

  if (lineLen !== 0) {
    line.split(' ').forEach((token) => {
      const [key, value] = token.split(':');
      fieldsOne += conditions.includes(key) ? 1 : 0;
      fieldsTwo += fieldsValidator[key](value) ? 1 : 0;
    });
  }

  if (lineLen === 0 || dataLen === 0) {
    countOne += fieldsOne === 7 ? 1 : 0;
    countTwo += fieldsTwo === 7 ? 1 : 0;
    fieldsOne = 0;
    fieldsTwo = 0;
  }
});

console.log(`Part One: ${countOne}`);
console.log(`Part Two: ${countTwo}`);
