#!/usr/bin/node
/**
  reads and prints the content of a file
  first argument is the file path
 */
const myArgs = process.argv.slice(2);
const fs = require('fs');
fs.writeFile(myArgs[0], myArgs[1], 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
