import generator
import PySimpleGUI as sg

# Add some color
# to the window
sg.theme("SandyBeach")

# Very basic window.
# Return values using
# automatic-numbered keys
layout = [
    [sg.Text("Please enter your Sex, Weight, Height, Age")],
    [sg.Radio("kg/cm", "RADIO1", default=True), sg.Radio("lbs/in", "RADIO1")],
    [sg.Radio("Male", "RADIO2", default=True), sg.Radio("Female", "RADIO2")],
    [sg.Text("Weight", size=(15, 1)), sg.InputText()],
    [sg.Text("Height", size=(15, 1)), sg.InputText()],
    [sg.Text("Age", size=(15, 1)), sg.InputText()],
    [sg.Text("Exclude", size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()],
]

window = sg.Window("Simple data entry window", layout)
event, values = window.read()
window.close()

# The input data looks like a simple list
# when automatic numbered
if values[2]:
    sex = "male"
else:
    sex = "female"

weight = int(values[4])
height = int(values[5])
age = int(values[6])
avoid = [values[7]]

if not values[0]:
    weight *= 0.453592
    height *= 2.54

print(generator.generate(sex, weight, height, age, avoid))
