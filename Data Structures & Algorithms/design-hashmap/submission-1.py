class MyHashMap:

    def __init__(self):
        self.dic=[]

    def put(self, key: int, value: int) -> None:
        found=False
        for i in range(len(self.dic)):
            if self.dic[i][0]==key:
                self.dic[i][1]=value
                found=True
                break
        if found==False:
            self.dic.append([key,value])
        #print("put",self.dic)

    def get(self, key: int) -> int:
        for i in range(len(self.dic)):
            if self.dic[i][0]==key:
                return self.dic[i][1]        
        return -1


    def remove(self, key: int) -> None:
        #print(self.dic)
        for i in range(len(self.dic)):
           # print(i,key,self.dic[i][0])
            if self.dic[i][0]==key:
                self.dic.pop(i)   
                return    


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)