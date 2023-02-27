def fourSum(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    List1=[]
    Length=len(nums)
    nums.sort()
    for a in range(Length-3):
        if a>0 and nums[a]==nums[a-1]:
            continue
        if nums[a]+nums[a+1]+nums[a+2]+nums[a+3]>target:
            break
        if nums[a]+nums[Length-1]+nums[Length-2]+nums[Length-3]<target:
            continue
        for b in range(a+1,Length-2):
            if b>a+1 and nums[b]==nums[b-1]:
                continue
            if nums[a]+nums[b]+nums[b+1]+nums[b+2]>target:
                break
            if nums[a]+nums[Length-1]+nums[Length-2]+nums[b]<target:
                continue   
            L_number,R_number=b+1,Length-1      
            while L_number<R_number:
                Count_number=nums[a]+nums[b]+nums[L_number]+nums[R_number]
                if Count_number<target:
                    L_number+=1
                elif Count_number>target:
                    R_number-=1
                else:
                    List1.append([nums[a],nums[b],nums[L_number],nums[R_number]])
                    while L_number<R_number and nums[L_number]==nums[L_number+1]:
                        L_number+=1
                    L_number+=1
                    while L_number<R_number and nums[R_number]==nums[R_number-1]:
                        R_number-=1
                    R_number-=1
           
    return List1
        



nums = [1,0,-1,0,-2,2] 
target = 0
nums = [2,2,2,2,2,2] 
target = 8
nums = [0,-5,5,1,1,2,-5,5,-3] 
target =-11

print(fourSum(nums,target))
