

letters = "acdegilmnoprstuw"

def hash(string):
    """
    implementing the hashing algorithm
    """
    h = 7 
    for i in range(len(string)):
        h = h*37 + letters.index(string[i])
    return h


def lengthOfString(hashed):
    """
    find length of string since we can deduce from 
    the hash algorithm that hashed int 
    will be greater than 37**n and lesser than 37**(n+1)
    """
    n = 0
    while True:
        if hashed < 37**n:
            return n - 1
            break
        n += 1


def reverseHash(hashed):
    """
    start with a string that will return largest int,
    and iterate towards the given hashed int by replacing 
    each letter in that string.
    """
    n = lengthOfString(hashed)
    startString = 'w' * n
    finalString = ''
    for i in range(n):
        for letter in letters:
            startString = startString[:i] + letter + startString[i+1:n]
            if hash(startString) >= hashed:
                finalString += letter
                break
    return finalString


if __name__ == "__main__":
    
    import sys
    argv = sys.argv[1:]

    if argv[0] == "hash":
        print("hashed int -- {}".format(hash(argv[1])))
    elif argv[0] == "reverse":
        print("reverse hash for {} is -- {}".format(argv[1],reverseHash(int(argv[1]))))
    else:
        print('''Please use the following options to run this script:
                  - python3 reverseHash.py hash <string containing letters from "acdegilmnoprstuw">
                  - python3 reverseHash.py reverse <hashed-int>
              ''')



