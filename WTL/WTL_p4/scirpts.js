let currentInput = "";  // Stores the current input string

// Function to append numbers to the display
function appendNumber(number) {
    currentInput += number;  // Append the number to the input string
    document.getElementById('result').value = currentInput;
}

// Function to append operators to the display
function appendOperator(operator) {
    currentInput += " " + operator + " ";  // Add operator with spaces for clarity
    document.getElementById('result').value = currentInput;
}

// Function to clear the display
function clearResult() {
    currentInput = "";  // Clear the current input
    document.getElementById('result').value = currentInput;
}

// Function to calculate the result
function calculate() {
    try {
        // Replace spaces for easier evaluation and evaluate the expression
        let result = eval(currentInput.replace(/ /g, ''));
        document.getElementById('result').value = result;
        currentInput = result.toString();  // Update the input with the result for further calculations
    } catch (error) {
        document.getElementById('result').value = "Error";  // Display error if invalid expression
        currentInput = "";
    }
}
