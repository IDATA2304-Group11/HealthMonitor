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

# The average standard deviation of adults
STANDARD_DEVIATION = 13

"""
This class represents a person with a given gender,age, incident_probability and blood pressure fluctuation
"""


class Patient:

    def __init__(self, gender, age, incident_probability, fluctuation):
        self.gender = gender
        self.age = age
        self.incident_probability = incident_probability
        self.fluctuation = fluctuation

    gender = int
    age = int
    incident_probability = float
    fluctuation = float


# Generates a psuedorandom elderly person
#
def generatePerson():
    gender = random.randrange(0, 1)
    age = random.randrange(60, 80)
    incident_probability = random.uniform(0.0, 0.001);
    fluctuation = random.uniform(0, 0.09)

    return Patient(gender, age, incident_probability, fluctuation)


def fetchMeanValue(age, gender):
    if gender == 0:
        return fetchMeanValuesMan(age)
    else:
        return fetchMeanValuesFemale(age)


# Returns the male mean value in systolic and diastolic blood pressure of a given age
def fetchMeanValuesMan(age):
    if age < 64:
        return 130, 80
    elif age < 69:
        return 135, 85
    elif age < 74:
        return 150, 95
    elif age < 79:
        return 170, 105
    else:
        return 180, 110


# Returns the female mean value in systolic and diastolic blood pressure of a given age
def fetchMeanValuesFemale(age):
    if age < 64:
        return 130, 80
    elif age < 69:
        return 135, 85
    elif age < 74:
        return 140, 90
    else:
        return 145, 95




def customizableSineWave(amplitude, phase, equilibrium):



# Generates bloodPressure for a given time interval
def generateBPDataMinutes(time):
    person = generatePerson()

    equilibrium_line = fetchMeanValue(person.age, person.gender)[0]

    frequency = person.fluctuation

    time_interval = np.linspace(1, 600, 100)

    interval = np.arange(0, 600, 1)

    amplitude = STANDARD_DEVIATION / equilibrium_line

    half_phase = np.pi / frequency # takes the last entry as the next wave's equilibrium



    plt.plot(time_interval, 13 * np.sin(time_interval) + equilibrium_line)


    plt.xlabel("Time")
    plt.ylabel("SDB")
    plt.show()


generateBPDataMinutes(20)
