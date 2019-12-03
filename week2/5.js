// fib n mod m

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine(line) {
    if (line !== "\n") {
        const n = parseInt(line.toString().split(' ')[0], 10);
        const m = parseInt(line.toString().split(' ')[1], 10);

        console.log(getFibMod(n, m));
        process.exit();
    }
}

function getFibMod(n, m) {
  const pisanoPeriodResult = pisanoPeriod(m);
  n = n % pisanoPeriodResult;

  return n <= 1 ? n : fibModHelper(n, m)
}

function fibModHelper(n, m) {
    let nOne = 0;
    let nTwo = 1;
    for (let i = 2; i <= n; i++) {
      const res = (nOne + nTwo) % m;
      nOne = nTwo;
      nTwo = res;
    }

    return nTwo % m;
}

function pisanoPeriod(m) {
  let previous = 0;
  let current = 1;
  const end = m * m;

  for (let i = 0; i < end; i++) {
    const next = (previous + current) % m;
    previous = current;
    current = next;
    if (previous === 0 && current === 1) { return i + 1; }
  }
}

module.exports = getFibMod;
