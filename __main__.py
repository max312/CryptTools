__author__ = 'Max Philipp Wriedt';

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *


LOWER_LETTERS = [chr(x) for x in range(97, 123)];
UPPER_LETTERS = [chr(x) for x in range(65, 91)];
#SUBS = ["j","k","l","p","q","r","t","u","v","w","x","y","z","s","i","m","o","n","a","b","c","d","e","f","g","h"];

def rot(s, n):
    result = "";
    for char in s:
        if char.isupper():
            result += encrypt(char, UPPER_LETTERS, n);
        elif char.islower():
            result += encrypt(char, LOWER_LETTERS, n);
        else:
            result += char;
    return result;


def encrypt(char, alpha, num):
    result = '';
    letter = alpha.index(char);
    index = letter + num;
    result += alpha[index % len(alpha)]
    return result;


## Executes
# Set Files to import and export
fileChooser = askopenfilename();
inputFile = open(fileChooser, "r");
fileChooser2 = askopenfilename();
outputFile = open(fileChooser2, "w");

string = inputFile.read();
num = int(input("Number of Rotates: "));
outputFile.write(rot(string, num))
saveFile = "Your rotated String is saved to "
showinfo("Info", saveFile+fileChooser2)
