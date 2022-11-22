package no.ntnu.idata2304.group11.backend;

import java.sql.*;

/**
 * With this class, you can connect to the db server.
 * The dbserver is finsveen_dev
 * @author Ole Kristian Dvergsdal
 * @version 1.0
 */
public class DbClient {

    //The connection
    private Connection conn;

    /**
     * Create the db client object.
     * The client is connected to the db server finsveen_dev.
     *
     * @param username of the user that want to log in
     * @param password for the user that want to log in
     * @throws SQLException
     */
    public DbClient(String username, String password) throws SQLException {
        //Creates a connection to the db server finsveen_dev.
        this.conn = DriverManager.getConnection("jdb:finsveen_dev://mysql579.loopia.se", username, password);
    }

    /**
     * Query information from a Patient form a given table.
     * @param table what table you want to get information from.
     * @param pid the ID of the Patient that you want to query.
     * @throws SQLException
     */
    public void queryFromPationTable(String table ,int pid) throws SQLException {
        Statement stmt = this.conn.createStatement();
        try {
            ResultSet rs = stmt.executeQuery("SELECT * FROM " + table + " WHERE PID = " + pid);
            try {
                while (rs.next()) {
                    rs.first();
                    //TODO FIND OUT HOW TO RETREVE THE RESULTS
                    System.out.println(rs.getString(1));
                }
            } finally {
                try {
                    rs.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        } finally {
            try {
                stmt.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * Update the information in a table.
     * @param table the table you want to update infromation on.
     * @param colum the colum you want to update the information. Here you need to spiffies what colum and new vale for the colum.
     * @param newVale the new vale you want to set in the colum.
     * @param pid the ID of the pation you want to update information in.
     * @throws SQLException
     */
    public void updatePationTab(String table, String colum, String newVale, int pid) throws SQLException {
        Statement stmt = this.conn.createStatement();
        try {
            ResultSet rs = stmt.executeQuery("UPDATE " + table + " SET " + colum + " = " + newVale + " WHERE PID = " + pid);
            try {
                while (rs.next()) {
                    rs.first();
                    System.out.println(rs.getString(1));
                }
            }finally {
                try {
                    rs.close();
                }catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }finally {
            try {
                stmt.close();
            }catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * insert new row to the table Patient.
     * @param pid ID of patient.
     * @param name of patient.
     * @param age of patient.
     * @param gender of patient.
     * @throws SQLException
     */
    public void insertToPatientTable(int pid, String name, int age, String gender) throws SQLException{
        Statement stmt = this.conn.createStatement();
        try {
            ResultSet rs = stmt.executeQuery("INSERT INTO Patient(PID, name, age, gender) VALUES (" + pid + " ," + name + " ," + age + " ," + gender + ")");
            try {
                while (rs.next()) {
                    rs.first();
                    System.out.println(rs.getString(1));
                }
            }finally {
                try {
                    rs.close();
                }catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }finally {
            try {
                stmt.close();
            }catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
