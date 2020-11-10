from Task import Task

def decode(Task, rnvec):
    d = Task.dims
    nvars = rnvec[:d]
    minrange = Task.Lb[:d]
    maxrange = Task.Ub[:d]
    y = maxrange - minrange
    variables = y * nvars + minrange
    return variables