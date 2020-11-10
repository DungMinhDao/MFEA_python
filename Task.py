import numpy as np

class Task:
    """
    Task in MFEA that is performed by individuals
    """
    def __init__(self, dims, fnc, Lb, Ub):
        self.dims = dims
        self.fnc = fnc
        self.Lb = Lb
        self.Ub = Ub
        
    def __repr__(self):
        return "Task(Dimension={}, Function={}, Lowerbound={}, Upperbound={})".format(self.dims, self.fnc.__doc__, self.Lb, self.Ub)
    
    def __str__(self):
        return "Task(Dimension={}, Function={}, Lowerbound={}, Upperbound={})".format(self.dims, self.fnc.__doc__, self.Lb, self.Ub)