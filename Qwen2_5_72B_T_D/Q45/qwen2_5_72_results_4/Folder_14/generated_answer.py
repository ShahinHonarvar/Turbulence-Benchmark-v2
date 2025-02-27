def palindromes_between_indices(s):
    substring = s[4:6].lower()
    letters = set(substring)
    palindromes = set()
    if len(letters) == 1:
        for length in range(3, 7, 2):
            palindrome = substring[0] * length
            palindromes.add(palindrome)
    return palindromes