/**
Complete the function getLastCharacter such that it returns the last character of the name parameter it receives.
*/

/**
 * @param {string} name
 */
function getLastCharacter(name) {
    const ultimate = name.charAt(name.length - 1);
    return ultimate

}

// Sample usage - do not modify
console.log(getLastCharacter("Sam")); // "m"
console.log(getLastCharacter("Alex")); // "x"
console.log(getLastCharacter("Charley")); // "y"
