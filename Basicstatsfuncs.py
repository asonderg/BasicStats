# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:19:52 2021

@author: asond
"""
# Import the matplotlib module here.  No other modules should be used.
import matplotlib
#Import numpy for making a random vector and for checking each section.
import numpy

#Alexei Sondergeld
#9/17/2021
def basicstatsrandom(): #No inputs, the function creates its own random data.
    
    
    # Create a list variable that contains at least 25 elements.  You can create this list any number of ways.  
    # This is my sample. It is random numbers between 0 and 10.
    datavec=numpy.random.rand(50)*10
    #print(datavec)
    
    # Pretend you do not know how long x is; compute it's length, N, without using functions or modules.
    #Do a loop looking for whether each element is a type of number (float or int). If one wanted to do this for something
    #including letters, string could be added. 
    n=0
    for a in datavec:
        if type(datavec[1]) == int or float:
            n=n+1
        else:
            break
        
   
    # Compute the mean of the elements in list x.
    total=0
    for num in datavec:
        total=total+num
        
  
    mean=total/n
    
   
    
    # Compute the std deviation, using the mean and the elements in list x.
    stdevsum=0
    for num in datavec:
        stdevsum=stdevsum+(num-mean)**2/n
    stdev=(stdevsum)**0.5
    
    # Use the 'print' command to report the values of average (mu) and std. dev. (sigma).
    mu=mean
    
    
    sigma=stdev
    
    
    # Count the number of values that are within +/- 1 std. deviation of the mean.  
    # A normal distribution will have approx. 68% of the values within this range.  
    # Based on this criteria is the list normally distributed?
    counter=0
    for num in datavec:
        if num < mean+stdev and num > mean-stdev:
            counter=counter+1
        
    # Use print() and if statements to report a message about whether the data is normally distributed.
    #Generally, if about 68% of the numbers lie within a standard deviation of the mean, it is normally distributed. I give a
    # +/- 5% margin, since the count will be unlikely to be exactly equal to 68% of the numbers.
    e=.05
    
    if counter < n*(.68+e) and counter > n*(.68-e):
        distmsg='normally distributed'
        
    else:
        distmsg="not normally distributed"
    
    #Note that this randomly distributed data is uniformly distributed, but by chance, the numbers falling within a standard
    #deviation of the mean might fall within +- 5% of the 68% target and create a false positive.
    
    ### Use Matplotlb.pyplot to make a histogram of x.
    
    
    #print(xaxis)
    
    matplotlib.pyplot.figure()
    matplotlib.pyplot.hist(datavec,30)
    matplotlib.pyplot.title('Function generated data histogram')
    matplotlib.pyplot.show()
    
    #Sum the cube of the difference between each number and the mean. This is a measure of how symmetrical the histogram is.
    numerator=0
    for num in datavec:
        numerator=numerator+(num-mean)**3
    skewness=numerator/((n-1)*stdev**3)
    
    return mean, stdev, distmsg, skewness

def basicstatsuserdef(datavec): #User inputs data.
   
    
   
    
    # Pretend you do not know how long x is; compute it's length, N, without using functions or modules.
    #Do a loop looking for whether each element is a type of number (float or int). If one wanted to do this for something
    #including letters, string could be added. 
    n=0
    for a in datavec:
        if type(datavec[1]) == int or float:
            n=n+1
        else:
            break
        
   
    # Compute the mean of the elements in list x.
    total=0
    for num in datavec:
        total=total+num
        
  
    mean=total/n
    
   
    
    # Compute the std deviation, using the mean and the elements in list x.
    stdevsum=0
    for num in datavec:
        stdevsum=stdevsum+(num-mean)**2/n
    stdev=(stdevsum)**0.5
    
    # Use the 'print' command to report the values of average (mu) and std. dev. (sigma).
    mu=mean
    
    
    sigma=stdev
    
    
    # Count the number of values that are within +/- 1 std. deviation of the mean.  
    # A normal distribution will have approx. 68% of the values within this range.  
    # Based on this criteria is the list normally distributed?
    counter=0
    for num in datavec:
        if num < mean+stdev and num > mean-stdev:
            counter=counter+1
        
    # Use print() and if statements to report a message about whether the data is normally distributed.
    #Generally, if about 68% of the numbers lie within a standard deviation of the mean, it is normally distributed. I give a
    # +/- 5% margin, since the count will be unlikely to be exactly equal to 68% of the numbers.
    e=.05
    
    if counter < n*(.68+e) and counter > n*(.68-e):
        distmsg='normally distributed'
        
    else:
        distmsg="not normally distributed"
    
    #Note that this randomly distributed data is uniformly distributed, but by chance, the numbers falling within a standard
    #deviation of the mean might fall within +- 5% of the 68% target and create a false positive.
    
    ### Use Matplotlb.pyplot to make a histogram of x.

    
    #print(xaxis)
    matplotlib.pyplot.figure()
    matplotlib.pyplot.hist(datavec,30)
    matplotlib.pyplot.title('User defined data histogram')
    matplotlib.pyplot.show()
    #Sum the cube of the difference between each number and the mean. This is a measure of how symmetrical the histogram is.
    numerator=0
    for num in datavec:
        numerator=numerator+(num-mean)**3
    skewness=numerator/((n-1)*stdev**3)
    
    return mean, stdev, distmsg, skewness