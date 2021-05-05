def longestRun(lst):
    #This tkes care of the first element of the list
    streak_lst = [lst[0]]
    longest_run_lst = streak_lst
    count = 0

    # process through the list from 2nd element to the end
    for i in range(1, len(lst) ):
        if lst[i] == lst[i-1]:
            streak_lst.append(lst[i])
        else:
            # When the current and the last do not match
            # check if current one is longer than longest
            if len(streak_lst) > len(longest_run_lst):
                longest_run_lst = streak_lst
            # Reassign streak_lst to the new element to start counting anew
            streak_lst = [lst[i]]
        print(f"the current longest run is {streak_lst}")
        print(f"the overall longest run is {longest_run_lst}")
        print("--------")

    #I need to deal with the case when the last element IS part of the longest streak
    #This only matters where the list is bigger than one value
    #if lst[-1] == lst[-2] then the last value is part of a streak
    if (len(lst) > 1 ) and (lst[-1] == lst[-2]):
        # We only want to replace longest is this last one is really the longest
        if len(streak_lst) > len(longest_run_lst):
            longest_run_lst = streak_lst
    return longest_run_lst


# Main starts here
if __name__ == '__main__':
    list_01 = [5]
    list_02 = [1, 1, 1, 2]
    list_03 = [1, 1, 1, 2, 3, 2, 2, 3, 3, 3, 3, 2, 2, 2]
    list_04 = [1, 1, 1, 2, 3, 2, 2, 3, 3, 3, 3]
    list_05 = [1, 1, 1, 2, 3, 2, 2, 3, 3, 3, 3, 5]

    result_lst = longestRun(list_03)
    print(f'The return list is {result_lst}')