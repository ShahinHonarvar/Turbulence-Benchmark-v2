def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[21:63]
    for i in range(len(substring) - 22):
        for j in range(22, 34):
            if i + j - 1 >= len(substring):
                break
            substring_window = substring[i:i + j]
            if substring_window.lower() == substring_window[::-1].lower():
                palindromes.add(substring_window)
    return palindromes