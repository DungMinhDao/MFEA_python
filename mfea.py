from Chromosome import Chromosome
from data_mfea import DataMFEA
import numpy as np
import random

class MFEA:
    """
    Class to initialize and execute MFEA 
    """
    def __init__(self, Tasks, pop, gen, selection_process, rmp):
        self.Tasks = Tasks
        self.pop = pop
        self.gen = gen
        self.selection_process = selection_process
        self.rmp = rmp
        self.no_of_tasks = len(self.Tasks)
        
    def execute(self):
        """
        Execute the MFEA with the given information
        """
        self.pop += self.pop % 2
        if self.no_of_tasks <= 1:
            raise Exception("Number of tasks must be at least 2")
        D = np.array([t.dims for t in self.Tasks])
        D_multitask = np.max(D)
        
        population = np.array([])
        bestobj = np.Inf * np.ones(self.no_of_tasks)
        EvBestFitness = np.zeros([self.gen, self.no_of_tasks])
        bestInd_data = [None] * self.no_of_tasks
        
        for i in range(self.pop):
            new_individual = Chromosome(D_multitask)
            new_individual.evaluate(self.Tasks, self.no_of_tasks)
            population = np.append(population, new_individual)
        
        factorial_cost = np.zeros(self.pop)
        for i in range(self.no_of_tasks):
            for j in range(self.pop):
                factorial_cost[j] = population[j].factorial_costs[i]
            population = population[np.argsort(factorial_cost)]
            for j in range(self.pop):
                population[j].factorial_ranks[i] = j + 1
            bestobj[i] = population[0].factorial_costs[i]
            EvBestFitness[0][i] = bestobj[i]
            bestInd_data[i] = population[0]
            
            
        for i in range(self.pop):
            min_rank = np.min(population[i].factorial_ranks)
            min_rank_skills = np.where(population[i].factorial_ranks == min_rank)[0]
            if (np.size(min_rank_skills) > 1):
                population[i].skill_factor = min_rank_skills[random.randint(0, np.size(min_rank_skills) - 1)]
            else:
                population[i].skill_factor = min_rank_skills[0]
            tmp = population[i].factorial_costs[population[i].skill_factor]
            population[i].factorial_costs[:] = np.Inf
            population[i].factorial_costs[population[i].skill_factor] = tmp
        
        generation = 0
        mu = 10 # Index of Simulated Binary Crossover (tunable)
        sigma = 0.02 # standard deviation of Gaussian Mutation model (tunable)
        while generation <= self.gen - 2:
            generation += 1
            print("gen ", generation)
            indorder = np.random.permutation(self.pop)
            child = np.array([])
            count = 0
            for i in range(0, self.pop//2):
                p1 = indorder[i]
                p2 = indorder[i+self.pop//2]
                child = np.append(child, Chromosome(D_multitask))
                child = np.append(child, Chromosome(D_multitask))
                if (population[p1].skill_factor == population[p2].skill_factor \
                or random.random() < self.rmp):
                    u = np.random.rand(D_multitask)
                    cf = np.zeros(D_multitask)
                    cf[u <= 0.5] = (2 * u[u <= 0.5]) ** (1/(mu+1))
                    cf[u > 0.5] = (2 * u[u > 0.5]) ** (-1/(mu+1))
                    child[count].crossover(population[p1], population[p2], cf)
                    child[count+1].crossover(population[p1], population[p2], cf)
                    if random.random() < 0.5:
                        child[count].skill_factor = population[p1].skill_factor
                    else:
                        child[count].skill_factor = population[p2].skill_factor
                    if random.random() < 0.5:
                        child[count+1].skill_factor = population[p1].skill_factor
                    else:
                        child[count+1].skill_factor = population[p2].skill_factor
                else:
                    child[count].mutate(population[p1], D_multitask, sigma)
                    child[count].skill_factor = population[p1].skill_factor
                    child[count+1].mutate(population[p2], D_multitask, sigma)
                    child[count+1].skill_factor = population[p2].skill_factor
                count += 2
        
            for i in range(self.pop):
                child[i].evaluate(self.Tasks, self.no_of_tasks)
            intpopulation = np.concatenate((population, child))
            factorial_cost = np.zeros(self.pop * 2)
            for i in range(self.no_of_tasks):
                for j in range(self.pop * 2):
                    factorial_cost[j] = intpopulation[j].factorial_costs[i]
                intpopulation = intpopulation[np.argsort(factorial_cost)]
                for j in range(self.pop * 2):
                    intpopulation[j].factorial_ranks[i] = j + 1
                if (intpopulation[0].factorial_costs[i] <= bestobj[i]):
                    bestobj[i] = intpopulation[0].factorial_costs[i]
                    bestInd_data[i] = intpopulation[0]
                EvBestFitness[generation][i] = bestobj[i]
            
            for i in range(self.pop * 2):
                min_rank = np.min(intpopulation[i].factorial_ranks)
                intpopulation[i].skill_factor = np.argmin(intpopulation[i].factorial_ranks)
                intpopulation[i].scalar_fitness = 1/min_rank
                
            if self.selection_process == 'elitist':
                # intpopulation.sort(key=lambda ind: ind.scalar_fitness, reverse=True)
                intpopulation = np.array(sorted(list(intpopulation), key = lambda ind: ind.scalar_fitness, reverse = True))
                population = intpopulation[:self.pop]
            elif self.selection_process == 'roulette wheel':
                pass
            
        data_MFEA = DataMFEA(EvBestFitness, bestInd_data)
        return data_MFEA