import string

def palindromes_of_specific_lengths(s):
    result = set()
    letters = set(string.ascii_lowercase)
    s = s[100:201].lower()
    for i in range(len(s) - 4):
        for j in range(i + 5, min(i + 11, len(s)) + 1):
            substring = s[i:j]
            if set(substring).issubset(letters) and substring == substring[::-1]:
                result.add(substring)
    return result