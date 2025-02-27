from collections import defaultdict

def if_contains_anagrams(string_list):

    def are_anagrams(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    strings_by_length = defaultdict(list)
    for s in string_list:
        if len(s) >= 3:
            strings_by_length[len(s)].append(s)
    for length, strings in strings_by_length.items():
        for i in range(len(strings)):
            for j in range(i + 1, len(strings)):
                if are_anagrams(strings[i], strings[j]):
                    anagram_count += 1
                    if anagram_count > 91:
                        return False
    return True