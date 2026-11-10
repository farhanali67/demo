const camelCase = require("lodash/camelCase");

const value = camelCase("CodeArtifact npm proxy works");
if (value !== "codeArtifactNpmProxyWorks") {
  throw new Error(`Unexpected lodash result: ${value}`);
}

console.log("npm dependency resolved through CodeArtifact successfully.");

