class NumberContainers(object):

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