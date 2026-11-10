# syntax=docker/dockerfile:1.7
FROM node:24-alpine

WORKDIR /app
COPY package.json ./

# The .npmrc is mounted only for dependency installation and is not retained in the image.
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm install --no-progress

COPY index.js ./
CMD ["npm", "test"]

