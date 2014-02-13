from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
import string


LOWER_LETTERS = string.ascii_lowercase
UPPER_LETTERS = string.ascii_uppercase


def rot(s, n):
    result = ""
    for char in s:
        if char.isupper():
            result += encrypt(char, UPPER_LETTERS, n)
        elif char.islower():
            result += encrypt(char, LOWER_LETTERS, n)
        else:
            result += char
    return result


def encrypt(char, alpha, num):
    result = ''
    letter = alpha.index(char)
    index = letter + num
    result += alpha[index % len(alpha)]
    return result


fileChooser = askopenfilename()
inputFile = open(fileChooser, "r")
fileChooser2 = askopenfilename()
outputFile = open(fileChooser2, "w")

string = inputFile.read()
number = int(input("Number of Rotates: "))
outputFile.write(rot(string, number))
saveText = "Your rotated String is saved to "
showinfo("Info", saveText+fileChooser2)