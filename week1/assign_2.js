const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.once('line', () => {
    rl.on('line', readLine);
});

function readLine(line) {
    const arr = line.toString().split(' ').map(Number);
    console.log(max(arr))
    process.exit();
}

const max = arr => {
  if (arr.length === 2) { return arr[0] * arr[1]; }
  const maxValues = arr.reduce((acc, val) => {
    if (val > acc.max1) {
      if (val > acc.max2) {
        acc.max1 = acc.max2;
        acc.max2 = val;
      } else {
        acc.max1 = val;
      }
    }
    return acc;
  }, {max1: Number.MIN_SAFE_INTEGER, max2: Number.MIN_SAFE_INTEGER})

  return maxValues.max1 * maxValues.max2;
}
