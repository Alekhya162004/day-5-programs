MAX = 26
def atLeastK(freq, k):
    for i in range(MAX):
        if (freq[i] != 0 and freq[i] < k):
            return False
    return True
def setzero(freq):
    for i in range(MAX):
        freq[i] = 0
def findlength(string, n, k):   
    maxLen = 0
    freq = [0] * MAX  
    for i in range(n):
        setzero(freq)
        for j in range(i, n):
            freq[ord(string[j]) - ord('a')] += 1

            if (atLeastK(freq, k)):

                maxLen = max(maxLen, j - i + 1)
    return maxLen

if __name__ == "__main__":
    string =input('enter a string')

    n = len(string)
    k = int(input('enter the number'))
    if(k<1):
        print('invalid input')
    else:
        print(findlength(string, n, k))
