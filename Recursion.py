
import methods

# Main starts here
if __name__ == '__main__':
    list_01 = []
    list_02 = [-6]
    list_03 = [1]
    list_04 = [-6, 1, -9, 5, -8]
    list_05 = [-6, 1, -9, 5, -8, 4]

    result_lst = methods.removeNegatives(list_05)
    helpers = methods.Removers()
    print(f'The return list is {result_lst}')
    result_lst = helpers.removeNegatives(list_04)
    print(f'The return list is {result_lst}')