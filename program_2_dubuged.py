#Here we are going to swap x and y values

#some found problems are: indexing of the coordinates when swapping, once the problem is solved, the swap function should correctly flip the x and y coordinates in the coords array.


import numpy as np
def swap(coords: np.ndarray):
#wrong way
  """coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3], = coords[:, 1], coords[:, 1], coords[:, 3], coords[:, 2]
  return coords"""
#correct answer for this problem

  coords[:, [0, 1, 2, 3]] = coords[:, [1, 0, 3, 2]]
  return coords

