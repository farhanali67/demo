const camelCase = require("lodash/camelCase");
const axios = require("axios");
const dayjs = require("dayjs");

const value = camelCase("CodeArtifact npm proxy works");
if (value !== "codeArtifactNpmProxyWorks") {
  throw new Error(`Unexpected lodash result: ${value}`);
}

if (typeof axios.create !== "function" || !dayjs("2026-01-01").isValid()) {
  throw new Error("Public npm dependencies were not loaded correctly.");
}

console.log("lodash, axios, and dayjs resolved through CodeArtifact successfully.");

