import tkinter as tk  # Import Tkinter library for creating the GUI
import time  # Import time library to get the current time
import math  # Import math library for trigonometric functions

# Function to update the clock every second
def update_clock():
    now = time.localtime()  # Get the current local time
    hours = now.tm_hour % 12  # Get the hour (convert to 12-hour format)
    minutes = now.tm_min  # Get the minutes
    seconds = now.tm_sec  # Get the seconds

    # Calculate the angle for each clock hand
    hr_angle = (hours + minutes / 60) * 30  # Angle for the hour hand
    min_angle = minutes * 6  # Angle for the minute hand
    sec_angle = seconds * 6  # Angle for the second hand

    # Calculate the end coordinates of each clock hand
    hr_x = clock_center + hand_length_hr * math.sin(math.radians(hr_angle))
    hr_y = clock_center - hand_length_hr * math.cos(math.radians(hr_angle))

    min_x = clock_center + hand_length_min * math.sin(math.radians(min_angle))
    min_y = clock_center - hand_length_min * math.cos(math.radians(min_angle))

    sec_x = clock_center + hand_length_sec * math.sin(math.radians(sec_angle))
    sec_y = clock_center - hand_length_sec * math.cos(math.radians(sec_angle))

    # Update the position of each clock hand on the canvas
    canvas.coords(hr_hand, clock_center, clock_center, hr_x, hr_y)
    canvas.coords(min_hand, clock_center, clock_center, min_x, min_y)
    canvas.coords(sec_hand, clock_center, clock_center, sec_x, sec_y)

    # Call this function again after 1000 milliseconds (1 second)
    window.after(1000, update_clock)

# Create the main window for the application
window = tk.Tk()
window.title("Analog Clock")  # Set the window title

# Create a drawing area (canvas) for the clock
clock_radius = 150  # Radius of the clock face
clock_center = clock_radius + 10  # Center of the clock (used for positioning)
canvas = tk.Canvas(window, width=2*clock_center, height=2*clock_center, bg="#222222")
canvas.pack()  # Add the canvas to the window

# Draw the clock face
canvas.create_oval(10, 10, 2*clock_radius+10, 2*clock_radius+10, outline="#595959", width=3)
# Draw the numbers on the clock face
for i in range(1, 13):
    angle = i * 30  # Angle for each number (1 to 12)
    x = clock_center + clock_radius * 0.85 * math.sin(math.radians(angle))
    y = clock_center - clock_radius * 0.85 * math.cos(math.radians(angle))
    canvas.create_text(x, y, text=str(i), fill="white", font=("Arial", 18))

# Lengths of the clock hands
hand_length_hr = clock_radius * 0.5  # Length of the hour hand
hand_length_min = clock_radius * 0.7  # Length of the minute hand
hand_length_sec = clock_radius * 0.85  # Length of the second hand

# Draw the clock hands
hr_hand = canvas.create_line(clock_center, clock_center, clock_center, clock_center-hand_length_hr, fill="#f20000", width=6)
min_hand = canvas.create_line(clock_center, clock_center, clock_center, clock_center-hand_length_min, fill="#2aa6ff", width=4)
sec_hand = canvas.create_line(clock_center, clock_center, clock_center, clock_center-hand_length_sec, fill="#ffffff", width=2)

# Start the clock update function
update_clock()

# Run the Tkinter event loop (keeps the window open)
window.mainloop()
