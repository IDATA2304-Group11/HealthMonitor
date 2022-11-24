package no.ntnu.idata2304.group11.app;

import java.time.LocalDateTime;

/**
     * Represents a proxy for a received
     * measurement. Makes it easier to
     * handle its components.
     */
public class Measurement {

    private String sensor;
    private int sys;
    private int dia;
    private int pulse;
    private LocalDateTime date;
    private String pid;


    public Measurement(String date, String sys,
                String dia, String pulse,
                String sensor) {
        
        this.sensor = sensor;
        this.sys = Integer.parseInt(sys);
        this.dia = Integer.parseInt(dia);
        this.pulse = Integer.parseInt(pulse);
        this.date = LocalDateTime.parse(date);
    }

    public String getSensor() {
        return this.sensor;
    }

    public int getSys() {
        return this.sys;
    }

    public int getDia() {
        return this.dia;
    }

    public int getPulse() {
        return this.pulse;
    }

    public LocalDateTime getDate() {
        return this.date;
    }

    public String getPid() {
        return this.pid;
    }

    public void setPid(String pid) {
        if (!pid.isBlank()) this.pid = pid;
    }
}