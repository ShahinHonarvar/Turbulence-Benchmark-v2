import re

def palindromes_of_specific_lengths(string):
    substring = string[11:94]
    regex = re.compile('[a-zA-Z]')
    substring = regex.sub('', substring)
    result = set()
    for length in range(34, 55):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result