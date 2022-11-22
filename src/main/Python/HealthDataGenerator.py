# Template based on Data from "National Health and Nutrition Examination Survey 2007-2010. JAMA. 2011;305(19):1971-1979"

import random
import numpy as np
from datetime import datetime

# The average fluctuation percentage in BP in adult patients
FLUCTUATION_PERCENTAGE = 0.20

"""
This class represents a Patient with random but realistic gender,age, heart rate and blood pressure fluctuation

@version 21/11/22
"""
class Patient:

    def __init__(self, gender, age, Systolicfluctuation, Diastolicfluctuation):
        self.gender = gender
        self.age = age
        self.Systolicfluctuation = Systolicfluctuation
        self.Diastolicfluctuation = Diastolicfluctuation
    
    gender = int
    age = int
    Systolicfluctuation = int
    Diastolicfluctuation = int
    heartratefluctuation = int

  
"""
Generates a psuedorandom elderly person with its respective attributes
"""
def generatePatient():
    gender = random.randrange(0, 2)
    age = random.randrange(60, 90)
    
    range = (FLUCTUATION_PERCENTAGE * fetchMeanValue(age, gender)[0])
    SystolicfluctuationRange = round(range)
    DiastolicfluctuationRange = round((FLUCTUATION_PERCENTAGE * fetchMeanValue(age, gender)[1]))
    
    return Patient(gender, age, SystolicfluctuationRange, DiastolicfluctuationRange)


"""
Fetches the mean value of a given age and gender of a patient
"""
def fetchMeanValue(age, gender):
    if gender == 0:
        return fetchMeanValuesMan(age)
    else:
        return fetchMeanValuesFemale(age)


"""
Returns the male mean value in systolic and diastolic blood pressure of a given age
Values are extracted from "National Health and Nutrition Examination Survey 2007-2010. JAMA. 2011;305(19):1971-1979"
"""
def fetchMeanValuesFemale(age):
    if age < 64:
        return 130,80 
    elif age < 69:
        return 135,85
    elif age < 74:
        return 140,90
    else:
        return 145,95


"""
Returns the female mean value in systolic and diastolic blood pressure of a given age
Values are extracted from "National Health and Nutrition Examination Survey 2007-2010. JAMA. 2011;305(19):1971-1979"
"""
def fetchMeanValuesMan(age):
    if age < 64:
        return 130,80
    elif age < 69:
        return 140,90
    elif age < 74:
        return 155,95
    elif age < 79:
        return 170,105
    else:
        return 180,115


"""
Creates a sine wave that can be easily modified

@version 21/11/22
"""
def customizableSineWave(variable, amplitude, frequency, equilibrium):
    return amplitude * np.sin(frequency * variable) + equilibrium


"""
Returns a coefficient sign value where the amplitude is directed towards the middle of the amplitude range provided

@version 26/10/22
"""
def stabilizeAmplitude(amplitude, amplitudeRange):
    coefficientSign = 1

    if amplitude > amplitudeRange / 2:  # Amplitude is in upper quadrant of fluctuation range
        coefficientSignValue = random.randrange(0, 3)

        if coefficientSignValue > 0:
            coefficientSign = -1
        else:
            coefficientSign = 1;

    if amplitude < -1 * (amplitudeRange / 2):  # Amplitude is in lower quadrant of fluctuation range
        coefficientSignValue = random.randrange(0, 3)

        if coefficientSignValue > 0:
            coefficientSign = 1
        else:
            coefficientSign = -1

    return coefficientSign


"""
This method generates an array of Syntetic systolic blood pressure data

@version 21/11/22
"""
def generateSystolicData(seconds, patient):

    equilibrium_line = fetchMeanValue(patient.age, patient.gender)[0]
    fluctuationRange = patient.SystolicfluctuationRange
    time_interval = np.arange(1, seconds, 1)
    amplitude = fluctuationRange / 2

    Sysdata = []
   
    for t in time_interval:
        frequency = random.uniform(6, 8)

        coefficient = stabilizeAmplitude(amplitude, fluctuationRange)

        amplitude = coefficient * random.randrange(1, fluctuationRange)

        dataValue = customizableSineWave(t, amplitude, frequency, equilibrium_line)

        roundedDataValue = round(dataValue, 2)

        Sysdata.append(roundedDataValue)

    return Sysdata

"""
This method generates an array of Syntetic systolic blood pressure data

@version 21/11/22
"""
def generateDiastolicData(seconds, patient):

    equilibrium_line = fetchMeanValue(patient.age, patient.gender)[1]
    fluctuationRange = patient.DiastolicfluctuationRange
    time_interval = np.arange(1, seconds, 1)
    amplitude = fluctuationRange / 2

    Diadata = []
   
    for t in time_interval:
        frequency = random.uniform(6, 8)

        coefficient = stabilizeAmplitude(amplitude, fluctuationRange)

        amplitude = coefficient * random.randrange(1, fluctuationRange)

        dataValue = customizableSineWave(t, amplitude, frequency, equilibrium_line)

        roundedDataValue = round(dataValue, 2)

        Diadata.append(roundedDataValue)

    return Diadata


""" 
Simulates a given timeframe 

@version 22/11/22
"""
def generateTimeframeData(seconds):
    
    currentTime = datetime.now()
    
    currentSecond = currentTime.now().second
    
    currentMinute = currentTime.minute
    
    counter = 1
    
    Timedata = [str(currentTime)]
    
    while counter <= seconds:
            
        newSecond = (currentSecond + counter) % 60
        
        newTime = str(currentTime.replace(second= newSecond, minute= currentMinute))
        
        Timedata.append(newTime)
        
        if newSecond == 59:
            currentMinute += 1
            
            
        counter += 1
        
    return Timedata    
    
"""
Generates sensor data for pre-defined registered sensor users in a given timeframe

"""
def generateRegisteredSensorData(seconds):
    
    # A list which consists of all the registered sensor serial numbers 
    REGISTERED_SENSOR_SERIALNUMBERS = ["ABCD-EFGH-AC78","ABCD-EFGH-AC79","ABCD-EFGH-AC80","ABCD-EFGH-AC81","ABCD-EFGH-AC82"]

    # A dictonary of all current patients
    REGISTERED_PATIENTS =  {"ABCD-EFGH-AC78": Patient(0,72,155,)
                                    ,"ABCD-EFGH-AC79": Patient(1,83,7,5) 
                                    ,"ABCD-EFGH-AC80": Patient(1,66,15,10)
                                    ,"ABCD-EFGH-AC81": Patient(0,88,6,2)
                                    ,"ABCD-EFGH-AC82": Patient(0,71,4,6)}
    
    TotalPatientData = []
        
    for sensor in REGISTERED_SENSOR_SERIALNUMBERS:
        tmpPatientData = []
        
        tmpPatientData.append(generateTimeframeData(seconds))
        
        tmpPatientData.append(generateSystolicData(seconds, REGISTERED_PATIENTS[sensor]))
        
        tmpPatientData.append(generateDiastolicData(seconds, REGISTERED_PATIENTS[sensor]))
        
        tmpPatientData.append(sensor)
        
        TotalPatientData.append(tmpPatientData)
        
    
    return TotalPatientData
        

    


