// string_datatype.ts
export {};

/**
 * This program demonstrates basic string operations in TypeScript.
 * It shows string concatenation, slicing, methods, substring checking, and string length calculation.
 */

// Defining strings with type annotations
const greeting: string = "Hello";  // Type annotation for string
const name: string = "Alice";      // Type annotation for string

// Concatenating strings
const message: string = greeting + " " + name;
console.log(message);  // Output: "Hello Alice"

// String slicing (TypeScript doesn't support slicing directly, so we use substring)
console.log(name.substring(1, 4));  // Output: "lic"

// String methods
console.log(message.toUpperCase());  // Output: "HELLO ALICE"
console.log(message.toLowerCase());  // Output: "hello alice"
console.log(message.replace("Alice", "Bob"));  // Output: "Hello Bob"

// Checking for substring
if (message.includes("Alice")) {
    console.log("Alice is in the message.");
}

// String length
console.log("Length of the message:", message.length);  // Output: Length of the message: 11