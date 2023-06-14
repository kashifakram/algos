import networkx as nx

def build_flow_network():
    flow_network = nx.DiGraph()

    flow_network.add_edge('source', 'A', capacity=10)
    flow_network.add_edge('source', 'B', capacity=5)
    flow_network.add_edge('A', 'C', capacity=7)
    flow_network.add_edge('A', 'D', capacity=4)
    flow_network.add_edge('B', 'C', capacity=8)
    flow_network.add_edge('B', 'D', capacity=3)
    flow_network.add_edge('C', 'sink', capacity=10)
    flow_network.add_edge('D', 'sink', capacity=6)

    return flow_network

def do_all():
    flow_network = build_flow_network()
    print("Nodes:", flow_network.nodes)
    print("Edges:", flow_network.edges)
    print("Edge capacities:")
    for u, v, attr in flow_network.edges(data=True):
        print(u, "->", v, "Capacity:", attr['capacity'])