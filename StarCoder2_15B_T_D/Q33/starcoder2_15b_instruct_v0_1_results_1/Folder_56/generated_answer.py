def return_vowels(s):
    """
    Returns the list of all vowel English letters between index 15 (inclusive) and index 86 (exclusive)
    that are greater than character @ and smaller than or equal to character ~. If no such characters
    exist in the specified range, an empty list is returned.
    """
    vowels = 'aeiou'
    return [c for i, c in enumerate(s) if 15 <= i < 86 and c in vowels and ('@' < c <= '~')]