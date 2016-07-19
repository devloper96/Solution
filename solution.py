import sys

digits = {
    "i": 1,
    "v": 5,
    "x": 10,
    "l": 50,
    "c": 100,
    "d": 500,
    "m": 1000
}

num = {}
goods = {}


def msg(s):
    """Return-and-print frontend"""
    print s


def parse(word):
    """Parse a Galactic/Roman number"""

    n = 0
    try:
        dig = [num[i] for i in word]
    except:
        return -1

    while dig:
        d = dig.pop(0)
        if dig and dig[0] > d:
            n -= d
        else:
            n += d

    return n


def process(line):
    """Read a sentence."""

    word = line.lower().split(None)

    if not word:
        return

    if len(word) == 3 and word[1] == "is":
        key = word[0]
        val = word[2]

        if val not in digits:
            return msg("'%s' is not a valid digit." % val)
        num[key] = digits[val]
        return

    if len(word) > 4 and word[-1] == "credits" and word[-3] == "is":
        word.pop()
        try:
            val = float(word[-1])
        except:
            return msg("'%s' is not a valid numeric value" % word[-1])

        word.pop()
        word.pop()
        g = word.pop()
        n = parse(word)

        if n < 0:
            return msg("That's not a valid Galactic number")

        goods[g] = val / n
        return

    if word[0:3] == ["how", "much", "is"]:
        word = word[3:]
        if word[-1] == "?":
            word.pop()

        n = parse(word)
        if n < 0:
            return msg("'%s' is not a valid Galactic number" % " ".join(word))

        print " ".join(word), "is", n
        return

    if word[0:4] == ["how", "many", "credits", "is"]:
        word = word[4:]
        if word[-1] == "?":
            word.pop()

        g = word.pop()
        if g not in goods:
            return msg("I don't know of the trading good %s" % g)

        n = parse(word)
        if n < 0:
            return msg("'%s' is not a valid Galactic number" % " ".join(word))

        print " ".join(word), g.title(), "is", int(n * goods[g]), "Credits"
        return

    return msg("I've no idea what you are talking about")


for line in sys.stdin:
    process(line)
