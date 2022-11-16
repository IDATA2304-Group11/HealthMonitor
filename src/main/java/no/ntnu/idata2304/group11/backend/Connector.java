package no.ntnu.idata2304.group11.backend;

import java.sql.*;

/**
 * With this class, you can connect to the db server.
 * The dbserver is finsveen_dev
 * @author Ole Kristian Dvergsdal
 * @version 1.0
 */
public class Connector {

    /**
     * Connects to the server finsveen_dev
     * @param username the username of the user you want to connect with
     * @param password password of the user you want to connect with
     * @throws SQLException
     */

    //VI SKAL BRUKE BRUKERNAMN: windows@f328341 OG PASSORD:NtnuGruppe11
    public void connecToDB(String username, String password) throws SQLException {
        try (
            //Creat a connection to the server ...., with username and password.
            Connection conn = DriverManager.getConnection("jdb:finsveen_dev://mysql579.loopia.se", username, password)) {
            //Create a statment
            try(Statement stmt = conn.createStatement()) {
                //Querys
                try(ResultSet rs = stmt.executeQuery("WRITE QUREY HERE")) {
                    //Results
                    rs.first();
                    System.out.println(rs.getString(1));
                }
            }
        }
         catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

