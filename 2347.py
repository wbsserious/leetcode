def bestHand(ranks, suits):
#     #   ""给你一个整数数组 ranks 和一个字符数组 suit 。你有 5 张扑克牌，第 i 张牌大小为 ranks[i] ，花色为 suits[i] 。

# 下述是从好到坏你可能持有的 手牌类型 ：

# "Flush"：同花，五张相同花色的扑克牌。
# "Three of a Kind"：三条，有 3 张大小相同的扑克牌。
# "Pair"：对子，两张大小一样的扑克牌。
# "High Card"：高牌，五张大小互不相同的扑克牌。
# 请你返回一个字符串，表示给定的 5 张牌中，你能组成的 最好手牌类型 。"
    #     :type ranks: List[int]
    #     :type suits: List[str]
    #     :rtype: str
    #     """
    #     # 判断花色
    if len(set(suits))==1:
        return "Flush"
    ranks1=set(ranks)
    if len(ranks1)==4:
        return "Pair"
    if len(ranks1)==3:
        ranks.sort()
        for i in range(len(ranks)-2):
            if ranks[i]==ranks[i+1]==ranks[i+2]:
                return "Three of a Kind"
        return "Pair"
    elif len(ranks1)==2:
        return "Three of a Kind"
    else:
        return "High Card"
    



# ranks = [13,2,3,1,9]
# suits = ["a","a","a","a","a"]
# ranks = [4,4,2,4,4]
# suits = ["d","a","a","b","c"]
# ranks = [10,10,2,12,9]
# suits = ["a","b","c","a","d"]
ranks = [2,1,1,2,7]
suits = ["a","d","d","d","c"]
print (bestHand(ranks,suits))
