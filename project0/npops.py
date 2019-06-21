from util import *
import numpy as np

def verify(py_arr, np_arr):
    v = (py_arr == np_arr)
    for c in v:
        if not c:
           return False
     
    return True

# indexing and slicing
def npops_slicing():
    a = [i for i in range(1, 10)]
    b = np.array(a)
    if verify(a[3:7:2], b[3:7:2]):
        log(green("PASS"), "py_array[3:7:2] == np_array[3:7:2]")
    else:
        log(red("FAIL"), "py_array[3:7:2] == np_array[3:7:2]")

    if verify(a[2:-1:2], b[2:-1:2]):
        log(green("PASS"), "py_array[2:-1:2] == np_array[2:-1:2]")
    else:
        log(red("FAIL"), "py_array[2:-1:2] == np_array[2:-1:2]")

    if verify(a[::-1], b[::-1]):
        log(green("PASS"), "py_array[::-1] == np_array[::-1]")
    else:
        log(red("FAIL"), "py_array[::-1] == np_array[::-1]")

    idx1 = [7, 2]
    idx2 = np.array(idx1)
    if verify(b[idx1], b[idx2]):
        log(green("PASS"), "np_array[index by py array] == np_array[index by np array]")
    else:
        log(red("FAIL"), "py_array[index by py array] == np_array[index by np array]")

if __name__ == "__main__":
    npops_slicing()
