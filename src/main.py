import networkx as nx
from networkx.algorithms.community import girvan_newman

# 创建一个示例图
G = nx.Graph()
edges = [
    (1, 2), (2, 3), (3, 4), (4, 5),
    (5, 1), (1, 3), (3, 5), (2, 4)
]
G.add_edges_from(edges)

# 使用Girvan-Newman算法发现社区
def find_communities(graph):
    comp = girvan_newman(graph)
    limited = next(comp)  # 获取第一次迭代的社区划分结果
    communities = [list(community) for community in limited]
    return communities

# 调用函数并打印社区划分结果
communities = find_communities(G)
print("发现的社区划分：")
for i, community in enumerate(communities, 1):
    print(f"社区 {i}: {community}")
