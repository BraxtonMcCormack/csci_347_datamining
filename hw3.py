from itertools import combinations
from collections import Counter, defaultdict, deque
from matplotlib import pyplot as plt


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_shortest_path(self, start, goal):
        """Find the shortest path using BFS"""
        if start == goal:
            return [start]
        visited = {start}
        queue = deque([(start, [start])])
        while queue:
            current, path = queue.popleft()
            for neighbor in self._graph[current]:
                if neighbor not in visited:
                    if neighbor == goal:
                        return path + [neighbor]
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def closeness_centrality(self, nodes):
        """Calculate the closeness centrality for specified nodes"""
        centrality = {}
        for node in nodes:
            sum_of_distances = sum(len(self.find_shortest_path(node, other)) - 1
                                   for other in self._graph if other != node)
            centrality[node] = 1 / sum_of_distances if sum_of_distances > 0 else 0
        return centrality

    def eccentricity(self, vertex):
        """Calculate the eccentricity of a given vertex"""
        max_distance = 0
        for other in self._graph:
            if other != vertex:
                path = self.find_shortest_path(vertex, other)
                if path:
                    distance = len(path) - 1
                    max_distance = max(max_distance, distance)
                else:
                    # Assuming infinity for disconnected components
                    return float('inf')
        return max_distance
    

    def find_all_paths(self, start, goal):
        """Find all paths between start and goal (not just the shortest)"""
        if start == goal:
            return [[start]]
        paths = []
        queue = deque([(start, [start])])
        while queue:
            (vertex, path) = queue.popleft()
            for next in set(self._graph[vertex]) - set(path):
                if next == goal:
                    paths.append(path + [next])
                else:
                    queue.append((next, path + [next]))
        return paths

    def betweenness_centrality(self, vertices):
        """Calculate the betweenness centrality for specific vertices"""
        centrality = dict.fromkeys(vertices, 0.0)
        for start in self._graph:
            for goal in self._graph:
                if start != goal:
                    all_paths = self.find_all_paths(start, goal)
                    total_paths = len(all_paths)
                    if total_paths > 0:
                        for vertex in vertices:
                            paths_through_vertex = sum(vertex in path for path in all_paths)
                            centrality[vertex] += paths_through_vertex / total_paths
        # Optionally, normalize the centrality values here
        return centrality
    
    def find_shortest_path_length(self, start, goal):
        """Find the shortest path length using BFS"""
        if start == goal:
            return 0
        visited = set([start])
        queue = deque([(start, 0)])
        while queue:
            (current, distance) = queue.popleft()
            for neighbor in self._graph[current]:
                if neighbor not in visited:
                    if neighbor == goal:
                        return distance + 1
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
        return float('inf')  # Return infinity if no path exists

    def average_shortest_path_length(self):
        """Calculate the average shortest path length in the graph"""
        path_lengths = []
        for (start, goal) in combinations(self._graph, 2):
            path_length = self.find_shortest_path_length(start, goal)
            if path_length != float('inf'):
                path_lengths.append(path_length)

        if path_lengths:
            return sum(path_lengths) / len(path_lengths)
        else:
            return 0
        
    def plot_degree_distribution(self):
        """Plot the degree distribution of the graph"""
        degrees = [len(self._graph[node]) for node in self._graph]
        degree_counts = Counter(degrees)
        fig, ax = plt.subplots()
        ax.bar(degree_counts.keys(), degree_counts.values(), color='b')

        ax.set_xlabel('Degree')
        ax.set_ylabel('Number of vertices')
        ax.set_title('Degree distribution of the graph')

        plt.show()

    def clustering_coefficient(self, vertex):
        """Calculate the clustering coefficient for a given vertex"""
        neighbors = self._graph[vertex]
        if len(neighbors) < 2:
            return 0.0  # No triangle is possible
        possible_links = len(neighbors) * (len(neighbors) - 1) / 2
        actual_links = 0
        for v1 in neighbors:
            for v2 in neighbors:
                if v1 != v2 and v2 in self._graph[v1]:
                    actual_links += 1
        # Each edge is counted twice (v1,v2) and (v2,v1)
        actual_links /= 2
        return actual_links / possible_links
    
    def average_clustering_coefficient(self):
        """Calculate the average clustering coefficient of the graph"""
        total_clustering = 0.0
        for vertex in self._graph:
            total_clustering += self.clustering_coefficient(vertex)
        return total_clustering / len(self._graph) if self._graph else 0

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
    
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
g = Graph(connections, directed=False)

#question 1
specific_nodes_centrality = g.closeness_centrality(nodes=['3', '12'])
print(f"Closeness centrality for nodes 3 and 12: {specific_nodes_centrality}")  #currently wrong
#question 2
eccentricity_of_vertex_3 = g.eccentricity('3')
print(f"Eccentricity of vertex 3: {eccentricity_of_vertex_3}")
eccentricity_of_vertex_12 = g.eccentricity('12')
print(f"Eccentricity of vertex 12: {eccentricity_of_vertex_12}")
eccentricity_of_vertex_11 = g.eccentricity('11')
print(f"Eccentricity of vertex 11: {eccentricity_of_vertex_11}")
#question 3
specific_vertices_centrality = g.betweenness_centrality(['3', '12'])
print(f"Betweenness centrality for vertices 3 and 12: {specific_vertices_centrality}")  #currently wrong
#question 5
average_length = g.average_shortest_path_length()
print(f"Average shortest path length: {average_length}")
#question 6, commented out because it stops the code until I close it and am lazy
g.plot_degree_distribution()
#question 7
clustering_coefficient_of_vertex_3 = g.clustering_coefficient('3')
print(f"Clustering coefficient of vertex 3: {clustering_coefficient_of_vertex_3}")
#question 8
average_clustering = g.average_clustering_coefficient()
print(f"Average clustering coefficient: {average_clustering}")