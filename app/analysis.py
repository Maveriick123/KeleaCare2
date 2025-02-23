import numpy as np
import matplotlib.pyplot as plt


labels = 'Happy', 'Angry', 'Surprise','Sad', 'Fear' 

# Initialize an empty array with shape (0,5)
data = np.empty((0, 5), dtype=int)

# Function to add a row
def add_row(array, row):
    return np.vstack([array, np.array(row)])

# Example: Adding rows
#We need to process inputs here
data = add_row(data, [0, 0, 0, 0, 1])
data = add_row(data, [0, 0, 0, 0, 1])
data = add_row(data, [0.33, 0.33, 0.33, 0, 0])
data = add_row(data, [0, 0, 0, 0.5, 0.5])


print(data)

#Mean of the analysis
emotion_mean = np.mean(data, axis=0)

def find_highest_and_second_highest(arr):
    if len(arr) < 2:
        return None  # Not enough elements to find both highest and second highest

    highest_index = second_highest_index = -1
    highest_value = second_highest_value = float('-inf')

    for i, value in enumerate(arr):
        if value > highest_value:
            second_highest_value = highest_value
            second_highest_index = highest_index
            highest_value = value
            highest_index = i
        elif value > second_highest_value and value != highest_value:
            second_highest_value = value
            second_highest_index = i

    return highest_index, second_highest_index

def find_lowest_and_second_lowest(arr):
    if len(arr) < 2:
        return None  # Not enough elements to find both lowest and second lowest

    lowest_index = second_lowest_index = -1
    lowest_value = second_lowest_value = float('inf')

    for i, value in enumerate(arr):
        if value < lowest_value:
            second_lowest_value = lowest_value
            second_lowest_index = lowest_index
            lowest_value = value
            lowest_index = i
        elif value < second_lowest_value and value != lowest_value:
            second_lowest_value = value
            second_lowest_index = i

    return lowest_index, second_lowest_index

def get_main_emotions(emotion_mean):
    first,secondary = find_highest_and_second_highest(emotion_mean)
    if(emotion_mean[first] > 75):
        switcher = {
            0: "ecstatic",
            1: "furious",
            2: "thrilled",
            3: "depressed",
            4: "terrified"
        }    
    else:
        switcher = {
                0: "in a good mood",
                1: "upset",
                2: "surprised",
                3: "feeling a bit off",
                4: "kind of scared"
            }
    main_emotion =switcher.get(first)
    switcher = {
                0: "in a good mood",
                1: "upset",
                2: "surprised",
                3: "feeling sad",
                4: "kind of scared"
            }
    secondary_emotion = switcher.get(secondary)
    return main_emotion,secondary_emotion

def get_big5(emotion_mean):
    biggest_big5,second_highest_big5 = find_highest_and_second_highest(big5_vector)
    lowest_big5,second_lowest_big5 = find_lowest_and_second_lowest(big5_vector)
    switcher = {
                0: "openness",
                1: "conscientiousness",
                2: "extraversion",
                3: "agreeableness",
                4: "neuroticism"
            }
    main_emotion =switcher.get(biggest_big5)
    switcher = {
                0: "openness",
                1: "conscientiousness",
                2: "extraversion",
                3: "agreeableness",
                4: "neuroticism"
            }
    secondary_emotion = switcher.get(second_highest_big5)
    switcher = {
                0: "openness",
                1: "conscientiousness",
                2: "extraversion",
                3: "agreeableness",
                4: "neuroticism"
            }
    main_lowest =switcher.get(lowest_big5)
    switcher = {
                0: "openness",
                1: "conscientiousness",
                2: "extraversion",
                3: "agreeableness",
                4: "neuroticism"
            }
    secondary_lowest = switcher.get(second_lowest_big5)
    return "The user shows " + main_emotion + " and " + secondary_emotion + " however, he also shows a lack of " + main_lowest + " and " + secondary_lowest

def get_recommendation(emotion_mean):
    first,secondary = find_highest_and_second_highest(emotion_mean)
    switcher = {
        0: "I'm glad to hear that!",
        1: "Try to calm down, exercise or relax",
        2: "Woah, what a big surprise!",
        3: "I'm sorry to hear that, try to talk to someone",
        4: "Don't worry, everything will be fine"
    }
    return switcher.get(first)


print(emotion_mean)
main_emotion, secondary_emotion = get_main_emotions(emotion_mean)
print("The user is ",main_emotion, " and ", secondary_emotion)
print(get_recommendation(emotion_mean))

emotion_to_big5 = np.array([
    #O,   C,  E,  A,  N
    [ 1,  1,  1,  1, 1],  # Joy
    [-1,  -1,  1, -1,  -1],  # Anger
    [-1,  1, -1,  -1,  1],  # Sadness
    [ 1,  -1,  1,  0,  -1],  # Surprise
    [-1,  -1, -1, -1,  -1]   # Fear
])


# Convert to Big Five representation
big5_vector = np.dot(emotion_mean, emotion_to_big5)





print("Big Five Encoded Values:", big5_vector)
print(get_big5(big5_vector))

