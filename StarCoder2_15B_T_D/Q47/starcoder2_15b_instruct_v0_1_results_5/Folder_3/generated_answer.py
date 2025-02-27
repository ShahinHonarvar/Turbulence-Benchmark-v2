from prompt_toolkit import prompt

def palindromes_of_specific_lengths(text: str) -> set:
    """
    Returns the set of all palindromes of specific lengths in a given string.
    """
    result = prompt(text)
    return result