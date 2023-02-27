def maximumRemovals(s: str, p: str, removable: int) -> int:
    Letter_dic=[]
    for i in range(len(p)):
        Letter_dic.append([])
        for j in range(len(s)):
            if p[i] == s[j]:
                Letter_dic[i].append(j)
    print(Letter_dic)
                
    return 0

s="abcacb"
s="abcbddddd"
p="ab"
p="abcd"
removable=[3,2,1,4,5,6]
maximumRemovals(s,p,removable)