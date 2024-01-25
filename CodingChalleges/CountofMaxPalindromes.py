def prepareMatrix(size):
    matrix = [[-1 for i in range(size)] 
              for j in range(size)]
    return matrix

def isPalindrome(S:str,i:int,j:int) -> int:
    if i > j:
        return 1
    if matrix[i][j] != -1:
        return matrix[i][j]
    if S[i] != S[j]:
        matrix[i][j] = 0
        return matrix[i][j]
    matrix[i][j] = isPalindrome(S,i + 1,j - 1)
    return matrix[i][j]

def numMaxPalindromicSequences(S:str) -> int:
    n = len(S)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if isPalindrome(S,i,j) != 0:
                count += 1
    return count
    
if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        S = input().strip()
        matrix = prepareMatrix(1001)
        print (numMaxPalindromicSequences(S))