def all_substring_of_size_n(my_str):
    """
    <Write a function called 'all_substring_of_size_n' that takes one argument which is a string. The function should return the list of all distinct substrings of the length equal to 42 with no duplicate characters. If no such substrings exist in the given string, the function should return an empty list. The order of the substrings in the returned list does not matter.>
    """
    n = 42
    result = []
    for i in range(len(my_str) - n + 1):
        substring = my_str[i:i + n]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result