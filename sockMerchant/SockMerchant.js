"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", inputStdin => {
  inputString += inputStdin;
});

process.stdin.on("end", _ => {
  inputString = inputString
    .replace(/\s*$/, "")
    .split("\n")
    .map(str => str.replace(/\s*$/, ""));

  main();
});

function readLine() {
  return inputString[currentLine++];
}

// Complete the sockMerchant function below.
function sockMerchant(n, ar = []) {
    if (ar == null || ar.length == 0) {
        console.log("empty pile of socks");
        return null;
    } else if ((n < 1) || (n > 100) || (ar.length > n)) {
        console.log("outside constraints");
        return null;
    } 
    for (let i = 0; i < n; i++) {
        if ((ar[i] > 100) || (ar[i] < 1)) {
            console.log("outside constraints");
            return null;
        }
    }

    let sockTypeCount = {};
    let pairCount = 0;
    for (let j = 0; j < n; j++) {
        if (sockTypeCount.hasOwnProperty(ar[j])) {
            sockTypeCount[ar[j]]++;
            if (sockTypeCount[ar[j]] % 2 == 0) pairCount++;
        } else {
            sockTypeCount[ar[j]] = 1;
        }
    }

    return pairCount;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine(), 10);

  const ar = readLine()
    .split(" ")
    .map(arTemp => parseInt(arTemp, 10));

  let result = sockMerchant(n, ar);

  ws.write(result + "\n");

  ws.end();
}
