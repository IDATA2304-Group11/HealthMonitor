package no.ntnu.idata2304.group11;

import no.ntnu.idata2304.group11.Client.ClientTCP;
import no.ntnu.idata2304.group11.ui.UI;

/**
 * Class starts the main application.
 */
public class App {

    public static void main(String[] args) {
        //UI ui = new UI();
        //ui.start();
        ClientTCP client = new ClientTCP("1.241.152.12", 1883);
        
    }

}