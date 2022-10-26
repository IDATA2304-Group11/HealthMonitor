# Generates a Patient

# Boolean with a 1/5 chance of an event happening where increased blood pressure over 2 minutes at a random
# time during the day

# BP with a mean value and variance of standard deviation of 13

# When an event occurs the BP spikes and uses a temporary mean value 20-30 higher than normal for the next
# 120 iterations

# Template based on Data from "National Health and Nutrition Examination Survey 2007-2010. JAMA. 2011;305(19):1971-1979"

# chance of having a increase during a positive phase

import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from faker import Faker

"""
This class represents a Patient with random but realistic gender,age, heart rate and blood pressure fluctuation
"""

# Fake Norwegian name generator
fake = Faker("no_NO")
# The average standard deviation of Blood pressure in adults
STANDARD_DEVIATION_BP = 13
# The average fluctuation percentage in BP in adult patients
FLUCTUATION_PERCENTAGE = 0.20


class Patient:

    def __init__(self, name, gender, age, fluctuationRange):
        self.name = name
        self.gender = gender
        self.age = age
        self.fluctuation = fluctuationRange

    name = ""
    gender = int
    age = int
    fluctuationRange = int


# Generates a psuedorandom elderly person with its respective attributes
def generatePatient():
    name = fake.name_male()
    gender = random.randrange(0, 2)
    age = random.randrange(60, 90)
    fluctuationRange = round(FLUCTUATION_PERCENTAGE * fetchMeanValue(age, gender))

    return Patient(name, gender, age, fluctuationRange)


# Fetches the mean value of a given age and gender of a patient
def fetchMeanValue(age, gender):
    if gender == 0:
        return fetchMeanValuesMan(age)
    else:
        return fetchMeanValuesFemale(age)


# Returns the male mean value in blood pressure of a given age
# Values are extracted from "National Health and Nutrition Examination Survey 2007-2010. JAMA. 2011;305(19):1971-1979"
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


# Returns the female mean value in systolic and diastolic blood pressure of a given age
# Values are extracted from "National Health and Nutrition Examination Survey 2007-2010. JAMA. 2011;305(19):1971-1979"
def fetchMeanValuesFemale(age):
    if age < 64:
        return 105
    elif age < 69:
        return 110
    elif age < 74:
        return 115
    else:
        return 120


# Returns a random integer in the range 0 - 1, a bit.
def getRandomBit():
    return random.randrange(0, 1)


def getGender(genderValue):
    if genderValue == 0:
        return "Male"
    else:
        return "Female"


# Converts a given dataframe into a csv file
def convert_dataframe_to_csv(df, fileName):
    csvFile = df.to_csv(fileName, sep=";", index=False)
    filePath = "/Python/Data/" + fileName
    path = os.path.join(filePath, fileName)


# Creates a sine value with given parameters
def customizableSineWave(variable, amplitude, frequency, equilibrium):
    return amplitude * np.sin(frequency * variable) + equilibrium


# Returns a coefficient sign value where the amplitude is directed towards the middle of the amplitude rannge
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


# Generates bloodPressure for a given time interval
def generateBPDataSeconds(seconds):
    patient = generatePatient()

    equilibrium_line = fetchMeanValue(patient.age, patient.gender)
    fluctuationRange = patient.fluctuation
    time_interval = np.arange(1, seconds, 1)
    amplitude = fluctuationRange / 2

    BPdata = [patient.name + "," + getGender(patient.gender) + "," + str(patient.age)]

    for t in time_interval:
        frequency = random.uniform(6, 8)

        coefficient = stabilizeAmplitude(amplitude, fluctuationRange)

        amplitude = coefficient * random.randrange(3, fluctuationRange)

        dataValue = customizableSineWave(t, amplitude, frequency, equilibrium_line)

        roundedDataValue = round(dataValue, 2)

        BPdata.append([roundedDataValue])

    df = pd.DataFrame(BPdata)

    fileName = patient.name + ".csv"

    convert_dataframe_to_csv(df, fileName)

    print(BPdata)
    plt.plot(time_interval, BPdata[1:])
    plt.show()

    return BPdata


generateBPDataSeconds(60)
