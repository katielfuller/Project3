def removeNegatives(lst):
    """
    parameters : lst of type list
    returns : another list with the same elements minus the negative numbers
    """

    # When list becomes empty just return an empty list
    if lst == []:
        print(f'The list was seen empty')
        return []

    #elif not required due to the returns (which act similiarly to break here)
    if lst[0] < 0:
        print(f"i found a negative number {lst[0]}")
        # In this case we simply want to continue processing the rest of the list
        return removeNegatives(lst[1:])

    # Again no "else" required ehre due to the ealier retturn which will prevent execution of these later
    # steps when thos conditions are true
    print(f'I found the positive number : {lst[0]}')
    # In this case we want to put the positive value BACK on the list that is return
    # But ONLY after the rest of the list has been processed (by recursion of this methd)
    return [lst[0]] + removeNegatives(lst[1:])

# Main starts here
if __name__ == '__main__':
    list_01 = []
    list_02 = [-6]
    list_03 = [1]
    list_04 = [-6, 1, -9, 5, -8]
    list_05 = [-6, 1, -9, 5, -8, 4]

    result_lst = removeNegatives(list_05)
    print(f'The return list is {result_lst}')