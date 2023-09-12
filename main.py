import tsp_brute_force
import tsp_simulated_annealing
import random
def menu_principal():
  print('Bienvenido!, selecciona entre las siguientes opciones:')
  while True:
    print("--Menú principal--")
    print('1) Seleccionar archivo. ')
    print('2) Generar aleatoriamente la matriz de costo')
    print('3) Terminar programa')
    try:
      opt = int(input("Selecciona tu opción (1, 2 ó 3): "))
      if opt == 1:
        print("opt 1 selected")
      elif opt == 2:
        menu_generador()
      elif opt == 3:
        break
      else:
        print("Opción no válida. Por favor, selecciona 1, 2 ó 3.")
    except ValueError:
      print("Debes ingresar un número.")
    

def menu_generador():
  try:
    num_ciudades = int(input("Escribe el número de ciudades: "))
    mc = generar_matriz_costo(num_ciudades)
    print("Matriz generada: \n", mc)
    if(num_ciudades <= 10):
      tsp_brute_force.tsp_bf_solver(mc)
    tsp_simulated_annealing.simulated_annealing(mc, 1000, 0.99, 10000)
  except ValueError:
    print("Debes ingresar un número")


def generar_matriz_costo(num_ciudades):
  distancias = []
  for _ in range(num_ciudades):
      fila = [random.uniform(1, 100) for _ in range(num_ciudades)]
      distancias.append(fila)
  return distancias


menu_principal()