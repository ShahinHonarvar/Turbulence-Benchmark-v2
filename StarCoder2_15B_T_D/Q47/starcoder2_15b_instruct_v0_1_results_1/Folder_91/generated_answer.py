from index 0 to 10 of the given string `s`, ignoring case.

def palindromes_of_specific_lengths(s):
    """
    Finds the set of all palindromes of lengths between 3 and 5 in the substring
    """
    palindromes = set()
    substring = s[0:11]
    for i in range(len(substring) - 2):
        for j in range(i + 3, min(i + 6, len(substring))):
            substring_slice = substring[i:j]
            if substring_slice.lower() == substring_slice[::-1].lower():
                palindromes.add(substring_slice)
    return palindromes