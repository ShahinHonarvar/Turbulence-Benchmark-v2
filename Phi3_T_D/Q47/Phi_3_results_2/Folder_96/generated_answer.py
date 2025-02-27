def palindromes_of_specific_lengths(text):
    start, end = (100, 300)
    char_set = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    potential_palindromes = set()
    for length in range(50, 101):
        for i in range(start, end - length + 1):
            substring = text[i:i + length]
            if all((c in char_set for c in substring)):
                if substring.lower() == substring[::-1].lower():
                    potential_palindromes.add(substring.lower())
    return potential_palindromes