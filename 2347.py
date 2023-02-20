def bestHand(ranks, suits):
    #   """
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
