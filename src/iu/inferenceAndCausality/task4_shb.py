'''
Created on 24.02.2025
Code for Workbook Inference & Causality Task4
@author: tillschoenbein
'''
import networkx as nx
import matplotlib.pyplot as plt

# Given probabilities
P_Y_X = 0.30
P_X_Z1 = 0.40
P_X_Z2 = 0.50
P_Y_Z1 = 0.20
P_Y_Z2 = 0.25
P_Y_given_Z1 = 0.2
P_Y_given_Z2 = 0.25


# Calculate P(Z1) and P(Z2)
P_Z1 = P_X_Z1 / (P_X_Z1 + P_X_Z2)
P_Z2 = P_X_Z2 / (P_X_Z1 + P_X_Z2)

# Calculate the causal effect using the back-door adjustment formula
causal_effect_back_door_adjustment = (P_Y_given_Z1 * P_Z1) + (P_Y_given_Z2 * P_Z2)

print(f"Causal Effect using Back-Door Adjustment Formula: {causal_effect_back_door_adjustment}")

# Create a directed graph for the DAG
G = nx.DiGraph()

# Add nodes
G.add_node("Gen. Marker A (Z1)", label="hah")
G.add_node("Gen. Marker B (Z2)")
G.add_node("Smoking (X)")
G.add_node("Lung Cancer (Y)")

# Add edges
G.add_edges_from([
    ("Gen. Marker A (Z1)", "Smoking (X)"),
    ("Gen. Marker B (Z2)", "Smoking (X)"),
    ("Smoking (X)", "Lung Cancer (Y)"),
    ("Gen. Marker A (Z1)", "Lung Cancer (Y)"),
    ("Gen. Marker B (Z2)", "Lung Cancer (Y)")
])

# Draw the graph
pos = nx.spring_layout(G)
pos = { 
    "Gen. Marker A (Z1)": (0, 1),
    "Gen. Marker B (Z2)": (1, 0),
    "Smoking (X)": (0, 0),
    "Lung Cancer (Y)": (1,1)
}

nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)
#nx.draw_networkx_edge_labels(G, pos, edge_labels={("Gen. Marker A (Z1)", "Smoking (X)"): "P(X|Z1)=0.4", ("Gen. Marker A (Z1)", "Lung Cancer (Y)"): "P(Y|Z1)=0.2", ("Gen. Marker B (Z2)", "Smoking (X)"): "P(X|Z2)=0.5", ("Gen. Marker B (Z2)", "Lung Cancer (Y)"): "P(Y|Z2)=0.25", ("Smoking (X)", "Lung Cancer (Y)"): "P(Y|X)=0.3 P(Y|¬X)=0.05"})


plt.title("DAG: Smoking, Genetic Markers, and Lung Cancer")
plt.show()