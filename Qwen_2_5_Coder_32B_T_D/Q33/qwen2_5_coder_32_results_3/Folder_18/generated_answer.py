def return_vowels(s):
    return [v for v in 'AEIOUaeiou' if 528 <= s.find(v) < 606 and 'M' < v <= 'X']