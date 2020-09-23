# All decimal 3 places
import math
import numpy as np
# Function to compute sum. You cant use Python functions
def summation(first_list):
# sum Logic
    for i in first_list:
        if not isinstance(i,float) and not isinstance(i,int):
            return 0
    sum =0
    summation_value = round([sum := sum + i for i in first_list ][-1],2) #used walrus opperator 
    return summation_value


# Function to compute mean
def mean(first_list):
    # mean Logic
    for i in first_list:
        if not isinstance(i,float) and not isinstance(i,int):
            return 0

    mean_value = round(summation(first_list)/len(first_list),2)
    
    return mean_value



# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    for i in first_list:
        if not isinstance(i,float) and not isinstance(i,int):
            return 0
    first_list = sorting(first_list)
    l = len(first_list)
    if l%2!=0:
        median_value = (first_list[int(l/2)] + first_list[int(l/2) + 1])/2
    else:
        median_value = first_list[int(l/2)]
    median_value = round(median_value,2)
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    for i in first_list:
        if not isinstance(i,float) and not isinstance(i,int):
            return 0
    standard_deviation_value = round(math.sqrt(variance(first_list)),2)
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    for i in first_list:
        if not isinstance(i,float) and not isinstance(i,int):
            return 0
    variance_value = mse(first_list, [mean(first_list) for i in first_list])
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    if len(first_list) != len(second_list):
        return 0
    for i,j in zip(first_list, second_list):
        if (not isinstance(i,float) and not isinstance(i,int)) or ( not isinstance(j,float) and not isinstance(j,int)) :
            return 0

    rmse_value = round(math.sqrt(mse(first_list,second_list)),2)
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    if len(first_list) != len(second_list):
        return 0
    for i,j in zip(first_list, second_list):
        if (not isinstance(i,float) and not isinstance(i,int)) or ( not isinstance(j,float) and not isinstance(j,int)) :
            return 0

    mse_value = round(summation([(first_list[i] - second_list[i])**2 for i in range(len(first_list))])/len(first_list),2)
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    if len(first_list) != len(second_list):
        return 0
    for i,j in zip(first_list, second_list):
        if (not isinstance(i,float) and not isinstance(i,int)) or ( not isinstance(j,float) and not isinstance(j,int)) :
            return 0
    mae_value = round(summation([abs(first_list[i]-second_list[i]) for i  in range(len(first_list))])/len(first_list),2)
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    if len(first_list) != len(second_list):
        return 0
    for i,j in zip(first_list, second_list):
        if (not isinstance(i,float) and not isinstance(i,int)) or ( not isinstance(j,float) and not isinstance(j,int)) :
            return 0
    nse_value = round(1- (mse(first_list,second_list)/mse(first_list,[mean(first_list) for i in first_list])),2)

    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    if len(first_list) != len(second_list):
        return 0
    for i,j in zip(first_list, second_list):
        if (not isinstance(i,float) and not isinstance(i,int)) or ( not isinstance(j,float) and not isinstance(j,int)) :
            return 0
    pcc_value = round(summation([(first_list[i] - mean(first_list))*(second_list[i] - mean(second_list)) for i in range(len(first_list))])/((rmse(first_list, [mean(first_list) for i in first_list])) * (rmse(second_list, [mean(second_list) for i in second_list]) * len(first_list) )),2)
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    for i in first_list:
        if not isinstance(i,float) and not isinstance(i,int):
            return 0
    s = standard_deviation(first_list)
    skewness_value = round(summation([((x - mean([first_list]))**3/s) for x in first_list ])/len(first_list),2)
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    for i in first_list:
        if not isinstance(i,float) and not isinstance(i,int):
            return 0
    for j in range(len(first_list)-1):
        for i in range(len(first_list)-1):
            if first_list[i]>first_list[i+1]:
                first_list[i],first_list[i+1] = first_list[i+1],first_list[i]
    sorted_list  = first_list
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    for i in first_list:
        if not isinstance(i,float) and not isinstance(i,int):
            return 0
    s = standard_deviation(first_list)
    
    kurtosis_value = round(summation([(x - mean([first_list]))**4/s for x in first_list ])/len(first_list),2)
    return kurtosis_value



