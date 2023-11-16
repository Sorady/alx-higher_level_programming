#!/usr/bin/node
/**
  prints the title of a Star Wars movie
 */
const myArgs = process.argv.slice(2);
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
request(url, function (error, response, body) {
  if (!error) {
    const json_ = JSON.parse(body);
    console.log(json_.title);
  }
});
