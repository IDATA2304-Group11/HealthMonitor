package no.ntnu.idata2304.group11.Server;

import org.eclipse.paho.client.mqttv3.IMqttClient;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import java.util.UUID;

/**
 * This class represent the MQTT Protocol. It is used to connect the microcontrollers and sensor to the cloud.
 * @author Ole Kristian Dvergsdal
 * @version 1.0
 */
public class Mqtt {
    //Gives a random UUID to the new client.
    private String id = UUID.randomUUID().toString();
    //The broker host on IP 129.241.152.12 and on Port 1883.
    private String broker = "tcp://129.241.152.12:1883";
    //Sets up the client.
    private IMqttClient client = new MqttClient(broker, id);
    //
    private MqttConnectOptions options = new MqttConnectOptions();

    public Mqtt() throws MqttException {
        //Will automatically try to reconnect to the server in the event of a network failure.
        options.setAutomaticReconnect(true);
        //Will discard unset messages from a previous run.
        options.setCleanSession(true);
        //Connection timeout is set to 10 seconds.
        options.setConnectionTimeout(10);
        client.connect(options);
    }
}