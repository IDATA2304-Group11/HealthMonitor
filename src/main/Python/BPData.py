# generate Person, gender and age as parameters , uses gender chart as template

# Boolean with a 1/5 chance of an event happening where increased blood pressure over 2 minutes at a random
# time during the day

# BP with a mean value and variance of standard deviation of 13

# When an event occurs the BP spikes and uses a temporary mean value 20-30 higher than normal for the next
# 120 iterations

# Template based on data from "National Health and Nutrition Examination Survey 2007-2010. JAMA. 2011;305(19):1971-1979"

# chance of having a increase during a positive phase

import random
import numpy as np
import matplotlib.pyplot as plt

"""
This class represents a person with a given gender,age, incident_probability and blood pressure fluctuation
"""

# The average standard deviation of adults
STANDARD_DEVIATION = 13
# The average fluctuation percentage in BP in adult patients
FLUCTUATION_PERCENTAGE = 0.20


class Patient:

    def __init__(self, gender, age, incident_probability, fluctuationRange):
        self.gender = gender
        self.age = age
        self.incident_probability = incident_probability
        self.fluctuation = fluctuationRange

    gender = int
    age = int
    incident_probability = float
    fluctuationRange = int


# Generates a psuedorandom elderly person with its respective attributes
def generatePatient():
    gender = random.randrange(0, 2)
    age = random.randrange(60, 80)
    incident_probability = random.uniform(0.005, 0.01)
    fluctuationRange = round(FLUCTUATION_PERCENTAGE * fetchMeanValue(age, gender))

    return Patient(gender, age, incident_probability, fluctuationRange)


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


# Creates a sine value with given parameters
def customizableSineWave(variable, amplitude, frequency, equilibrium):
    return amplitude * np.sin(frequency * variable) + equilibrium


# Returns a random integer in the range 0 - 1, a bit.
def getRandomBit():
    return random.randrange(0, 1)


# Returns a coefficient sign value where the probability for growth towards the equilibrium line is favored
def stabilizeAmplitude(amplitude, amplitudeRange):
    coefficientSign = 1

    if amplitude > amplitudeRange / 2:  # Amplitude is in upper quadrant of fluctuation range
        coefficientSignValue = random.randrange(0, 3)

        if coefficientSignValue > 0:
            coefficientSign = -1
        else:
            coefficientSign = 1;

    if amplitude < -1 * (amplitudeRange / 2):
        coefficientSignValue = random.randrange(0, 3)

        if coefficientSignValue > 0:
            coefficientSign = 1
        else:
            coefficientSign = -1

    return coefficientSign


# Generates bloodPressure for a given time interval
def generateBPDataSeconds(seconds):
    person = generatePatient()

    equilibrium_line = fetchMeanValue(person.age, person.gender)
    fluctuationRange = person.fluctuation
    time_interval = np.arange(1, seconds, 1)
    amplitude = fluctuationRange / 2
    # frequency = random.randrange(60, 100)

    BPdata = []

    for t in time_interval:

        coefficient = stabilizeAmplitude(amplitude, fluctuationRange)

        amplitude = coefficient * random.randrange(0, fluctuationRange)

        dataValue = customizableSineWave(t, amplitude, 1, equilibrium_line)

        BPdata.append(dataValue)

    # Normal heart rate 60 - 100, so 60 to 100 phases in 60 iterations,  freq bigger than x so more than 60 phases a min
    # Vary in amplitude to generate realistic data, + and - in the range of SD

    plt.plot(time_interval, BPdata)
    plt.show()
    print(person.age)
    if person.gender == 0:
        print("Male")
    else:
        print("Female")


    return BPdata, person.gender, person.age;

generateBPDataSeconds(50)
