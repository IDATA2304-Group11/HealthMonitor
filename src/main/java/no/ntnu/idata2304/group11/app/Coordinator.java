package no.ntnu.idata2304.group11.app;

/**
 * Processes data received from the analyzer.<p>
 * 
 * Classifyes the staus of a patient by comparing 
 * health-parameters and measurements done by sensors.
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
    public void receive(String measurement) {
        // Todo: Implement code.
    }

    /**
     * Determine what the health-status of
     * the patient is.
     */
    private void classifyPatientStatus() {
        // Todo: Implement code.
    }

    /**
     * Convert data types of the measurements
     * received to the appropriate type.
     */
    private void convertDataTypes() {
        // Todo: Implement code.
    }

    /**
     * Identify which patient this measurement
     * has been performed on.
     */
    private void identifyPatient() {
        // Todo: Implement code.
    }

    /**
     * Send to database-handler for uploading.
     */
    private void uploadToDatabase() {
        // Todo: Implement code.
    }
}
