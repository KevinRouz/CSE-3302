//Kevin Farokhrouz
//1002072886
//10-01-2024

let inputtable = [1,2,3,4,5,6,7,8,9,10]; // Create an array of all numbers from 1 to 10

//map() is used for these to create a new array based on the requirements.
let fiveTable = inputtable.map(x => x * 5); // Create an array of all multiples of 5 from 1 to 51
console.log(fiveTable);

let thirteenTable = inputtable.map(x => x * 13); // Create an array of all multiples of 13 from 1 to 131
console.log(thirteenTable);

let squaresTable = inputtable.map(x => x * x); // Create an array of all squares of nums 1 to 10
console.log(squaresTable);

let newTable = fiveTable.concat(fiveTable.map(x => x + 50)); // Uses fiveTable as a basis to create an array of all multiples of 5 from 1 to 100
console.log(newTable);

function isOddAndMult5(num){ // Checks if a number is odd and a multiple of 5
    return (num % 2 === 1) && (num % 5 === 0);
};

let oddAndMult5 = newTable.filter(isOddAndMult5); // Filter newTable based on nums odd and multiple of 5
console.log(oddAndMult5);

function isEvenAndMult7(num){   // Same as line 16, but for even and 7
    return (num % 2 === 0) && (num % 7 === 0);
}

let numbers = Array.from({ length: 100 }, (_, i) => i + 1); // Create an array from 1 to 100 without iterables or loops
let evenAndMult7 = numbers.filter(isEvenAndMult7); // Filter numbers array based on nums even and multiple of 7
console.log(evenAndMult7);

let sumOfEvenAndMult7 = evenAndMult7.reduce((sum, num) => sum + num, 0); // Sum up all even multiples of 7
console.log(sumOfEvenAndMult7);

function cylinder_volume(r){ // Curry the cylinder_volume function to take radius first, then height
    return function(h) { // Return function to accept height and calculate volume
        var volume = 3.14 * r * r * h; // Formula to calculate cylinder volume
        return volume;
    }
}

let volWithRadius5 = cylinder_volume(5); // Fix the radius at 5

let volume1 = volWithRadius5(10); // Use the curried function to calculate volume when h=10
console.log(volume1);

let volume2 = volWithRadius5(17); // Use the curried function to calculate volume when h=17
console.log(volume2);

let volume3 = volWithRadius5(11); // Use the curried function to calculate volume when h=11
console.log(volume3);

makeTag = function(beginTag, endTag){ // Function to generate HTML tags using closures
    return function(textcontent){ // Inner function takes content and wraps it in beginTag and endTag
       return beginTag + textcontent + endTag; 
    } 
}

let makeTable = makeTag("<table>", "</table>"); // Use makeTag to create a table
let makeRow = makeTag("<tr>", "</tr>"); // Use makeTag to create table rows
let makeCell = makeTag("<td>", "</td>"); // Use makeTag to create table cells

let headerRow = makeRow( // Create a header row with column titles
  makeTag("<th>", "</th>")("Name") + makeTag("<th>", "</th>")("Occupation") + makeTag("<th>", "</th>")("Age")
);

let row1 = makeRow( // Create the first data row with values
  makeCell("Kevin") + makeCell("Software Engineer") + makeCell("25")
);

let row2 = makeRow( // Create the second data row with values
  makeCell("Sammy") + makeCell("Research Assistant") + makeCell("27")
);

let table = makeTable(headerRow + row1 + row2); // Wrap the rows in a table tag
console.log(table);

function makeChecker(multiple, evenOdd) { // General function to check multiples and even/odd condition
    let rem;
    switch(evenOdd) { // Determine remainder based on whether we're checking for "even" or "odd"
        case "even":
            rem = 0;
            break;
        case "odd":
            rem = 1;
            break;
        default:
            throw new Error("invalid usage: use 'even' or 'odd'. ex: makeChecker(5, \"odd\")."); // Error if neither is provided
    }

    return function(num) { // Return a function that checks if num is a multiple and satisfies the even/odd condition
        return (num % multiple === 0) && (num % 2 === rem);
    }
}

let oddMult5Checker = makeChecker(5, "odd"); // Create a function that checks for odd multiples of 5
let oddMult5 = numbers.filter(oddMult5Checker); // Use the checker to filter numbers array for odd multiples of 5
console.log(oddMult5);

let evenMult7Checker = makeChecker(7, "even"); // Create a function that checks for even multiples of 7
let evenMult7 = numbers.filter(evenMult7Checker); // Use the checker to filter numbers array for even multiples of 7
console.log(evenMult7);
