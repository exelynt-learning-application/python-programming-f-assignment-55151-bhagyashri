// Number Comparison Program in TypeScript

// Function to compare two numbers and display results
function compareNumbers(num1: number, num2: number): void {
    // Check which number is greater
    const isNum1Greater: boolean = num1 > num2;
    const isNum2Greater: boolean = num2 > num1;

    // Check if both numbers are equal
    const areNumbersEqual: boolean = num1 === num2;

    // Check if both numbers are positive
    const areBothPositive: boolean = num1 > 0 && num2 > 0;

    // Using logical operators (and, or, not) for comparisons
    const positiveOrEqual: boolean = (num1 > 0 || num2 > 0) || areNumbersEqual;

    // Displaying the results
    console.log("\n--- Comparison Results ---");
    console.log(`Is num1 greater than num2? ${isNum1Greater}`);
    console.log(`Is num2 greater than num1? ${isNum2Greater}`);
    console.log(`Are num1 and num2 equal? ${areNumbersEqual}`);
    console.log(`Are both numbers positive? ${areBothPositive}`);
    console.log(`Are either of the numbers positive or both numbers equal? ${positiveOrEqual}`);
}

// Taking user input for two numbers (using prompt or custom input method)
const num1: number = parseFloat(prompt("Enter the first number: ") || "0");
const num2: number = parseFloat(prompt("Enter the second number: ") || "0");

// Call the comparison function
compareNumbers(num1, num2);