def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[100:296]
    for i in range(len(substring) - 135):
        for length in range(136, 161):
            substring_slice = substring[i:i + length]
            if substring_slice == substring_slice[::-1]:
                if substring_slice.isalpha():
                    palindromes.add(substring_slice)
    return palindromes