import networkx as nx
import matplotlib.pyplot as plt

# Define the connections
connections = [
    ('1', '2'), ('1', '3'),
    ('2', '3'),
    ('3', '4'), ('3', '5'), ('3', '12'),
    ('4', '5'),
    ('5', '11'),
    ('6', '7'), ('6', '12'),
    ('7', '12'),
    ('8', '12'),
    ('9', '12'),
    ('10', '12'),
    ('11', '12')
]

# Create a graph
G = nx.Graph()

# Add connections
G.add_edges_from(connections)

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15)
plt.show()


# Calculate the closeness centrality of vertices 3 and 12
closeness_centrality = nx.closeness_centrality(G)
closeness_3 = closeness_centrality['3']
closeness_12 = closeness_centrality['12']

# Calculate the eccentricity of vertices 3, 12, and 11
eccentricity = nx.eccentricity(G)
eccentricity_3 = eccentricity['3']
eccentricity_12 = eccentricity['12']
eccentricity_11 = eccentricity['11']

# Calculate the betweenness centrality of vertices 3 and 12
betweenness_centrality = nx.betweenness_centrality(G)
betweenness_3 = betweenness_centrality['3']
betweenness_12 = betweenness_centrality['12']

# Calculate the eigenvector centrality of vertices 3 and 12
eigenvector_centrality = nx.eigenvector_centrality(G)
eigenvector_3 = eigenvector_centrality['3']
eigenvector_12 = eigenvector_centrality['12']

# Calculate the average length of the shortest path between two vertices in the graph
average_shortest_path_length = nx.average_shortest_path_length(G)

# Calculate the degree distribution
degrees = [degree for node, degree in G.degree()]
degree_distribution = plt.hist(degrees, bins=range(min(degrees), max(degrees) + 2), align='left')

# Calculate the clustering coefficient of vertex 3
clustering_coefficient_3 = nx.clustering(G, '3')

# Calculate the clustering coefficient of the graph
average_clustering_coefficient = nx.average_clustering(G)

#question 1
print(f'"closeness_centrality_3": {closeness_3}')
print(f'"closeness_centrality_12": {closeness_12}')
#question 2
print(f'"eccentricity_3": {eccentricity_3}')
print(f'"eccentricity_12": {eccentricity_12}')
print(f'"eccentricity_11": {eccentricity_11}')
#quesiton 3
print(f'"betweenness_centrality_3": {betweenness_3}')
print(f'"betweenness_centrality_12": {betweenness_12}')
#question 4
print(f'"eigenvector_centrality_3": {eigenvector_3}')
print(f'"eigenvector_centrality_12": {eigenvector_12}')
#question 5
print(f'"average_shortest_path_length": {average_shortest_path_length}')
#question 7
print(f'"clustering_coefficient_3": {clustering_coefficient_3}')
#question 8
print(f'"average_clustering_coefficient": {average_clustering_coefficient}')