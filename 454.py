def fourSumCount(nums1, nums2, nums3, nums4):
    """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
    List1={}
    C_number=0
    Length=len(nums1)
    nums1.sort()
    nums2.sort()
    nums3.sort()
    nums4.sort()
    for c in range(Length):
        for d in range(Length):
            number2=-nums3[c]-nums4[d]
            if number2 in List1:
                C_number+=List1[number2]
    return C_number

nums1 = [0,1,-1]
nums2 = [-1,1,0]
nums3 = [0,0,1]
nums4 = [-1,1,1]
print(fourSumCount(nums1,nums2,nums3,nums4))
