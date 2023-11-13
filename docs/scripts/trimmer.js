function trimCodeElements(className) {
    // This script is designed to format code blocks on a webpage by removing unnecessary leading spaces while preserving the intended indentation. Here's a step-by-step explanation of how it works:

    // 1. Element Selection: The script selects all elements with a specific class name, typically elements with the class name "trim-code," found on the webpage.

    // 2. Text Content Retrieval: For each selected element, which is expected to contain code blocks, the script retrieves the text content. This content may include code with uneven indentation.

    // 3. Line Separation: The code content is split into individual lines based on newline characters (newline character `\n`). This operation transforms the code into an array where each element represents a line of code.

    // 4. Minimum Indentation Calculation: To maintain consistent indentation, the script calculates the minimum indentation level. It does so by examining each line within the code block, excluding the first and last lines. For each non-empty line, the script determines the number of leading spaces and keeps track of the smallest number of leading spaces.

    // 5. Indentation Removal: The script processes each line in the code block, including the first line, and removes the minimum indentation from each line. This ensures that the code's indentation remains uniform while eliminating unnecessary leading spaces.

    // 6. Text Content Update: After completing the cleaning process, the script updates the text content of the element with the formatted code, making it more readable and visually consistent.

    // This script is useful for enhancing the display of code on webpages, improving its readability by aligning indentation while preserving code structure.

    var elements = document.querySelectorAll("." + className);
    for (var i = 0; i < elements.length; i++) {
        var codeElement = elements[i];
        var codeContent = codeElement.textContent;
        
        // Split the code content into lines
        var codeLines = codeContent.split('\n');
        var minIndent = Number.MAX_SAFE_INTEGER;

        // Find the minimum indentation level
        for (var j = 1; j < codeLines.length - 1; j++) {
            var line = codeLines[j];
            if (line.trim() !== "") {
                var leadingSpaces = line.length - line.trimLeft().length;
                minIndent = Math.min(minIndent, leadingSpaces);
            }
        }

        var cleanedCode = "";

        // Remove the minimum indentation from each line, including the last line
        for (var j = 1; j < codeLines.length; j++) {
            var line = codeLines[j];
            cleanedCode += line.slice(minIndent) + (j === codeLines.length - 1 ? '' : "\n");
        }

        

        codeElement.textContent = cleanedCode;
        console.log(cleanedCode)
    }
}

document.addEventListener('DOMContentLoaded', function() {
    trimCodeElements("trim-code");
});