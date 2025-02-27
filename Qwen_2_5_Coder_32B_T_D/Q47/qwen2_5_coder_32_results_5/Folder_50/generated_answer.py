import string

def palindromes_of_specific_lengths(s):
    s = s[36:93].lower()
    s = ''.join(filter(lambda x: x in string.ascii_lowercase, s))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 10, min(i + 36, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes