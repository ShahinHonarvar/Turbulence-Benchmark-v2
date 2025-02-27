def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(4, min(len(letters), 9)):
        for j in range(len(letters) - i + 1):
            substring = letters[j:j + i]
            reversed_substring = substring[::-1]
            if substring.lower() == reversed_substring.lower():
                palindromes.add(substring)
    return palindromes