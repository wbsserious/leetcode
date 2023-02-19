def putMarbles(weights, k):
    """
    你有 k 个背包。给你一个下标从 0 开始的整数数组 weights ，其中 weights[i] 是第 i 个珠子的重量。同时给你整数 k 。
    请你按照如下规则将所有的珠子放进 k 个背包。
    没有背包是空的。
    如果第 i 个珠子和第 j 个珠子在同一个背包里，那么下标在 i 到 j 之间的所有珠子都必须在这同一个背包中。
    如果一个背包有下标从 i 到 j 的所有珠子，那么这个背包的价格是 weights[i] + weights[j] 。
    一个珠子分配方案的 分数 是所有 k 个背包的价格之和。
    请你返回所有分配方案中，最大分数 与 最小分数 的 差值 为多少。
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
    if len(weights)==1:
        return 0
    list1=[weights[x]+weights[x+1] for x in range(len(weights)-1)]
    list1.sort()
    return sum(list1[(len(list1)-k+1):])-sum(list1[:k-1])

cesicesi=[1,3,5,1]
k=2
print(putMarbles(cesicesi,k))