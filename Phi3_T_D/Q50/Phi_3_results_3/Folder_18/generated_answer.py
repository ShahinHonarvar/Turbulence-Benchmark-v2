def if_contains_anagrams(strings):

    def can_form_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    sorted_strings = sorted([s for s in strings if len(s) >= 3], key=lambda s: s.lower())
    anagrams_count = 0
    seen = set()
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] in seen and can_form_anagram(sorted_strings[i], sorted_strings[j]):
                anagrams_count += 1
                if anagrams_count >= 106:
                    return True
                break
        seen.add(sorted_strings[i])
    return False