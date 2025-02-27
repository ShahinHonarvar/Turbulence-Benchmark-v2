def if_contains_anagrams(input_list):
    """
    Write a function called 'if_contains_anagrams' that takes one argument, a list of strings.
    The function should return true if there are at least 9 pairs of anagrams in the given list;
    otherwise, it should return false. The function should only consider the anagrams of the length
    of at least three. The function should compare the strings in a case-insensitive manner.
    """
    anagrams = {}
    for s in input_list:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
    return len(anagrams) >= 9