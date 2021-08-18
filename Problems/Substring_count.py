# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

def evenCtr(w,l):

    if list(w).count(w[0]) == l:

        return 1
    else:
        return 0
        
def oddCtr1(w,l):

    for m in range((l//2)+1):

        if w[m] == w[-(m+1)]:
            pass
        else:
            return 0

    return 1
    
def oddCtr(w,l):

    if list(w).count(w[0]) == l-1 and (l//2)+1 != w[0] :
        return 1
    elif list(w).count(w[0]) == l:
        return 1
    else:
        return 0
        
 def substrCount(n, s):

    count = n

    for i in range(2,n+1):
        for j in range(n):

            if j+i <= n:
                
                word = s[j:j+i]
                low = len(word)

                if low%2 == 0:

                    count += evenCtr(word,low)

                else:

                    count += oddCtr(word,low)

            else:
                break

    return count
    
string = 'mnonopoo'
los = len(string)

substrCount(los,string)
