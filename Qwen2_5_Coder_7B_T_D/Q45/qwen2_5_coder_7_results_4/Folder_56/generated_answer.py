def palindromes_between_indices(s):
    letters = s[5:10]
    letters = letters.lower()
    unique_letters = set(letters)
    letters = ''.join(sorted(unique_letters))
    max_length = len(letters)
    palindromes = set()
    for i in range(4, max_length):
        for j in range(max_length - i + 1):
            substring = letters[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes