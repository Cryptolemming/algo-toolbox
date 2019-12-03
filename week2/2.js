// last digit of large fib number

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine(line) {
    console.log(fib(parseInt(line, 10)));
    process.exit();
}

function fib(n) {
    if (n <= 1) { return n; }
    let nOne = 0;
    let nTwo = 1;
    for (let i = 2; i <= n; i++) {
      const lastDigit = (nOne + nTwo) % 10;
      nOne = nTwo;
      nTwo = lastDigit;
    }

    return nTwo;
}

module.exports = fib;
