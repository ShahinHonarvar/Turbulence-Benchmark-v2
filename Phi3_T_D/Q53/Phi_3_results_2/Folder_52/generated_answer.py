from re import finditer

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for match in finditer('(?i)(.{14,})', s):
        substr = match.group(1)
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes