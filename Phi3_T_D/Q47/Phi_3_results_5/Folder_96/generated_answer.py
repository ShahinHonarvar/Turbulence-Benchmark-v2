def is_english_letter(c):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

def find_palindromes(s, length):
    palindromes = set()
    for i in range(length - 1, len(s)):
        for j in range(i - length + 1, -1, -1):
            substring = s[j:i + 1]
            if substring == substring[::-1] and all((is_english_letter(c) for c in substring)):
                palindromes.add(substring.lower())
                break
    return palindromes

def palindromes_of_specific_lengths(s):
    a100 = 100
    a300 = 300
    a101 = 101
    a99 = 99
    return set.union(*(find_palindromes(s[a100:a300], i) for i in range(a101, a99 + 1)))