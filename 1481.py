def findLeastNumOfUniqueInts(arr, k) -> int:
    from collections import Counter
    Arr_counter=Counter(arr)
    Arr_s_counter= sorted(Arr_counter.items(),key=lambda x:x[1])
    print(type(Arr_s_counter[0]))
    for i in range(len(Arr_s_counter)):
        if Arr_s_counter[i][1]<k:
            k=k-Arr_s_counter[i][1]
        elif Arr_s_counter[i][1]==k:
            print(Arr_s_counter[i+1])
            result=len(Arr_s_counter)-i-1
            print(len(Arr_s_counter)-i-1)
            break
        elif Arr_s_counter[i][1]>k:

            # Arr_s_counter[i][1]=int(Arr_s_counter[i][1])-k
            print(Arr_s_counter[i])
            result=len(Arr_s_counter)-i
            print(len(Arr_s_counter)-i)
            break
    print(result)

        
    return result

AAA=[5,5,3]
k=1
findLeastNumOfUniqueInts(AAA,k)