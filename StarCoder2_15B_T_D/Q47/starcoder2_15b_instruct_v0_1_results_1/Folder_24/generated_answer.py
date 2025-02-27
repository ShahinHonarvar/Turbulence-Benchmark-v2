def palindromes_of_specific_lengths(string):
    """
    Find palindromes of specific lengths in a given string.
    
    Args:
        string (str): The input string.
        
    Returns:
        set: A set of palindromes that satisfy the specified requirements.
    """
    string = string.lower()
    substring = string[12:93]
    palindromes = set()
    for i in range(len(substring) - 42):
        for length in range(42, 78):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes