# 测试排序算法

lst = [23,12,74,13,6,16,86,82,17,39,44,22,85,372,4,22,73,253]

def Bubble_Sort(lst):
    # 冒泡排序    
    for j in range(len(lst)):
        for i in range(len(lst)-j-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]   # 交换
    return lst



if __name__ == "__main__":
    res = Bubble_Sort(lst)
    print(res)