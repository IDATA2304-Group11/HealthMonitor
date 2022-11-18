# Template based on Data from "National Health and Nutrition Examination Survey 2007-2010. JAMA. 2011;305(19):1971-1979"

import random
import numpy as np

# The average fluctuation percentage in BP in adult patients
FLUCTUATION_PERCENTAGE = 0.20

"""
This class represents a Patient with random but realistic gender,age, heart rate and blood pressure fluctuation

@author Edvardsn
@version 18/11/22
"""


class Patient:

    def __init__(self, name, gender, age, fluctuationRange):
        self.gender = gender
        self.age = age
        self.fluctuation = fluctuationRange
    

    name = ""
    gender = int
    age = int
    fluctuationRange = int
  


"""
Generates a psuedorandom elderly person with its respective attributes
"""


def generatePatient():
    gender = random.randrange(0, 2)
    age = random.randrange(60, 90)
    fluctuationRange = round(FLUCTUATION_PERCENTAGE * fetchMeanValue(age, gender))
   

    return Patient(gender, age, fluctuationRange)


"""
Fetches the mean value of a given age and gender of a patient
"""


def fetchMeanValue(age, gender):
    if gender == 0:
        return fetchMeanValuesMan(age)
    else:
        return fetchMeanValuesFemale(age)


"""
Returns the male mean value in blood pressure of a given age
Values are extracted from "National Health and Nutrition Examination Survey 2007-2010. JAMA. 2011;305(19):1971-1979"
"""


def fetchMeanValuesMan(age):
    if age < 64:
        return 105
    elif age < 69:
        return 110
    elif age < 74:
        return 123
    elif age < 79:
        return 138
    else:
        return 145


"""
Returns the female mean value in systolic and diastolic blood pressure of a given age
Values are extracted from "National Health and Nutrition Examination Survey 2007-2010. JAMA. 2011;305(19):1971-1979"
"""


def fetchMeanValuesFemale(age):
    if age < 64:
        return 105
    elif age < 69:
        return 110
    elif age < 74:
        return 115
    else:
        return 120


""" 
Returns the gender of a patient from the binary representation
"""


def getGender(genderValue):
    if genderValue == 0:
        return "Male"
    else:
        return "Female"


"""
Creates a sine wave that can be easily modified
"""
def customizableSineWave(variable, amplitude, frequency, equilibrium):
    return amplitude * np.sin(frequency * variable) + equilibrium


"""
Returns a coefficient sign value where the amplitude is directed towards the middle of the amplitude range provided
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
This method generates an array realistic syntetic blood pressure data along with generated personal information
measured once per second.

Array Format: ["Name, Gender, Age", 231, 213, ....]
"""

def generateBPDataSeconds(seconds):
    patient = generatePatient()

    equilibrium_line = fetchMeanValue(patient.age, patient.gender)
    fluctuationRange = patient.fluctuation
    time_interval = np.arange(1, seconds, 1)
    amplitude = fluctuationRange / 2

   # BPdata = [patient.name + "," + getGender(patient.gender) + "," + str(patient.age)]
    BPdata = []
   
    for t in time_interval:
        frequency = random.uniform(6, 8)

        coefficient = stabilizeAmplitude(amplitude, fluctuationRange)

        amplitude = coefficient * random.randrange(1, fluctuationRange)

        dataValue = customizableSineWave(t, amplitude, frequency, equilibrium_line)

        roundedDataValue = round(dataValue, 2)

        BPdata.append(roundedDataValue)

    return BPdata
