import string

def palindromes_of_specific_lengths(s):
    letters = set(string.ascii_lowercase)
    s = s[1:300].lower()
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 2, min(i + 11, len(s) + 1)):
            sub = s[i:j]
            if all((c in letters for c in sub)) and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes