from collections import defaultdict

# l = [234,567,321,345,123,110,767,111]
def countPairs(l,bitp = [],firsts = [],check = defaultdict(list),pairs=0):
    # Part 1 : Bit scores
    for num in l:
        temp = [int(i) for i in str(num)]
        bit_sc = (11*max(temp)) + (7*min(temp))
        bitp.append(bit_sc%100)
    firsts = list(map(lambda x : x//10, bitp)) # Store the MSBs
    # Lookup table
    for i,dig in enumerate(firsts):
        if i not in check[dig]:
            check[dig].append(i)
        else:
            continue
    # Part 2 : Count pairs
    for elem in check.values():
        pe,po,p_curr = 0,0,0
        t_ev,t_odd = list(filter(lambda x: x%2 == 0, elem)),list(filter(lambda x: x%2 != 0, elem))
        # Even indices
        if len(t_ev) >= 3:
            pe += 2
        elif len(t_ev) == 2:
            pe += 1
        else:
            pe += 0
        # Odd indices
        if len(t_odd) >= 3:
            po += 2
        elif len(t_odd) == 2:
            po += 1 
        else:
            po += 0 
        p_curr += (po + pe)
        if p_curr >= 3:
            pairs += 2
        else:
            pairs += p_curr
    return pairs
    
# Driver code
if __name__ == "__main__":
    N = int(input())
    l = list(map(int, input().split()))
    res = countPairs(l)
    print(res)
