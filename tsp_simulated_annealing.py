import random
import math

def calc_total_distance(route, distance_matrix):
    total_distance = 0
    num_nodes = len(route)
    for i in range(num_nodes - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  
    return total_distance


def random_initial_route(num_cities): 
    initial_sol = list(range(num_cities))
    random.shuffle(initial_sol)
    return initial_sol


def simulated_annealing(distance_matrix, initial_temp, cooling_rate, max_iterations):
    num_nodes = len(distance_matrix)
    current_route = random_initial_route(num_nodes)
    current_distance = calc_total_distance(current_route, distance_matrix)
    best_route = current_route
    best_distance = current_distance
    temperature = initial_temp
    for _ in range(max_iterations):

        #Enfriar la temperatura
        temperature *= cooling_rate
        #Crear una copia de la ruta actual
        nb_sol = current_route[:]
        #Intercambiar dos coordenadas y obtener una nueva sol vecina
        r1, r2 = random.sample(range(num_nodes), 2)
        temp = nb_sol[r1]
        nb_sol[r1] = nb_sol[r2]
        nb_sol[r2] = temp
        
        #distancia de la sol vecina
        nb_distance = calc_total_distance(nb_sol, distance_matrix)
        
        #Se calcula la diferenciade distancias entre la vecina solución y la actual
        diff_distance = nb_distance - current_distance

        #Se decide si la nueva sol se acepta
        if diff_distance < 0 or random.random() < math.exp(-diff_distance/temperature):
            current_route = nb_sol
            current_distance= nb_distance

            if current_distance < best_distance:
                best_route = current_route
                best_distance = current_distance 
    print("Mejor ruta encontrada (recocido simulado): ", tuple(best_route) + (best_route[0],))
    print("Distancia más corta (recocido simulado): ", best_distance)
