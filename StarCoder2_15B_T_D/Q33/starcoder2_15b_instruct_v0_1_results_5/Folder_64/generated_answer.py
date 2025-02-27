def return_vowels(string):
    """
    Returns a list of vowels from a given string between index 1 (inclusive) and index 7 (exclusive) that are greater than 'F' and smaller than or equal to 'j'. If no such characters exist, returns an empty list.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, c in enumerate(string):
        if i >= 1 and i < 7 and (c.lower() in vowels) and (c.lower() > 'f') and (c.lower() <= 'j'):
            result.append(c)
    return result