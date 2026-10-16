class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        Lista =[]
        for i in range(numRows):
            Lista2 =[]
            for j in range(i+1):
                if j == 0 or j == i:
                    Lista2.append(1)
                else:
                    Lista2.append(Lista[i-1][j-1] + Lista[i-1][j])
            Lista.append(Lista2)
        return Lista