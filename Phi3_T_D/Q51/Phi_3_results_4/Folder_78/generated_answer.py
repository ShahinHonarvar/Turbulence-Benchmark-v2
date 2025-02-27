def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    seen_anagrams = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                sorted_pair = tuple(sorted([strings[i].lower(), strings[j].lower()]))
                if sorted_pair not in seen_anagrams:
                    seen_anagrams.add(sorted_pair)
                    count += 1
    return count <= 70