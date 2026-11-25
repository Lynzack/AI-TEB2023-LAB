import random

#six delivery locations
locations = [ 'B', 'C', 'D', 'E', 'F', 'G']

#distance matrix/dataset
distance_matrix = {
    'A': {'A': 0, 'B': 4, 'C': 8, 'D': 6, 'E': 7, 'F': 9, 'G': 5},
    'B': {'A': 4, 'B': 0, 'C': 5, 'D': 7, 'E': 3, 'F': 8, 'G': 6},
    'C': {'A': 8, 'B': 5, 'C': 0, 'D': 4, 'E': 6, 'F': 3, 'G': 7},
    'D': {'A': 6, 'B': 7, 'C': 4, 'D': 0, 'E': 5, 'F': 6, 'G': 8},
    'E': {'A': 7, 'B': 3, 'C': 6, 'D': 5, 'E': 0, 'F': 4, 'G': 6},
    'F': {'A': 9, 'B': 8, 'C': 3, 'D': 6, 'E': 4, 'F': 0, 'G': 5},
    'G': {'A': 5, 'B': 6, 'C': 7, 'D': 8, 'E': 6, 'F': 5, 'G': 0}
}

#function to calculate fitness for route
def calculate_fitness (route):
    total_distance = 0
    new_route = []
    new_route = ["A"] + route + ["A"]  #combine with starting point and last point
    for i in range(len(new_route)-1):
        current = new_route[i]
        next_location = new_route[i+1]

        total_distance += distance_matrix[current][next_location]


    return total_distance

#generate random sequence based o location element
def generate_chromosome():
    chromosome = random.sample(locations, 6)
    return chromosome

#generate multiple chromosome up to population size
def generate_population (size):
    population = []
    for i in range(size):
        population.append(generate_chromosome())

    return population

 #select random 3 population to compare the minimum fitness - chromosome with minimum fitness is selected as parent
def selection(population):
    tournament = random.sample(population, 3)
    candidates = []
    parent = []

    for x in tournament:
        
        fitness = calculate_fitness(x)
        candidates.append(fitness)
    lowest = min(candidates)
    index = candidates.index(lowest)
    parent = tournament[index]

    return parent
        
#order crossover 
def crossover(parent1,parent2):
    # find random index
    point1 = random.randint(0,len(parent1)-1)
    point2 = random.randint(0,len(parent1)-1)

    #make sure first point always lower
    start, end = sorted([point1, point2])

    #identify the section slice and append in child
    section = parent1[start:end]
    child = [None] * 6
    child[start : end] = section

    i = end
    j = end

    #the remaining position is filled with parent2 order starting from 'end' index
    while None in child :  
        if parent2[i] not in child: #ensure no repetition of delivery location
            child[j] = parent2[i]
            j = (j+1) % len(parent1)
        i = (i+1) % len(parent1)

    return child

#sway delivery location
def mutation(child):
    #find random index
    first = random.randint(0,len(child)-1)
    second = random.randint(0,len(child)-1)

    #prevent the index of first and second is same 
    while second == first :
        second = random.randint(0,5)

    location1 = child[first]
    child[first] = child[second]
    child[second] = location1


    return child 

#identify best route based on lower fitness score
def bestRoute (population):
    best_fitness = 999
    best_route = []
    for x in population:
        fitness = 0
        fitness = calculate_fitness(x)
        if fitness < best_fitness :
            best_fitness = fitness
            best_route = x
    return best_route, best_fitness

    


def run_GA(size,generation):
    #initial population
    population = generate_population(size)
    print("generating population....")
    #repeat for 50 generations
    for i in range(generation):  

        new_population =[]
        #identify elitism for every generation
        best_route, best_fitness = bestRoute(population)
        new_population.append(best_route)

        #repeat selection, crossover, mutation
        while len(new_population)< (size):
            parent1 = selection(population)
            parent2 = selection(population)
            
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent1, parent2)
            
            child1 = mutation(child1)
            child2 = mutation(child2)

            new_population.append(child1)
            if len(new_population) < size:
                new_population.append(child2)
           

        population = new_population
        best_route, best_fitness = bestRoute(population)

    return population,best_route, best_fitness
        

def main():
    random.seed(42)
    
    routes, best, fitness = run_GA(10,50)
    print("Population : ", routes)

    route = ["A"] + best + ["A"]
    print("Best Route : ", route)
    print("Total Distance : ", fitness , " km")

if __name__ == "__main__" :
    main()
    


