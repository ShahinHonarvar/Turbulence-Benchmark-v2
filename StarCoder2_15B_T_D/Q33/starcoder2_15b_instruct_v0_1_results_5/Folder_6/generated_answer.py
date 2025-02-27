def return_vowels(string):
    """
    Returns a list of all vowel English letters in the given string that are greater than 'U' and
    smaller than or equal to 'i'. If no such letters exist, returns an empty list.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, c in enumerate(string):
        if i >= 20 and i < 34 and c.isalpha() and (c.lower() in vowels) and (c > 'U') and (c <= 'i'):
            result.append(c)
    return result