# This file converts a list of tensors
# with different sizes into a vector so it can be histogrammed 

def histo(x): 
    d=[]
    for j in range(len(x)):
        d=tf.concat([d, tf.reshape(x[j], [-1])],0)
    return d
