package no.ntnu.idata2304.group11.app;

import no.ntnu.idata2304.group11.client.ftp.FtpClient;
import org.eclipse.paho.client.mqttv3.MqttException;

import no.ntnu.idata2304.group11.client.mqtt.Mqtt;

import java.io.IOException;

/**
 * Class starts the main application.
 */
public class App {

    public static void main(String[] args) throws MqttException, IOException {
        //Mqtt mqtt = new Mqtt("129.241.152.12","1883","102");
        FtpClient ftpClient = new FtpClient();
        ftpClient.disconnect();
    }

}