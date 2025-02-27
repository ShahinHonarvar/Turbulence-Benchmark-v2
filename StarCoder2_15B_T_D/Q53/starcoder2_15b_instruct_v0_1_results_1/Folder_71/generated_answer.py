import re
from collections import Counter

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for m in re.finditer('(?=(\\w{87,}))', s):
        palindrome = m.group(1)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes