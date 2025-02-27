import re

def palindrome_of_length_at_least_n(string):
    processed_string = re.sub('\\W+', '', string.lower())
    palindromes = set()
    for i in range(len(processed_string) - 21):
        substring = processed_string[i:i + 22]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes