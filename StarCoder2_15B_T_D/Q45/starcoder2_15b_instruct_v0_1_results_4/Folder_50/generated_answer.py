def palindromes_between_indices(string):
    palindromes = set()
    letters = [char for char in string if char.isalpha()]
    for i in range(len(letters) - 4):
        for j in range(i + 4, len(letters) + 1):
            substring = ''.join(letters[i:j])
            if len(substring) >= 5 and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes