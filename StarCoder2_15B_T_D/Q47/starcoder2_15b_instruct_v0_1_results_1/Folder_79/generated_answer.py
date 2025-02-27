def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[1:9]
    for i in range(len(substring) - 3):
        for j in range(i + 3, i + 5):
            window = substring[i:j]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes