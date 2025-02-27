def palindromes_of_specific_lengths(input_string):
    considered_range = input_string[75:96]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for length in range(7, 10):
        for i in range(len(considered_range) - length + 1):
            substring = considered_range[i:i + length]
            if set(substring.lower()) <= english_letters and substring.lower() == substring[::-1].lower():
                palindromes.add(substring.lower())
    return palindromes