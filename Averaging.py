# Given a list of lists each consisting of arrays
# with different sizes, this functions computes the average of these lists. 

#Use: This function can be used to average the gradients of a model (NN) parameters over a specific number of epochs. 


def averaging(params): # params [[],[],....[]]
    s=[]
    l1=len(params)  # no. of nodes
    l2=len(params[0]) # no. of arrays of parameters
    for i in range(l2):
        d=0
        for j in range(l1): 
            d+=params[j][i]/l1
        s.append(d)
    

    return s


# Example:

# l=[[np.array([[2,2], [1,1]]), np.array([2,2])], [np.array([[3,3], [3,3]]),np.array([0,0])]]
# averaging(l)

# output: 
#[array([[2.5, 2.5],
    #    [2. , 2. ]]), array([1., 1.])]
