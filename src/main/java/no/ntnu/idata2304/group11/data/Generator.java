package no.ntnu.idata2304.group11.data;

import java.util.Random;

public class Generator implements HealthDataGenerator {

    // Mean of systolic blood pressure in elderly
    public static final double EXPECTED_VALUE = 150;

    // Mean of diastolic blood pressure in adults
    public static final double EXPECTED_VALUE_DIASTOLIC_PRESSURE = 75;

    // The average standard deviation in diastolic blood pressure for adults
    public static final double STANDARD_DEVIATION_DIASTOLIC_PRESSURE = 7.24;

    // The average standard deviation in systolic blood pressure for adults
    public static final double STANDARD_DEVIATION_SYSTOLIC_PRESSURE = 19.6;

    public static final Random randomGenerator = new Random();

    /**
     * Generates a dataset which represents data gathered for each hour in a day
     */
    @Override
    public void generateDailyDataSet() {

    }

    /**
     * Generates a dataset which represents data gathered for each day in a month
     */
    @Override
    public void generateMonthlyDataSet() {

    }

    /**
     * Generates a dataset which represents data gathered for each month of the year
     */
    @Override
    public void generateYearlyDataSet() {

    }
}
