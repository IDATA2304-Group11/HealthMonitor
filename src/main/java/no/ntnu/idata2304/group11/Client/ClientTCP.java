package no.ntnu.idata2304.group11.Client;
import java.io.*;
import java.net.Socket;
import java.net.UnknownHostException;
import static java.lang.System.in;

/**
 * This class represent the TCP client
 * @author Ole Kristian Dvergsdal
 * @version 1.0
 */
public class ClientTCP {
    private Socket socket;
    private BufferedReader input;
    private PrintWriter output;

    /**
     * The connstructer of the socket connection for the client.
     * @param address address to the server you want to connect to.
     * @param portNumber TCP port number you want to connect to.
     */
    public ClientTCP(String address, int portNumber) {
        String line = "";
        try {
            this.socket = new Socket(address, portNumber);
            //System.out.println("Connected");
            this.input = new BufferedReader(new InputStreamReader(in));
            this.output = new PrintWriter(socket.getOutputStream());
        }
        catch (UnknownHostException unknownHost) {
            unknownHost.printStackTrace();
        }
        catch (IOException exception) {
            exception.printStackTrace();
        }

        //keeps the connection running until DISCONNECT is written and run in the terminal.
        while (!line.equals("DISCONNECT")) {
            try{

                line = this.input.readLine();
                this.output.println(line);
            }
            catch (IOException exception) {
                exception.printStackTrace();
            }
        }

        //closes the connecction
        try {
            this.socket.close();
            this.input.close();
            this.output.close();
        }
        catch (IOException exception) {
            exception.printStackTrace();
        }
    }
}
