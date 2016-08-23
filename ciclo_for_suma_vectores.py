# Vector addition function
###################################################
# Student should enter code below
def add_vector(v, w):
    vv=list(v)
    for i in range(len(v)):
        vv[i]= v[i]+w[i]
        #return vv
    return vv

###################################################
# Test

print add_vector([4, 3], [0, 0])
print add_vector([1, 2], [3, 4])
print add_vector([2, 3], [-6, -3])
print add_vector([5, 3, 5], [-6, -3, 5])
print add_vector([1, 4, -4, 7], [-6, -3, 8, 8])

###################################################
# Output

#[4, 3]
#[4, 6]
#[-4, 0]
