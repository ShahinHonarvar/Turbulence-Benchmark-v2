def palindromes_between_indices(s):
    s = s[:5].lower()
    unique_letters = set(s)
    palindromes = set()

    def generate_palindromes(path, remaining):
        if len(path) == 3:
            if path == path[::-1]:
                palindromes.add(path)
            return
        for letter in set(remaining):
            generate_palindromes(path + letter, remaining - {letter})
    for _ in range(3):
        generate_palindromes('', unique_letters)
    return palindromes