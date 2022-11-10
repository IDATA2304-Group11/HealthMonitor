package no.ntnu.idata2304.group11.client.tcp;

import java.io.IOException;

/**
 * Starting point of the backend implementation of
 * the application.
 * 
 * @since    15-10-2022
 * @version  10-11-2022
 * @author   jorgenfinsveen
 */
public class Main {

    /**
     * Creates a receiver-instance.
     */
    public static void main(String[] args) throws IOException {
        RaspberryPiServer server = new RaspberryPiServer();
        server.run();
    }
}