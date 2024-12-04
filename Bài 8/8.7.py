print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
# Import the modules
import tkinter
import random

# List of possible colours
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
# The game time left, initially 30 seconds
timeleft = 30

# Function that will start the game
def startGame(event):
    global score
    global timeleft
    if timeleft == 30:
        # Start the countdown timer
        countdown()
    # Run the function to choose the next colour
    nextColour()

# Function to choose and display the next colour
def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        # Make the text entry box active
        e.focus_set()
        # Check if the colour typed is equal to the colour of the text
        if e.get().lower() == colours[1].lower():
            score += 1
            # Clear the text entry box
            e.delete(0, tkinter.END)
            # Shuffle the colours list
            random.shuffle(colours)
            # Change the colour to type, by changing the text and the colour
            label.config(fg=colours[1], text=colours[0])
            # Update the score
            scoreLabel.config(text="Score: " + str(score))

# Countdown timer function
def countdown():
    global timeleft
    if timeleft > 0:
        # Decrement the timer
        timeleft -= 1
        # Update the time left label
        timeLabel.config(text="Time left: " + str(timeleft))
        # Run the function again after 1 second
        timeLabel.after(1000, countdown)

# Driver code
# Create a GUI window
root = tkinter.Tk()
# Set the title
root.title("COLORGAME")
# Set the size
root.geometry("375x200")

# Add an instructions label
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()

# Add a score label
scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

# Add a time left label
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

# Add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# Add a text entry box for typing in colours
e = tkinter.Entry(root)
e.pack()

# Run the 'startGame' function when the enter key is pressed
root.bind('<Return>', startGame)

# Set focus on the entry box
e.focus_set()

# Start the GUI
root.mainloop()
