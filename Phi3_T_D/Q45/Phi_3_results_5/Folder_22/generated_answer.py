def palindromes_between_indices(input_string):
    selected_letters = input_string[5:7].lower()
    unique_letters = sorted(set(selected_letters))
    palindromes = set()

    def generate_palindromes(prefix, remaining_letters):
        if len(prefix) >= 3:
            palindromes.add(prefix)
        for i, letter in enumerate(remaining_letters):
            generate_palindromes(prefix + letter + prefix[::-1][1:i + 1], remaining_letters[i + 1:])
    generate_palindromes('', unique_letters)
    return palindromes