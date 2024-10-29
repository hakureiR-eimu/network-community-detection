import networkx as nx
from networkx.algorithms.community import girvan_newman


def detect_communities(G, iteration=1):
    """

    :param G: NetworkX图
    :param iteration: 选择第几次迭代后的社区结果，默认为1
    :return list: 每个社区包含的节点列表
    """
    comp = girvan_newman(G)
    for _ in range(iteration - 1):
        next(comp)
    communities = next(comp)
    return [list(community) for community in communities]
