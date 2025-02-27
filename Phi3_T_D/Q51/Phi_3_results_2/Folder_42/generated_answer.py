def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower()) and len(set(str1.lower()) & set(str2.lower())) >= 3

    def count_anagrams(string, remaining):
        count = 0
        anagrams = set()
        for other in remaining:
            if is_anagram(string, other):
                count += 1
                if count >= 38:
                    return True
                anagrams.add(other)
        return count
    if len(strings) < 2:
        return False
    strings.sort(key=len)
    for i, string in enumerate(strings):
        if count_anagrams(string, strings[i + 1:]):
            return True
    return False