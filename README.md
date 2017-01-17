Crypt Tools
=====

This is a _little_ collection of encryption and decryption tools

Crypt Tools currently includes Caesar Cipher and Vigenère Cipher
More to come.

====

`caesar.py`
====

`caesar.py` is a simple tool to rotate the characters of a string or text
caesar cipher is also known as rotate cipher.

`caesar.py` includes tkinter to provide a simple interface for choosing file input and output.

=====

`vigenere.py`
====

`vigenere.py` is a more advanced tool than caesar.py.
Vigenère Cipher is using caesar cipher with rotation based on keyword.

Only CLI so no GUI is available at the moment.
CLI intructions: 
  - `python vigenere.py -t <"TEXT"|PATHNAME> -k <KEY>`
  - Don't forget the `""` if you have a text longer than 1 word!
  - add `-a` to the end to analyze the frequency of characters

====

REMINDER: None of those Ciphers is very secure as I provide de- AND encode, 
don't use it for really important mails or similar!

====
TODO:
 - GUI for Vigenère
 - Recode Caesar on Vigenère for mor flexibility
 - more to come...
