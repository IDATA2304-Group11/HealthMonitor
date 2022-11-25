package no.ntnu.idata2304.group11.json;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class JsonParserTest {
    
    @Test
    public void testParser_male_43() {
        int[] val = JsonHandler.getParameters("male", 43);

        assertEquals(125, val[0]);
        assertEquals(83, val[1]);
        assertEquals(57, val[2]);
        assertEquals(82, val[3]);
    }


    @Test
    public void testParser_female_62() {
        int[] val = JsonHandler.getParameters("female", 62);

        assertEquals(130, val[0]);
        assertEquals(86, val[1]);
        assertEquals(60, val[2]);
        assertEquals(83, val[3]);
    }
}
