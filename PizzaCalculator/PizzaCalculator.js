var document;

// Crust variables
var crustPrice;
var crustValue;

// Size variables
var sizePrice;
var sizeValue;

// Sauce variables
var sauceValue;

// Toppings variables
var toppingsPrice;
var numToppings;
var sizeToppings;

// Total price variable
var totalPrice;
var stringPrice;

//var submitButton = document.getElementsByClassName("totalPrompt");
//var totalPrompt = document.getElementsByClassName("totalPrompt");

function calculatePrice() {
    // Calculate the prices for each element of the pizza
    crustPrice = calculateCrust();
    sizePrice = calculateSize();
    toppingsPrice = calculateToppings();
    // Calculate the price for the entire pizza
    totalPrice = crustPrice + sizePrice + toppingsPrice;
    
    // Print the total price of the pizza
    stringPrice = convertPrice();
    //alert("Total cost of Pizza: " + stringPrice);
    document.getElementById("total").innerHTML = stringPrice;
}

// Prices for crust: 5 = thin, 7 = regular, 10 = deep dish
function calculateCrust() {
    crustPrice = 0;
    if (document.getElementById("thin").checked === true) {
        crustPrice += 5;
        //crustValue = document.getElementById("thin").value;
    }
    if (document.getElementById("regular").checked === true) {
        crustPrice += 7;
        //crustValue = document.getElementById("regular").value;
    }
    if (document.getElementById("deep dish").checked === true) {
        crustPrice += 10;
        //crustValue = document.getElementById("deep dish").value;
    }
    
    // Error handling for user not selecting a crust thickness
    if (crustPrice === 0) {
        document.getElementById("warning 1").innerHTML = "Please select a crust thickness";
    }
    return crustPrice;
}

// Prices for size: 5 = small, 10 = medium, 15 = large
function calculateSize() {
    sizePrice = 0;
    sizeValue = "";
    if (document.getElementById("small").checked === true) {
        sizePrice += 5;
        //sizeValue = document.getElementById("small").value;
    }
    if (document.getElementById("medium").checked === true) {
        sizePrice += 10;
        //sizeValue = document.getElementById("medium").value;
    }
    if (document.getElementById("large").checked === true) {
        sizePrice += 15;
        //sizeValue = document.getElementById("large").value;
    }
    
    // Error handling for user not selecting a size
    if (sizePrice === 0) {
        document.getElementById("warning 2").innerHTML = "Please select a size";
    }    
    return sizePrice;
}

function calculateToppings () {
    toppingsPrice = 0;
    numToppings = 0;
    sizeToppings = 0;
    
    // Calculates how many toppings have been selected
    if (document.getElementById("pepperoni").checked === true) {
        numToppings += 1;
    }
    if (document.getElementById("sausage").checked === true) {
        numToppings += 1;
    }
    if (document.getElementById("onion").checked === true) {
        numToppings += 1;
    }
    if (document.getElementById("garlic").checked === true) {
        numToppings += 1;
    }
    if (document.getElementById("green pepper").checked === true) {
        numToppings += 1;
    }
    if (document.getElementById("mushrooms").checked === true) {
        numToppings += 1;
    }
    if (document.getElementById("black olives").checked === true) {
        numToppings += 1;
    }
    
    // Error handling for user selecting too many toppings
    if (numToppings >= 3) {
        document.getElementById("warning 3").innerHTML = "Please select three or fewer toppings";
    } 
    
    // Calculates the size of the toppings being added:
    // Small multiplies the number of toppings by one
    // Medium multiplies the number of toppings by two
    // Large multiplies the number of toppings by three
    if (sizeValue === "small") {
        sizeToppings = 1;
    }
    if (sizeValue === "medium") {
        sizeToppings = 2;
    }
    if (sizeValue === "large") {
        sizeToppings = 3;
    }
    
    // Total price for toppings is the number of toppings times 1, 2, or 3 (depending on size)
    toppingsPrice = numToppings * sizeToppings;
    return toppingsPrice;
}

function convertPrice() {
    stringPrice = "";
    var tempString = totalPrice.toString();
    stringPrice += "$ ";
    stringPrice += tempString;
    stringPrice += ".00";
    return stringPrice;
}