class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[[1],[1,1]]
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        for i in range(1,numRows-1):
            value=[1]
            for j in range(i):
                sum=arr[i][j]+arr[i][j+1]
                value.append(sum)
    
            value.append(1)
            arr.append(value)
            print(arr)
        return arr