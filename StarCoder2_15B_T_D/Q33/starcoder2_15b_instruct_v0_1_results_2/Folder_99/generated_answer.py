import re

def return_vowels(string):
    pattern = '[+:<]'
    matches = re.findall(pattern, string[323:526])
    return matches