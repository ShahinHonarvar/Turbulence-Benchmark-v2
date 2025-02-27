def palindromes_between_indices(string):
    letters = [c for c in string[4:8].lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 4, len(letters) + 1):
            palindromes.add(''.join(letters[i:j]))
    return {p for p in palindromes if len(p) >= 5 and p == p[::-1]}