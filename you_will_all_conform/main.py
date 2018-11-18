"""
This function takes a list of two different types,
and outputs the fewest intervals that when changed would produce
a list of only one type.

>>> conformList(['a', 'b', 'a'])
1 through 1 must be changed

>>> conformList(['a', 'a', 'b', 'a', 'a', 'b', 'b', 'b', 'a'])
2 through 2 must be changed
5 through 7 must be changed
"""


def conformList(the_list, type1='a', type2='b'):
    start = 0
    type_count_tracker = 0
    intervals = []

    the_list.append(type1 if the_list[-1] == type2 else type2)

    for i, the_type in enumerate(the_list):
        if the_type != the_list[i - 1]:
            intervals.append((start, i - 1, the_list[start]))

            if the_list[start] == type1:
                type_count_tracker += 1
            else:
                type_count_tracker -= 1

            start = i

    type_to_change = type1 if type_count_tracker < 0 else type2

    intervals_to_change = []
    for start, end, type_of_interval in intervals:
        if type_of_interval == type_to_change:
            intervals_to_change.append(
                "{} through {} must be changed".format(start, end)
                )

    print('\n'.join(intervals_to_change))


if __name__ == "__main__":
    import doctest
    doctest.testmod()