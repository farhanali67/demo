package com.tappayments.demo;

import org.apache.commons.lang3.StringUtils;

public final class App {
    private App() { }

    public static void main(String[] args) {
        if (!StringUtils.isNotBlank("CodeArtifact")) {
            throw new IllegalStateException("Apache Commons Lang was not resolved correctly.");
        }
        System.out.println("Maven dependency resolved through CodeArtifact successfully.");
    }
}

