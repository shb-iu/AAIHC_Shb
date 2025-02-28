'''
Created on 23.02.2025
Code for Workbook Inference & Causality Task2
@author: tillschoenbein
'''
import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node("T", label="Time spent on platform")
G.add_node("S", label="User satisfaction")
G.add_node("C", label="Content quality")

# Add edges with probabilities
G.add_edges_from([("T", "S"), ("C", "T"), ("C", "S")])

# Define positions for the nodes
pos = {
    "T": (0, 1),
    "S": (1, 0),
    "C": (0, 0)
}

# Draw the graph
#plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)
nx.draw_networkx_edge_labels(G, pos, edge_labels={("T", "S"): "P(S|T)=0.7", ("C", "T"): "P(T|C)=0.8", ("C", "S"): "P(S|C)=0.6"})

#plt.title("Causal Graph with Probabilities: Time Spent on Platform and User Satisfaction")


# Probabilities
P_C = 0.5  # Prior probability of content quality being high
P_T_given_C = 0.8  # Probability of spending more time given high content quality
P_S_given_T = 0.7  # Probability of user satisfaction given more time spent
P_S_given_C = 0.6  # Probability of user satisfaction given high content quality

# Calculate the total probability of user satisfaction P(S)
P_S = P_S_given_T * P_T_given_C * P_C + P_S_given_C * (1 - P_T_given_C) * P_C

print(f"The total probability of user satisfaction P(S) is {P_S:.2f}.")

# D-separation analysis with probabilities

# Without conditioning on C
P_S_without_conditioning = P_S_given_T * P_T_given_C * P_C + P_S_given_C * (1 - P_T_given_C) * P_C

# With conditioning on C
P_S_with_conditioning = P_S_given_T * P_T_given_C * P_C

print(f"Probability of user satisfaction without conditioning on C: {P_S_without_conditioning:.2f}")
print(f"Probability of user satisfaction with conditioning on C: {P_S_with_conditioning:.2f}")

# Interpretation:
if P_S_without_conditioning != P_S_with_conditioning:
    print("The association between T and S is likely due to the confounding effect of C.")
else:
    print("The association between T and S is likely a direct causal relationship.")
    
plt.show()