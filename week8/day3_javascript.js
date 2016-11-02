console.log("Getting started with javascript");

var myNumber = 10 / 90.23;
console.log(myNumber);

var myArray = [10, "joel", [10, 90, 23], "peanut"];
console.log(myArray);
console.log(myArray[2][1]);

// for counter, item in enumerate(array):

for (var i = 0 ; i < myArray.length ; i++) {
    // var item = myArray[i];
    console.log(myArray[i]);
}

var myObject = {
    myName: "joel",
    myAge: 33
};

console.log(myObject["myName"]);
console.log(myObject.myName);

var myFunc = function(x, y) {
    return x * y;
};

console.log(myFunc(9, 4));

var sillyArray = [9, 34, 123, 12, 4, 52];

var loopFunc = function(item) {
    console.log(item);
};

sillyArray.forEach(loopFunc);

sillyArray.forEach(function(item) {
    console.log(item);
});
