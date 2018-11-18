def findGreatestOverlap(spans):
    """
    my solution:
    returns a discrete moment of one-dimensional space where
    the most spans overlap


    >>> findGreatestOverlap([(0,2), (1, 2), (1,3)])
    1
    >>> findGreatestOverlap([(6, 7), (7, 9), (10, 11), (10, 12), (8, 10),\
        (9, 11), (6, 8)])
    10
    """

    d = {}

    for span_start, span_end in spans:
        for i in range(span_start, span_end):
            d[i] = d.setdefault(i, 0) + 1
    
    # d.get means find the largest value and return its key
    return max(d, key=d.get)


def findGreatestOverlapOpt(spans):
    """
    optimal solution:
    returns a discrete moment of one-dimensional space where
    the most spans overlap

    start times increment, end times decrement

    >>> findGreatestOverlapOpt([(0,2), (1, 2), (1,3)])
    1
    >>> findGreatestOverlapOpt([(6, 7), (7, 9), (10, 11), (10, 12), (8, 10),\
        (9, 11), (6, 8)])
    10
    """

    # sort spans by start times
    new_spans = []
    [new_spans.extend([(span_start, 1), (span_end, -1)])
        for span_start, span_end in spans]

    sorted_spans = sorted(new_spans, key=lambda x: x[0])

    max_moment = max_overlaps = current_overlaps = 0
    for moment, status in sorted_spans:
        current_overlaps += status
        if current_overlaps > max_overlaps:
            max_overlaps = current_overlaps
            max_moment = moment
    
    return max_moment


if __name__ == "__main__":
    import doctest
    doctest.testmod()