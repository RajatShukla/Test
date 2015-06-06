__author__ = 'RAJAT'
def findCandidate(a):
    arr_size = len(a)
    maj_index, count = 0,1
    i=0
    while(i<arr_size):
        if(a[maj_index] == a[i]):
            count += 1
        else:
            count -= 1
        if(count == 0):
            maj_index = i
            count = 1
        i += 1
    return a[maj_index]


def isMajority(a, element):
    arr_size = len(a)
    count = 0;
    for i in a:
        if i == element:
            count += 1
            if(count > arr_size/2):
                return 1
    return 0

def main():
    a = [1, 3, 3, 1, 2, 1, 1, 1]
    candidate = findCandidate(a)
    ret_val = isMajority(a, candidate)
    if(ret_val == 1):
        print(candidate)


main()


