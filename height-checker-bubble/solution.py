def heightChecker(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    # make a copy of 'heights' called 'sorted_heights'
    sorted_heights = heights[:]

    # bubble sort 'sorted_heights'
    difference = True
    while difference:
        difference = False
        j = 1
        for i in range(0, len(sorted_heights) - 1):
            if sorted_heights[j] < sorted_heights[i]:
                sorted_heights[j], sorted_heights[i] = (
                    sorted_heights[i],
                    sorted_heights[j],
                )
                difference = True
            j += 1

    # decare a variable "discrepancy" as 0
    discrepancy = 0

    # compare 'heights' and 'sorted_heights' and increment disrepancy if any difference occurs at each index
    for i in range(0, len(heights)):
        if heights[i] != sorted_heights[i]:
            discrepancy += 1

    return discrepancy
