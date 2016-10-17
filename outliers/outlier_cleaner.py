#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for (prednw, actualnw, age) in zip(predictions, net_worths, ages):
        cleaned_data.append((age[0], actualnw[0], prednw[0] - actualnw[0]))

    # sort list based on error
    cleaned_data.sort(key=lambda tup: tup[2])

    return cleaned_data[:81]

    
    

