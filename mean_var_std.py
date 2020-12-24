import numpy as np

def calculate(lst):
    # if input list is wrong size, raise value error with message
  if len(lst) != 9:
    raise ValueError('List must contain nine numbers.')

  # list turned into array
  flat = np.array(lst)
  # 1 x 9 array turned into 3 x 3 array
  arr = np.reshape(flat, (3, 3))

  # dict created
  calc_dict = {}

  # declares lists
  mean_list = []
  var_list = []
  stdev_list = []
  max_list = []
  min_list = []
  sum_list = []

  # declares lists
  # mean axes 1 and 2
  ma1 = []
  ma2 = []
  # variance axes 1 and 2
  va1 = []
  va2 = []
  # standard deviation axes 1 and 2
  sda1 = []
  sda2 = []
  # maximimum axes 1 and 2
  max1 = []
  max2 = []
  # minimum axes 1 and 2
  min1 = []
  min2 = []
  # sum axes 1 and 2
  sum1 = []
  sum2 = []

  # iterates through elements of array to initialize above lists
  for i in range(3):
    ma1.append(np.mean(arr[:, i]))
    ma2.append(np.mean(arr[i, :]))
    va1.append(np.var(arr[:, i]))
    va2.append(np.var(arr[i, :]))
    sda1.append(np.std(arr[:, i]))
    sda2.append(np.std(arr[i, :]))
    max1.append(np.max(arr[:, i]))
    max2.append(np.max(arr[i, :]))
    min1.append(np.min(arr[:, i]))
    min2.append(np.min(arr[i, :]))
    sum1.append(np.sum(arr[:, i]))
    sum2.append(np.sum(arr[i, :]))
  
  # adds variables to associated lists in format [axis1, axis2, flattened]
  mean_list.extend([ma1, ma2, np.mean(flat)])
  var_list.extend([va1,va2, np.var(flat)])
  stdev_list.extend([sda1, sda2, np.std(flat)])
  max_list.extend([max1, max2, np.max(flat)])
  min_list.extend([min1, min2, np.min(flat)])
  sum_list.extend([sum1, sum2, np.sum(flat)])

  # sets up dict
  calc_dict['mean'] = mean_list
  calc_dict['variance'] = var_list
  calc_dict['standard deviation'] = stdev_list
  calc_dict['max'] = max_list
  calc_dict['min'] = min_list
  calc_dict['sum'] = sum_list

  return calc_dict
