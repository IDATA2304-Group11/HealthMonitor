package no.ntnu.idata2304.group11.backend;

import static org.junit.Assert.assertEquals;

import java.sql.SQLException;
import java.util.ArrayList;

import org.junit.Test;

public class DataBaseClientTest {
    

    @Test
    public void getStatusTest() throws SQLException {
        assertEquals("stable", DataBaseClient.getStatus(1001));
    }


    @Test
    public void getPIDTest() throws SQLException {
        assertEquals("1001", DataBaseClient.getPID("E89X-2JKL-5420-GH42"));
        System.out.println(DataBaseClient.getPID("E89X-2JKL-5420-GH42"));
    }

    @Test
    public void testStatus() throws SQLException {
        DataBaseClient.setStatus("1003", "critical");
        assertEquals("unusual", DataBaseClient.getStatus(1007));
    }

    @Test
    public void testGetMeasurements() throws SQLException {
        ArrayList<ArrayList<String>> result = DataBaseClient.getMeasurements("1001", 10);

        for (String s : result.get(0)) {
            System.out.println(s);
        }
    }

    @Test
    public void testInsertMeasurement() throws SQLException {
        DataBaseClient.insertMeasurement("1001", "2015-04-27 23:02:04.0", "120", "81", "76");
        ArrayList<ArrayList<String>> result = DataBaseClient.getMeasurements("1001", 1);

        for (String s : result.get(0)) {
            System.out.println(s);
        }
    }
}
