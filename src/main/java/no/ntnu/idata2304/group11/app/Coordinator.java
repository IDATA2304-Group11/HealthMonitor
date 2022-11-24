package no.ntnu.idata2304.group11.app;

import java.sql.SQLException;
import java.util.ArrayList;

import no.ntnu.idata2304.group11.backend.DataBaseClient;

/**
 * Processes data received from the analyzer.<p>
 * 
 * Unpacks data and classifies the staus of a patient 
 * by comparing health-parameters and measurements done 
 * by sensors.
 * 
 * @since    10-11-2022
 * @version  10-11-2022
 * @author   jorgenfinsveen
 */
public class Coordinator {
    
    /**
     * Receive the data from the server.
     * 
     * @param message from the server.
     */
    public static void receive(String measurement) {
        System.out.println(measurement);
        String[] data = measurement.split(";");
        Measurement measure = new Measurement(
                                               data[0], data[1], 
                                               data[2], data[3],
                                               data[4]);
        try {
            identifyPatient(measure);
            classifyPatientStatus(measure, 5);
            uploadToDatabase(measure);

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    /**
     * Determine what the health-status of
     * the patient is.
     * @throws SQLException
     */
    private static void classifyPatientStatus(Measurement measure, int num) throws SQLException {
        ArrayList<ArrayList<String>> result = DataBaseClient.getMeasurements(measure.getPid(), num);
    }


    /**
     * Identify which patient this measurement
     * has been performed on.
     * @throws SQLException
     */
    private static void identifyPatient(Measurement measure) throws SQLException {
        measure.setPid(DataBaseClient.getPID(measure.getSensor()));
    }

    /**
     * Send to database-handler for uploading.
     * @throws SQLException
     */
    private static void uploadToDatabase(Measurement measure) throws SQLException {
        String date = measure.getDate() + "";
        String dia = measure.getDia() + "";
        String sys = measure.getSys() + "";
        String pulse = measure.getPulse() + "";
        DataBaseClient.insertMeasurement(
            measure.getPid(), date,
            dia, sys, pulse);
    }
}