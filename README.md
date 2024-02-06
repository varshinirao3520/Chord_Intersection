# Chord_Intersection
This is a python project designed to count the number of chord intersections in a circle. The project takes input from the user in the form of parallel lists containing the radian measures of the chords and returns the number of chord intersections for the given set of chords in the circle. 

#Installation
Run the python file named "Chord_Intersection.py" using any Python IDE. I have used Visual Studio Code for the same. 
Python Version: 3.11.5 -- https://www.python.org/downloads/
Install the following python packages: 
matplotlib -- pip install matplotlib
numpy -- pip install numpy

#Input 
User must enter the input in the given format:
Ex:[(0.78,1.47,1.77,2.92),("s1","s2","e1","e2")]
where the first list contains the radian measures of the chords and the second list contains the identifiers

#Code Description:
The code takes input from the user and parses through the lists to extract the chords. 
The draw_circle_chords function draws a circle for a pictorial representation of the chords in the circle and shows the intersection graphically using Matplotlib.
The count_intersection function counts the number of intersections in the circle and returns an integer value.

#Big-O Runtime
The time complexity of this function is O(n log n), where n is the number of chords. This is because the function first creates a list of events, which takes O(n) time. Then, it sorts the events list, which takes O(n log n) time. Finally, it iterates through the sorted events list, which takes O(n) time. Therefore, the overall time complexity is O(n log n).

The space complexity of this function is O(n), where n is the number of chords. This is because the function creates a list of events, which has a length of 2n. Therefore, the overall space complexity is O(n).
