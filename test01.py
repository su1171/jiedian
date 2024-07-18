# 测试排序算法

lst = [23,12,74,13,6,16,86,82,17,39,44,22,85,372,4,22,73,253]

def Bubble_Sort(lst):
    # 冒泡排序    
    for j in range(len(lst)):
        for i in range(len(lst)-j-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]   # 交换
    return lst


def Selection_Sort(lst):
    # 选择排序
    for j in range(len(lst)-1):
        min_num = j
        for i in range(j,len(lst)):
            if lst[i] < lst[min_num]:
                min_num = i
        # 交换
        lst[j],lst[min_num] = lst[min_num],lst[j]
    return lst


def Insertion_Sort(lst):
    # 插入排序
    
    return lst


if __name__ == "__main__":

    res = Selection_Sort(lst)
    print(res)