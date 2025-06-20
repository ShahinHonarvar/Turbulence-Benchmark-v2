from Q34.Phi_3_results_4.Folder_15.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(2):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(2):
        l.append({i})
    assert find_original_set(*l) == set(range(2))


def test_similar_sets():
    l = []
    for i in range(2):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 2*2, 2):
        l.append(set(range(i, i + 2)))
    assert find_original_set(*l) == set(range(2*2))


def test_several_subsets():
    l = []
    for i in range(2):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(2))
