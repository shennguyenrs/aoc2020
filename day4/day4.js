const fs = require('fs');

// Read file to lines
const lines = fs.readFileSync('entries.txt', 'utf-8').split('\n');

const conditions = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'];
let fieldsOne = 0;
let fieldsTwo = 0;
let countOne = 0;
let countTwo = 0;
let dataLen = lines.length;

const partTwo = (key, value) => {
  switch (key) {
    // byr
    case conditions[0]: {
      if (Number(value) >= 1920 && Number(value) <= 2002) return true;
      return false;
    }

    // iyr
    case conditions[1]: {
      if (Number(value) >= 2010 && Number(value) <= 2020) return true;
      return false;
    }

    // eyr
    case conditions[2]: {
      if (Number(value) >= 2020 && Number(value) <= 2030) return true;
      return false;
    }

    // hgt
    case conditions[3]: {
      const lenValue = value.length;
      const unit = value.slice(lenValue - 2, lenValue);
      const hgt = Number.isInteger(Number(unit))
        ? Number(value)
        : Number(value.slice(0, lenValue - 2));

      if (unit === 'cm') {
        if (hgt >= 150 && hgt <= 193) return true;
        return false;
      } else {
        if (hgt >= 59 && hgt <= 76) return true;
        return false;
      }
    }

    // hcl
    case conditions[4]: {
      const pattern = RegExp('^#([a-f]|[0-9]){6}$', 'g');
      return pattern.test(value);
    }

    // ecl
    case conditions[5]: {
      const ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'];
      return ecl.includes(value);
    }

    // pid
    case conditions[6]: {
      const pattern = RegExp('[0-9]{9}$', 'g');
      return pattern.test(value);
    }

    default:
      return false;
  }
};

// Count Part One
lines.forEach((line) => {
  const lineLen = line.length;
  dataLen -= 1;

  if (lineLen !== 1) {
    line.split(' ').forEach((token) => {
      const [key, value] = token.split(':');
      fieldsOne += conditions.includes(key) ? 1 : 0;
      fieldsTwo += partTwo(key, value) ? 1 : 0;
      // console.log(`${lineLen}\t${key}\t${value}`);
    });
  }

  if (lineLen === 1 || dataLen === 0) {
    countOne += fieldsOne === 7 ? 1 : 0;
    countTwo += fieldsTwo === 7 ? 1 : 0;
    fieldsOne = 0;
    fieldsTwo = 0;
  }
});

console.log(`Part One: ${countOne}`);
console.log(`Part Two: ${countTwo}`);
