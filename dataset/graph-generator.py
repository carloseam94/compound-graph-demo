import json
import networkit as nk


def generate_graph(nodes, density_factor=.2):
    generator = nk.generators.ErdosRenyiGenerator(
        nodes, density_factor, directed=True)
    return generator.generate()


def networkit_communities(G):
    uG = nk.graphtools.toUndirected(G)
    return nk.community.detectCommunities(G, algo=nk.community.PLM(uG, True))


data = []

g = generate_graph(2000, .001)

communities = networkit_communities(g).getVector()

clusters = {}


def iternodes(x):
    if communities[x] in clusters:
        data.append(
            {"data": {"id": x, "name": "ECLI:NL:PHR:2001:AB" + str(x), "parent": clusters[communities[x]]}})
    else:
        data.append(
            {"data": {"id": x, "name": "ECLI:NL:PHR:2001:AB" + str(x)}})
        clusters[communities[x]] = x


def iteredges(x, y, z, u):
    data.append(
        {"data": {"id": str(x) + '_' + str(y), "source": x, "target": y}})


g.forNodes(iternodes)
g.forEdges(iteredges)

print(clusters)

json_graph = json.dumps(data)

with open("./dataset/graph.json", "w") as i:
    json.dump(json_graph, i)
