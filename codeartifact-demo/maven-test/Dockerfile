# syntax=docker/dockerfile:1.7
FROM maven:3.9-eclipse-temurin-17 AS build

WORKDIR /build
COPY pom.xml ./
COPY src ./src

# The Maven settings are mounted only for package resolution and are not retained in the image.
RUN --mount=type=secret,id=maven_settings,target=/root/.m2/settings.xml \
    mvn --batch-mode clean package

FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=build /build/target/codeartifact-maven-demo-1.0.0.jar ./app.jar
ENTRYPOINT ["java", "-jar", "/app/app.jar"]

