import re

def palindromes_between_indices(string):
    letters = re.findall('[a-z]', string.lower())[5:10]

    def arrangements(letters, arrangement=[]):
        if len(letters) == 0:
            return [arrangement]
        else:
            return [arrangement + [letter] + a for letter in letters for a in arrangements(letters[:] - {letter})]
    arranged_letters = arrangements(set(letters))
    palindromes = {''.join(arrangement) for arrangement in arranged_letters if len(arrangement) >= 5 and arrangement == arrangement[::-1]}
    return palindromes