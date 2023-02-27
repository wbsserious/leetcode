def letterCombinations(digits):
    """
        :type digits: str
        :rtype: List[str]
        """
    Dic_number={}
    Dic_number[2]=["a","b","c"]
    Dic_number[3]=["d","e","f"]
    Dic_number[4]=["g","h","i"]
    Dic_number[5]=["j","k","l"]
    Dic_number[6]=["m","n","o"]
    Dic_number[7]=["p","q","r","s"]
    Dic_number[8]=["t","u","v"]
    Dic_number[9]=["w","x","y","z"]
    List_digits=list(digits)
    # print(List_digits)
    List_letter=[]
    List_record=[]
    for i in List_digits:
        # print(i)
        if List_letter==[]:
            for j in Dic_number[int(i)]:
                List_letter.append(j)
        else:
            # print(List_letter)
            for a in List_letter:
                for b in Dic_number[int(i)]:
                    List_record.append(a+b)
            List_letter=[]
            for letter in List_record:
                List_letter.append(letter)
            List_record=[]
            # print(List_record)
            # print(List_letter)
    return List_letter

            
                    




print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))
        