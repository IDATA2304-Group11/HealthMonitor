package no.ntnu.idata2304.group11.client.ftp;
import org.apache.commons.net.PrintCommandListener;
import org.apache.commons.net.ftp.FTPClient;
import org.apache.commons.net.ftp.FTPFile;
import org.apache.commons.net.ftp.FTPReply;
import java.io.*;
import java.util.Arrays;
import java.util.Collection;

/**
 * This class represent the Client FT Protocol.
 * It is used to transfer data form a client to an FTP server.
 * @author Ole Kristian Dvergsdal
 * @version 1.0
 */
public class FtpClient {

    //The ftp client
    private FTPClient ftp;

    /**
     * Constructor of a ftp client.
     * @param serverIp ip of the server you want to connect to.
     * @param port port number of the server you want to connect to.
     * @param user username you want to log inn with.
     * @param password password you want to log inn with.
     * @throws IOException error if you can't connect to the server.
     */
    public FtpClient(String serverIp, int port, String user, String password) throws IOException {

        //Setts up ftp for use.
        this.ftp = new FTPClient();
        this.ftp.addProtocolCommandListener(new PrintCommandListener(new PrintWriter(System.out)));

        //Sets up different settings for the ftp client
        this.ftp.setConnectTimeout(10);


        //Connecet to server and checks if it connected to the server
        this.ftp.connect(serverIp,port);
        int replay = ftp.getReplyCode();
        if (!FTPReply.isPositiveCompletion(replay)) {
            this.ftp.disconnect();
            throw new IOException("DID NOT CONNECT TO FTP SERVER. Exception error.");
        }

        //login wiht username and password
        this.ftp.login(user, password);
    }

    /**
     * Disconnect from the ftp.
     * @throws IOException error
     */
    public void disconnect() throws IOException {
        this.ftp.disconnect();
    }

    //TODO check if i want to trasnform it to Strings.
    /**
     * List the files.
     * @param path
     * @return
     * @throws IOException
     */
    public Collection<String> listFlies(String path) throws IOException {
        FTPFile[] files = this.ftp.listFiles(path);
        return Arrays.stream(files).map(FTPFile::getName).toList();
    }

    /**
     * Uplodes file to the FTP server
     * @param file the file you want to upload
     * @param path of the file
     * @throws IOException eror
     */
    public void upload(File file, String path) throws IOException {
        this.ftp.storeFile(path, new FileInputStream(file));
    }

    /**
     * download a file from the FTP server
     * @param source of the file.
     * @param destination where you want to download the file to
     * @throws IOException
     */
    public void download(String source, String destination) throws IOException {
        FileOutputStream out = new FileOutputStream(destination);
        this.ftp.retrieveFile(source,out);
    }
}
