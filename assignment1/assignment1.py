# Task 1: Write a function that prints "Hello!"
def hello():
    return "Hello!"

# Task 2: Write a function that takes a name as an argument and prints "Hello, name!"
def greet(name):
    return f"Hello, {name}!"

# Task 3: Write a calc function that takes three arguments
def calc(a, b, operation="multiply"):
    def _numeric_pair():
        return isinstance(a, (int, float)) and isinstance(b, (int, float))

    if operation == "add":
        if not _numeric_pair():
            return f"You can't {operation} those values!"
        return a + b
    elif operation == "subtract":
        if not _numeric_pair():
            return f"You can't {operation} those values!"
        return a - b
    elif operation == "multiply":
        if not _numeric_pair():
            return f"You can't {operation} those values!"
        return a * b
    elif operation == "divide":
        if b == 0:
            return "You can't divide by 0!"
        if not _numeric_pair():
            return f"You can't {operation} those values!"
        return a / b
    elif operation == "modulo":
        if not _numeric_pair():
            return f"You can't {operation} those values!"
        return a % b
    else:
        return f"You can't {operation} those values!"

# Task 4: Write a function that converts a string to a float
def data_type_conversion(value, data_type):
    if data_type == "float":
        try:
            return float(value)
        except (ValueError, TypeError):
            return f"You can't convert {value} into a {data_type}."
    elif data_type == "int":
        try:
            return int(value)
        except (ValueError, TypeError):
            return f"You can't convert {value} into a {data_type}."
    elif data_type == "str":
        return str(value)
    elif data_type == "bool":
        return bool(value)
    else:
        return f"You can't convert {value} into a {data_type}."

# Task 5: Create a grade function.
def grade(*args):
    if not args:
        return "Invalid data was provided."
    for x in args:
        if not isinstance(x, (int, float)):
            return "Invalid data was provided."
    mean = sum(args) / len(args)
    if mean >= 90:
        return "A"
    elif mean >= 80:
        return "B"
    elif mean >= 70:
        return "C"
    elif mean >= 60:
        return "D"
    else:
        return "F"

# Task 6: Use a For Loop with a range.
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

# Task 7: Student scores, using kwargs.
def student_scores(mode, **kwargs):
    if mode == "best":
        best_name = None
        best_score = None
        for key, value in kwargs.items():
            if best_score is None or value > best_score:
                best_name = key
                best_score = value
        return best_name

    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)
        
    else:
        return "Invalid data was provided."

# Task 8: Titleize, with String and List Operations.
def titleize(string):
    small = {"and","or","the",
             "a","an","but",
             "in","on","at",
             "to","for","of",
             "as","by",
    }
    words = string.split()
    if not words:
        return ""
    out = []
    for i, word in enumerate(words):
        lower = word.lower()
        if i == 0 or i == len(words) - 1:
            out.append(word.capitalize())
        elif lower in small:
            out.append(lower)
        else:
            out.append(word.capitalize())
    return " ".join(out)

# Task 9: Hangman, with more String Operations.
def hangman(secret, guess):
    return "".join(c if c in guess else "_" for c in secret)

# Task 10: Pig Latin
def _pig_latin_word(word):
    vowels = "aeiouAEIOU"

    def is_vowel_at(j):
        return j < len(word) and word[j] in vowels

    if is_vowel_at(0):
        return word + "ay"

    i = 0
    n = len(word)
    while i < n and not is_vowel_at(i):
        if word[i].lower() == "q" and i + 1 < n and word[i + 1].lower() == "u":
            i += 2
        else:
            i += 1
    return word[i:] + word[:i] + "ay"


def pig_latin(string):
    return " ".join(_pig_latin_word(w) for w in string.split())
