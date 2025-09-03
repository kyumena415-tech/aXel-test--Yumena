const args = require('minimist')(process.argv.slice(2));
const name = args.name || "World";
console.log(`Hello, ${name}!`);
