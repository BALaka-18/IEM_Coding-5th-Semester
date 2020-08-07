# Vessel filling problem
# Calculate GCD to check validity of Diophantine equation
def GCD(a,b):
    if b == 0:
        return a;
    return GCD(b,a%b)
# Function to define the steps.
# to - Vessel to be poured into
# fro - Vessel to be poured from
'''Algorithm :
    A. Pouring from a ltr to b ltr vessel.
        1. Fill the vessel of 'a' litres and empty into 'b' litres vessel.
        2. Empty 'b' litres vessel whenever it becomes full. Fill 'a' litres vessel whenever it becomes empty.
        3. Continue till one of the vessels achieve 'c' litres.
    B. Pouring from b ltrs to a ltrs vessel.
        1. Fill the vessel of 'b' litres and empty into 'a' litres vessel.
        2. Empty 'a' litres vessel whenever it becomes full. Fill 'b' litres vessel whenever it becomes empty.
        3. Continue till one of the vessels achieve 'c' litres.
'''
def vesselPour(to,fro,c):
    # Initialize 'to' to 0 and 'fro' to current value
    toVes = 0
    froVes = fro
    # Initialize step = 1 
    step = 1 
    # Condition
    while (toVes is not c) and (froVes is not c):
        pour = min(toVes,froVes)
        # Update step
        froVes = froVes - pour
        toVes = toVes + pour
        step = step + 1 
        
        # Check for breaking of condition 
        if (toVes == c) or (froVes == c):
            break
        # Else, if Vessel 1 is empty, fill it. If Vessel 2 is filled, then empty it.
        if froVes == 0:
            froVes = fro
            step = step + 1 
        if toVes == to:
            toVes = 0
            step = step + 1 
    return step
    
# Function to calculate minimum no. of steps from among Case A and Case B.
def minSteps(a,b,c):
    if b > a:
        p = b 
        b = a 
        a = p 
    # Check validity of Diophantine equation
    if (c%GCD(a,b) is not 0):
        return -1
    return (min(vesselPour(a,b,c),vesselPour(b,a,c)))
    
# Driver code 
if __name__ == "__main__":
    result = []
    t = int(input())
    while t > 0:
        a = int(input())
        b = int(input())
        c = int(input())
        result.append(minSteps(a,b,c))
        t = t - 1 
    for r in result:
        print(r)
