def palindromes_between_indices(s):
    substring = s[2:5]
    substring = substring.lower()
    english_letters = ''.join(sorted(set(substring)))
    palindromes = set()

    def generate_arrangements(chars, length):
        if length == 0:
            yield ''
        else:
            for char in chars:
                for rest in generate_arrangements(chars, length - 1):
                    yield (char + rest)
    for length in range(3, len(substring) + 1):
        for arrangement in generate_arrangements(english_letters, length):
            if arrangement == arrangement[::-1] and all((char in substring for char in arrangement)):
                palindromes.add(arrangement)
    return palindromes