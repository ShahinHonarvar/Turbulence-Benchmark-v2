def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[100:301]
    for i in range(len(substring) - 50):
        for j in range(50, 101):
            if i + j - 1 >= len(substring):
                break
            substring_slice = substring[i:i + j]
            if substring_slice.lower() == substring_slice[::-1].lower():
                palindromes.add(substring_slice)
    return palindromes