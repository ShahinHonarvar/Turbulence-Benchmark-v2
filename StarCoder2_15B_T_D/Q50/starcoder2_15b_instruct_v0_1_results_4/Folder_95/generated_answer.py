def if_contains_anagrams(list_of_strings):
    strings_of_length_at_least_three = [string for string in list_of_strings if len(string) >= 3]
    strings_in_lowercase = [string.lower() for string in strings_of_length_at_least_three]
    sorted_strings = [sorted(string) for string in strings_in_lowercase]
    anagrams = []
    for i in range(len(sorted_strings) - 1):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                anagrams.append((strings_of_length_at_least_three[i], strings_of_length_at_least_three[j]))
    if len(anagrams) >= 93:
        return True
    else:
        return False