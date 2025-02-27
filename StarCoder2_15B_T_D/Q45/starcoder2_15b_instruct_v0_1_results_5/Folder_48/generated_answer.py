def palindromes_between_indices(string):
    palindromes = set()
    temp_string = ''
    for i, char in enumerate(string):
        if char.isalpha():
            temp_string += char.lower()
            if len(temp_string) >= 4 and i >= 6 and (i <= 8):
                palindromes.add(temp_string + temp_string[::-1])
    return palindromes