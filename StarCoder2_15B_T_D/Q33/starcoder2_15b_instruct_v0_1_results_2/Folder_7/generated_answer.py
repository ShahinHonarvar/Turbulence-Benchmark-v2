import re

def return_vowels(string):
    pattern = '[aieou]{202,872}[3-]>[aieou]'
    matches = re.findall(pattern, string)
    return matches