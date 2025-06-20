from Q9.Phi_3_results_3.Folder_18.generated_answer import all_odd_ints_inclusive


def test_odd_range():
    for n in range(-11,12,2):
        n_list = [n * n for _ in range(0, (49 + 1) * 10)]
        assert all_odd_ints_inclusive(n_list) == n_list[35:49 + 1]


def test_even_range():
    even_list = [i for i in range(-10000,10002,2)]
    assert all_odd_ints_inclusive(even_list) == []


def test_all_zero_range():
    zero_list = [0 for _ in range(0,49 * 5)]
    assert all_odd_ints_inclusive(zero_list) == []


def test_all_one_range():
    initial_list = [1 for _ in range(1, 49 + 10)]
    assert all_odd_ints_inclusive(initial_list) == initial_list[35:49 + 1]


def test_range_size():
    initial_list = [i for i in range(-1000, (49 + 1) * 3)]
    assert len(all_odd_ints_inclusive(initial_list)) < len(initial_list)


def test_range_sum_positive_odds():
    initial_list = [i for i in range(1, 49 + 10)]
    assert sum(all_odd_ints_inclusive(initial_list)) >= 0


def test_range_sum_negative_odds():
    initial_list = [i for i in range(-1, -49 - 10, -1)]
    assert sum(all_odd_ints_inclusive(initial_list)) <= 0


def test_each_num_is_odd():
    initial_list = [i for i in range(-100, 49 + 50)]
    result_list  = all_odd_ints_inclusive(initial_list)
    for i in result_list:
        assert i % 2


def test_all_negative_ones():
    initial_list = [-1 for _ in range(1, 49 + 10)]
    assert all_odd_ints_inclusive(initial_list) == initial_list[35:49 + 1]