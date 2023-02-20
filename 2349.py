class NumberContainers(object):
# 设计一个数字容器系统，可以实现以下功能：

# 在系统中给定下标处 插入 或者 替换 一个数字。
# 返回 系统中给定数字的最小下标。
# 请你实现一个 NumberContainers 类：

# NumberContainers() 初始化数字容器系统。
# void change(int index, int number) 在下标 index 处填入 number 。如果该下标 index 处已经有数字了，那么用 number 替换该数字。
# int find(int number) 返回给定数字 number 在系统中的最小下标。如果系统中没有 number ，那么返回 -1 。
 
    def __init__(self):
        self.table={}
        self.tableindex={}


    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if number not in self.tableindex:
            self.tableindex[number]=[]

        if index in self.table and self.table[index]!=number:
            self.tableindex[self.table[index]].remove(index)
            self.tableindex[number].append(index)
            self.table[index]=number
        elif index not in self.table:
            self.table[index]=number
            self.tableindex[number].append(index)
            
    
        print(self.table)
        print(self.tableindex)
        print("111111111111111111111111111")

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number not in self.tableindex or self.tableindex[number]==[] :
            return -1
        return min(self.tableindex[number])





NumberContainers=NumberContainers()
print(NumberContainers.find(10))
# NumberContainers.change(2,10)
NumberContainers.change(1,10)
# NumberContainers.change(3,10)
print(NumberContainers.find(10))
NumberContainers.change(1,10)
NumberContainers.change(1,20)
print(NumberContainers.find(10))
