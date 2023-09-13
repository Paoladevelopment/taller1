import tsp_brute_force
import tsp_simulated_annealing
import random
import time
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
        archivo = input()
        read_file(archivo)
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
      t1_brute_force = time.time()
      tsp_brute_force.tsp_bf_solver(mc)
      t2_brute_force = time.time()
      time_execution_bf = t2_brute_force - t1_brute_force
      print("Tiempo requerido enfoque de recocido simulado para solucionar el problema del agente viajero:", f"{time_execution_bf:.6f} segundos")

    t1_simulated_annealing = time.time()
    tsp_simulated_annealing.simulated_annealing(mc, 1000, 0.99, 10000)
    t2_simulated_annealing = time.time()
    time_execution_sa = t2_simulated_annealing - t1_simulated_annealing
    print("Tiempo requerido enfoque de recocido simulado para solucionar el problema del agente viajero:", f"{time_execution_sa:.6f} segundos")
  except ValueError:
    print("Debes ingresar un número")


def generar_matriz_costo(num_ciudades):
  distancias = []
  for _ in range(num_ciudades):
      fila = [round(random.uniform(1, 100), 3) for _ in range(num_ciudades)]
      distancias.append(fila)
  return distancias


def read_file(file_name):
  matriz = []

  try:
      with open(file_name, 'r') as archivo:
          for linea in archivo:
              numeros = linea.strip().split()
              fila = [int(num) for num in numeros]
              matriz.append(fila)
      
      if len(matriz) <= 10:
        t1_brute_force = time.time()
        tsp_brute_force.tsp_bf_solver(matriz)
        t2_brute_force = time.time()
        time_execution_bf = t2_brute_force - t1_brute_force
        print("Tiempo requerido enfoque de fuerza bruta para solucionar el problema del agente viajero:", f"{time_execution_bf:.6f} segundos")
      
      t1_simulated_annealing = time.time()
      tsp_simulated_annealing.simulated_annealing(matriz, 1000, 0.99, 10000)
      t2_simulated_annealing = time.time()
      time_execution_sa = t2_simulated_annealing - t1_simulated_annealing
      print("Tiempo requerido enfoque de fuerza bruta para solucionar el problema del agente viajero:", f"{time_execution_sa:.6f} segundos")
              
  except FileNotFoundError:
      print(f"El archivo {file_name} no fue encontrado.")
      
  except Exception as e:
      print(f"Error al leer el archivo: {str(e)}")

  return matriz


menu_principal()