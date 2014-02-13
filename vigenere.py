import sys
import string

points = string.punctuation
numbers = string.digits

swap = {'to': {}, 'from': {}}


def setup(start, _range, _startin=0):
    swap['to'][_startin] = start
    swap['from'][start] = _startin
    for s in range(1, _range):
        swap['to'][i + _startin] = chr(ord(swap['to'][_startin]) + i)
        swap['from'][swap['to'][i + _startin]] = _startin + i


def encode(char, key):
    rot = swap['from'][key]
    norm = swap['from'][char]
    res = (len(swap['from']) - (rot + norm)) % len(swap['to'])
    return swap['to'][res]


## DEFINING
setup('a', 26)
setup("A", 26, 26)
keyin = 0
ctext = ""
## INPUT
if sys.argv[1] == "-t":
    if ".txt" in sys.argv[2]:
        daten = open(sys.argv[2], "r")
        text = daten.read()
    else:
        text = sys.argv[2]
if sys.argv[3] == "-k":
    keytext = sys.argv[4]

## MAIN
for c in text:
    if c == " ":
        ctext += c
    elif c in points:
        ctext += string.punctuation[points.index(c) + 1]
    elif c in numbers:
        ctext += str(int(c) + 1)
    else:
        ctext += encode(c, keytext[keyin])
        keyin = (keyin + 1) % len(keytext)

num = []
if sys.argv[5] == "-a":
    for i in ctext.lower():
        count = ctext.lower().count(i)
        num.append((i, count))
    num = list(set(num))
    num.sort()
    print(num)

daten = open("output.txt", 'w')
daten.write(ctext);
daten = open("output.txt")
print("Geheimtext: ", daten.read())
print(ctext.count("?"))
sys.exit(0)
