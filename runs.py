def longestRun(lst):
    # Write your code here

    #longest_run_lst = []
    streak_lst = [lst[0]]
    longest_run_lst = streak_lst
    count = 0

    for i in range(1, len(lst) - 1 ):
        if lst[i] == lst[i-1]:
            count += 1
            streak_lst.append(lst[i])

            #longest_run_lst = streak_lst
            #print(longest_run_lst)
        else:

            #check if current one is longer than longest
            if len(streak_lst) > len(longest_run_lst):
                longest_run_lst = streak_lst

            streak_lst = [lst[i]]
        print(f"the current longest run is {streak_lst}")
        print(f"the overall longest run is {longest_run_lst}")
        print(f"the current location in lst is {count}")
        print("--------")
    ##

    ##i need to deal with the case when the last element is part of the longest streak
    #make sure we dont process this is only one element in the list
    if 1 < len(lst):
        if lst[-1] == lst[-2]:

            longest_run_lst = streak_lst
        if longest_run_lst


    #lst.count(lst[i])
    #if lst.count(lst[i]) > lst.count[i-1]:


    return longest_run_lst
# Main starts here
if __name__ == '__main__':
    list_01 = [5]
    list_02 = [1, 1, 1, 2]
    list_03 = [1, 1, 1, 2, 3, 2, 2, 3, 3, 3, 3, 2, 2]
    list_04 = [1, 1, 1, 2, 3, 2, 2, 3, 3, 3, 3]
    list_05 = [1, 1, 1, 2, 3, 2, 2, 3, 3, 3, 3, 5]

    result_lst = longestRun(list_05)
    print(f'The return list is {result_lst}')