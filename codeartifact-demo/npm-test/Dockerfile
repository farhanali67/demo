# syntax=docker/dockerfile:1.7
FROM node:24-alpine

WORKDIR /app
COPY package.json ./

# The .npmrc is mounted only for dependency installation and is not retained in the image.
# --loglevel=http shows the CodeArtifact registry URLs in the Jenkins console.
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm install --no-progress --loglevel=http

COPY index.js ./
CMD ["npm", "test"]

