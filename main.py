from Chromosome import Chromosome
from Task import Task
from test_functions import sphere1, sphere2, sphere3
from mfea import MFEA
from data_mfea import DataMFEA
import numpy as np
        
Tasks = []
Tasks.append(Task(dims=3, fnc=sphere1, Lb=-3*np.ones(3), Ub=3*np.ones(3)))
Tasks.append(Task(dims=2, fnc=sphere2, Lb=-10*np.ones(2), Ub=5*np.ones(2)))
Tasks.append(Task(dims=3, fnc=sphere3, Lb=-5*np.ones(3), Ub=5*np.ones(3)))
Tasks.append(Task(dims=3, fnc=sphere3, Lb=-5*np.ones(3), Ub=7*np.ones(3)))

pop = 30
gen = 50
selection_process = 'elitist'
rmp = 0.3

process_MFEA = MFEA(Tasks, pop, gen, selection_process, rmp)
data_MFEA = process_MFEA.execute()
[i.decode(Tasks) for i in data_MFEA.bestInd_data]

print(data_MFEA.EvBestFitness[:])
print(data_MFEA.bestInd_data)

