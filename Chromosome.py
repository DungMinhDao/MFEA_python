import numpy as np
import fnceval

class Chromosome:
    """
    Chromosome - individual that is used for MFEA
    """
    def __init__(self, D=None, rnvec=np.array([])):
        if np.size(rnvec) == 0:
            self.rnvec = np.random.rand(D)
        else:
            self.rnvec = rnvec
            
        self.factorial_costs = None
        self.factorial_ranks = None
        self.scalar_fitness = 0
        self.skill_factor = 0
        self.solution = None
    
    def evaluate(self, Tasks, no_of_tasks):
        self.factorial_costs = np.zeros(no_of_tasks) * np.Inf
        self.factorial_ranks = np.zeros(no_of_tasks)
        if self.skill_factor == 0:
            for i in range(no_of_tasks):
                self.factorial_costs[i] = Tasks[i].fnc(fnceval.decode(Tasks[i], self.rnvec))
        else:
            for i in range(no_of_tasks):
                if self.skill_factor == i: 
                    self.factorial_costs[i] = Tasks[i].fnc(fnceval.decode(Tasks[i], self.rnvec))
                    break
        
    def mutate(self, parent, D, sigma):
        rvec = np.random.normal(0, sigma, D)
        self.rnvec = parent.rnvec + rvec
        self.rnvec[self.rnvec > 1] = 1
        self.rnvec[self.rnvec < 0] = 0
    
    def crossover(self, parent1, parent2, cf):
        self.rnvec = 0.5 * ((1+cf) * parent1.rnvec + (1-cf) * parent2.rnvec)
        self.rnvec[self.rnvec > 1] = 1
        self.rnvec[self.rnvec < 0] = 0
        
    def decode(self, Tasks):
        self.solution = fnceval.decode(Tasks[self.skill_factor], self.rnvec)
        
    def __repr__(self):
        return "****************************************" \
             + "\n| Chromosome: " + str(self.rnvec) \
             + "\n| Factorial costs: " + str(self.factorial_costs) \
             + "\n| Factorial ranks: " + str(self.factorial_ranks) \
             + "\n| Scalar fitness: " + str(self.scalar_fitness) \
             + "\n| Skill factor: " + str(self.skill_factor) \
             + "\n| Solution for skill factor: " + str(self.solution) \
             + "\n****************************************\n"
    
    def __str__(self):
        return self.__repr__()