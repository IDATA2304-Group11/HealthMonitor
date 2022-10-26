package no.ntnu.idata2304.group11.data;

/**
 * This interface contains all available types of datasets to be generated
 *
 * @version 16/10/22
 * @author Edvardsn
 */
public interface HealthDataGenerator {

    /**
     * Generates a dataset which represents data gathered for each hour in a day
     */
    public void generateDailyDataSet();

    /**
     * Generates a dataset which represents data gathered for each day in a month
     */
    public void generateMonthlyDataSet();

    /**
     * Generates a dataset which represents data gathered for each month of the year
     */
    public void generateYearlyDataSet();
}
