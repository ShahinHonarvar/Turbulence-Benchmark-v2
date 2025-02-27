from collections import Counter

def palindromes_between_indices(s):
    substring = s[0:8]
    char_count = Counter(substring)
    for char in char_count.copy():
        if not char.isalpha():
            del char_count[char]
    palindromes = set()
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(26):
                    for m in range(26):
                        candidate = chr(97 + i) + chr(97 + j) + chr(97 + k) + chr(97 + l) + chr(97 + m) + chr(97 + l) + chr(97 + k)
                        temp_count = Counter(candidate)
                        if all((temp_count[char] <= char_count[char] for char in temp_count)):
                            palindromes.add(candidate)
                            palindromes.add(candidate.upper())
    return palindromes