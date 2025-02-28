'''
Created on 24.02.2025
Code for Workbook Inference & Causality Task6
@author: tillschoenbein
'''
import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node("Exercise")
G.add_node("Weight Loss")
G.add_node("Diet")

# Add edges
G.add_edge("Exercise", "Weight Loss")
G.add_edge("Diet", "Exercise")
G.add_edge("Diet", "Weight Loss")

# Draw the graph
#pos = nx.spring_layout(G)
pos = { 
    "Exercise": (0, 0),
    "Weight Loss": (1, 0),
    "Diet": (0.5, 1),
    }

nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=15, font_weight="bold", arrowsize=20)
plt.show()

# Example probabilities for estimation
prob_W_given_E_D = 0.7  # Example value for P(Weight Loss | Exercise, Diet)
prob_D = 0.5            # Example value for P(Diet)

# Calculate the back-door adjustment with example probabilities
estimated_back_door_adjustment = prob_W_given_E_D * prob_D

print(f"Estimated Back-door adjustment considering Diet as a confounder: {estimated_back_door_adjustment}")