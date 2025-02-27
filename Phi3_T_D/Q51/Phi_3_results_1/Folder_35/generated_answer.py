def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())
    count_anagrams = 0
    seen = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3:
                if (strings[i], strings[j]) not in seen:
                    seen.add((strings[i], strings[j]))
                    if count_anagrams // 2 > 210:
                        return False
                    count_anagrams += 1
    return count_anagrams // 2 <= 210