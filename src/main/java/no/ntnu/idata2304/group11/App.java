package no.ntnu.idata2304.group11;

import no.ntnu.idata2304.group11.Client.Mqtt;
import org.eclipse.paho.client.mqttv3.MqttException;

import java.io.IOException;

/**
 * Class starts the main application.
 */
public class App {

    public static void main(String[] args) throws MqttException, IOException {
        Mqtt mqtt = new Mqtt("129.241.152.12","1883","102");
    }

}