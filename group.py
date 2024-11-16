

# Task 1
def groups_of_3(groups: list[int])->list[list[int]]:
    groups_o3 = []
    index = 0
    if len(groups)%3 == 0:
        total_lists = len(groups)//3
    else:
        total_lists = len(groups)//3 + 1

    for elements in range(0, total_lists):
        sublist = []
        for x in range(3):
            sublist.append(groups[index])
            index += 1
            if index == len(groups):
                break
        groups_o3.append(sublist)

    return groups_o3

