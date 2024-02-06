from matplotlib import pyplot as plt
import numpy as np

#To draw a circle
def draw_circle_chords(chords):
    fig, ax = plt.subplots()
    circle_t = np.linspace(0, 2*np.pi, 100)
    circle_x = np.cos(circle_t)
    circle_y = np.sin(circle_t)
    ax.plot(circle_x, circle_y, '-k')

    for i, c_angles in enumerate(chords):
        c_x = np.cos(c_angles)
        c_y = np.sin(c_angles)
        ax.plot(c_x, c_y, '-b')
        ax.text(c_x[0]*1.05, c_y[0]*1.05, f"s{i}")
        ax.text(c_x[1]*1.05, c_y[1]*1.05, f"e{i}")

    ax.set_aspect('equal')
    return fig, ax

#To count the number of intersections
def count_intersections(chords):
    chords_count = len(chords)
    events = []

    for i in range(chords_count):
        events.append((chords[i][0], 'start', i))
        events.append((chords[i][1], 'end', i))

    events.sort()
    num_intersections = 0
    active_chords = set()

    for _, event_type, chord_index in events:
        if event_type == 'start':
            num_intersections += len(active_chords)
            active_chords.add(chord_index)
        else:
            active_chords.remove(chord_index)

    return num_intersections

#To parse through the input list and extract the chords
def parse_chords(input_str):
    try:
        input_str = input_str.replace(' ', '')
        if not (input_str.startswith("[(") and input_str.endswith(")]")):
            raise ValueError("Input must start with '[(' and end with ')]'")
        
        tuples_str = input_str[2:-2].split("),(")
        if len(tuples_str) != 2:
            raise ValueError("Input must contain exactly two tuples.")

        first_tuple_str = tuples_str[0]
        first_tuple = tuple(float(item) for item in first_tuple_str.split(","))

        second_tuple_str = tuples_str[1].strip("\"'")
        
        second_tuple = tuple(item.strip("\"'") for item in second_tuple_str.split('","'))

        return first_tuple, second_tuple
    except ValueError as e:
        print(f"Error: {e}")
        return None, None

#To extract the radian measures and identifiers
def input_chords_modified(chords):

    rad_measure, ids = parse_chords(chords)

    angles = []
    
    for i in range(0, int(len(rad_measure)/2)):
        elem = []
        elem.append(rad_measure[i])
        elem.append(rad_measure[i+int(len(rad_measure)/2)])
        angles.append(elem)

    return angles

# Format to be followed: [(0.78, 1.47, 1.77,2.92), ("s1", "s2", "e1", "e2")]
input_prompt = "Enter the list of chords in the given format : "
input_str = input(input_prompt)
chords = input_chords_modified(input_str)
print("The chords are:",chords)

# Draw the circle 
draw_circle_chords(chords)

# Find Intersections
print("Number of Chord Intersections:", count_intersections(chords))
plt.show()
