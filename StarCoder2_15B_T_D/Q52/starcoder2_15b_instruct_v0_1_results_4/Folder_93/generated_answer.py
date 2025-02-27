import re

def palindrome_of_length_n(text):
    substrings = re.findall('.{45}', text, flags=re.IGNORECASE)
    palindromes = set()
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes