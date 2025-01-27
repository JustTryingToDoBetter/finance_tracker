module.exports = {
    moduleFileExtensions: ["js", "json", "vue"],
    transform: {
      "^.+\\.js$": "babel-jest",
      "^.+\\.vue$": "vue-jest",
    },
    moduleNameMapper: {
      "^@/(.*)$": "<rootDir>/src/$1", // Correctly map @/ to src/
    },
    testMatch: ["**/tests/unit/**/*.spec.js"], // Look for all test files in the tests/unit folder
  };