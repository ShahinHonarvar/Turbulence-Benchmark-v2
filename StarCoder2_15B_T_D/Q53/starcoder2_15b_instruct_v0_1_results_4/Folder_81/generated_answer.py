import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = '(.)(?P<content>.{33,})?\\1'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    for match in matches:
        content = match[1]
        if content and content.isalpha():
            palindromes.add(content)
    return palindromes