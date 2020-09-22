# All decimal 3 places
import math
# Function to compute mean
def mean(first_list):
    # mean Logic
    for i in first_list:
        if (type(i) != float and type(i) != int):
            return 0
    mean_value = round(summation(first_list)/len(first_list),3)
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    for i in range(len(first_list)-1):
        if first_list[i]>first_list[i+1]:
            first_list[i],first_list[i+1] = first_list[i+1],first_list[i]
    l = len(first_list)
    if l%2!=0:
        median_value = first_list[l/2] + first_list[l/2 + 1]
    else:
        median_value = first_list[l/2]
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    rmse_value = round(math.sqrt(mse(first_list,second_list)),3)
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    if len(first_list) != len(second_list):
        return 0
    for i,j in first_list, second_list:
        if (type(i) != float and type(i) != int) or (type(j) != float and type(j) != int) :
            return 0

    mse_value = round(summation([(first_list[i] - second_list[i])**2 for i in range(len(first_list))])/len(first_list),3)
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    if len(first_list) != len(second_list):
        return 0
    for i,j in first_list, second_list:
        if (type(i) != float and type(i) != int) or (type(j) != float and type(j) != int) :
            return 0
    mae_value = round(summation([abs(first_list[i]-second_list[i]) for i  in range(len(first_list))])/len(first_list),3)
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    if len(first_list) != len(second_list):
        return 0
    for i,j in first_list, second_list:
        if (type(i) != float and type(i) != int) or (type(j) != float and type(j) != int) :
            return 0
    nse_value = round(1- (mse(first_list,second_list)/mse(first_list,[mean(first_list) for i in first_list])),3)

    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    if len(first_list) != len(second_list):
        return 0
    for i,j in first_list, second_list:
        if (type(i) != float and type(i) != int) or (type(j) != float and type(j) != int) :
            return 0
    pcc_value = round(summation([(first_list[i] - mean(first_list))*(second_list[i] - mean(second_list)) for i in len(first_list)])/((rmse(first_list, [mean(first_list) for i in first_list])) * (rmse(second_list, [mean(second_list) for i in second_list]) * len(first_list) )),3)
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
# sum Logic
    for i in first_list:
        if (type(i) != float and type(i) != int):
            return 0
    sum =0
    summation_value = round([sum + i for i in first_list ][-1],3)
    return summation_value

