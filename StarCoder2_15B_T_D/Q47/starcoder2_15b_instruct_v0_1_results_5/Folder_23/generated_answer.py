def palindromes_of_specific_lengths(string):
    sub_string = string[23:95]
    palindromes = set()
    for length in range(17, 56):
        for i in range(len(sub_string) - length + 1):
            window = sub_string[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes