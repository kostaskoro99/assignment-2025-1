# kostaskoro99-algo-assignments

import itertools
import argparse
import networkx as nx

# True αν οι δυαδικες συμβολοσειρες a & b διαφερουν κατα μια μονο μεταθεση. False διαφορετικα
def is_valid_transition(a,b):

diff = sum(x != y for x,y in zip(a,b))
return diff = 2 and sorted(a) == sorted(b)


# Κατασκευαζει ολες τις μεταθεσεις του γραφου με s μηδενικα(0) και t ασσους(1) 
  def generate_nodes(s,t):

base = ['0'] * s + ['1'] * t 
perms = set(itertools.permutations(base)) 

return [''. join(p) for p in perms]

def build_permutation_graph(s,t):
     nodes = generate_nodes(s,t)
     G = nx.Graph()
     G.add_nodes_from(nodes)

     for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
          if is_valid_transition(nodes[i],nodes[j]):
        G.add_edge(nodes[i],nodes[j])

        return G 

# ευρεση συμβατης genlex διαδρομης
def dfs_paths(graph, start, path=None, visited=None):
     if path is None:
         path = [start]
     if visited is None:
         visited = set([start])

     if len(path) == len(graph.nodes):
         return [path]

     paths = []
     for neighbor in
  graph.neighbors(start):
        if neighbor not in visited:
            new_path = path + [neighbor]
            new_visited = visited | {neighbor}
    
   result = dfs_paths(graph, neighbor, new_path, new_visited)
        paths.extend(result)

      return paths

 def main():
    s = 2
    t = 3
    G = build_permutation_graph(s,t)
    all_nodes = list(G.nodes)

      print(f"Συνολικοι Κομβοι: {len(all_nodes)}")
      print("Εκκινηση DFS για ευρεση διαδρομων ακολουθιας Genlex")

       for start in all_nodes:
           paths = dfs_paths(G, start)
           if paths:
                print(f"\nΕντοπιστηκε Μονοπατι {start}:")
                 for p in paths[:1]: # δειξε μονοπατι εκκινησης
                   for b in p:
                       print(f"{b} ({int(b,2)})")  
                        break 
            else:
                print("δε βρεθηκε πληρες μονοπατι")

          if __name__ == "__main__":
              main()






