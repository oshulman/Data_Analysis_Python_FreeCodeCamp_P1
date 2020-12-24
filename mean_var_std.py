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

  # declares and initializes lists
  mean_list = [list(arr.mean(axis=0)), list(arr.mean(axis=1)), flat.mean()]
  var_list = [list(arr.var(axis=0)), list(arr.var(axis=1)), flat.var()]
  stdev_list = [list(arr.std(axis=0)), list(arr.std(axis=1)), flat.std()]
  max_list = [list(arr.max(axis=0)), list(arr.max(axis=1)), flat.max()]
  min_list = [list(arr.min(axis=0)), list(arr.min(axis=1)), flat.min()]
  sum_list = [list(arr.sum(axis=0)), list(arr.sum(axis=1)), flat.sum()]

  # sets up dict
  calc_dict['mean'] = mean_list
  calc_dict['variance'] = var_list
  calc_dict['standard deviation'] = stdev_list
  calc_dict['max'] = max_list
  calc_dict['min'] = min_list
  calc_dict['sum'] = sum_list

  #print(arr.mean(axis=0))
  return calc_dict
