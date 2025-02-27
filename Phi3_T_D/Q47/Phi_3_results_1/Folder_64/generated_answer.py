from string import ascii_letters

def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(min(7, len(s))):
        for length in range(4, 6):
            if i + length > len(s):
                break
            substring = s[i:i + length]
            if all((c in ascii_letters for c in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes