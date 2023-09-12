from itertools import permutations

matriz_costo = [
  [0, 2, 5, 7],
  [2,0,8,3],
  [5,8,0,1],
  [7,3,1,0]
]


#generation of the (n-1)! permutations of the cities (nodes), and returning the routes adding the startNode.
def obtain_routes(lst_nodes, startNode) :
  generated_permutations = permutations(lst_nodes)
  return [(startNode,) + p for p in generated_permutations]


#Given a route, it calculates the sum of it. 
def calc_total_distance(graph, route):
  total_distance = 0
  num_nodes = len(route)
  for i in range(num_nodes -1):
    total_distance += graph[route[i]][route[i+1]]
  total_distance += graph[route[num_nodes -1]][route[0]]
  return total_distance

def tsp_bf_solver(graph, startNode = 0): 
  number_nodes = len(graph)
  #list of the nodes that are going to permutate
  lst_nodes = list(range(number_nodes))
  del lst_nodes[startNode]
  routes = obtain_routes(lst_nodes, startNode)
  #So far we do not have a best route yet
  best_route = None
  #neither we have a shortest distance yet.
  shortest_distance = float("inf")
  for route in routes:
    distance_sum = calc_total_distance(graph, route)
    print("route", route + (startNode,), "->", distance_sum)
    if distance_sum < shortest_distance: 
      shortest_distance = distance_sum
      best_route = route
  print("Mejor ruta encontrada (fuerza bruta): ", best_route + (startNode,))
  print("Distancia más corta (fuerza bruta): ", shortest_distance)


