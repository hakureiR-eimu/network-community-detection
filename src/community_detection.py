# community_detection.py

import networkx as nx
from logger_config import logger


def detect_communities(G, iteration=10):
    """
    使用Girvan-Newman算法检测社区。

    参数：
    G - 输入图（NetworkX图对象）
    iteration - 迭代次数（用于多次检测）

    返回：
    communities - 检测到的社区
    """
    logger.info("开始检测社区...")

    # 输出图的基本信息
    logger.info(f"图的节点数: {G.number_of_nodes()}")
    logger.info(f"图的边数: {G.number_of_edges()}")

    # 初始检测社区
    initial_communities = list(nx.connected_components(G))
    logger.info(f"初始检测到的社区数: {len(initial_communities)}")

    # 使用Girvan-Newman算法
    comp = nx.community.girvan_newman(G)

    # 迭代获取社区
    for i in range(iteration):
        logger.info(f"第 {i + 1} 次迭代开始...")

        # 获取当前的社区划分
        communities = next(comp)

        logger.info(f"第 {i + 1} 次迭代检测到的社区数: {len(communities)}")

        # 如果社区数目增加，则记录
        if len(communities) > len(initial_communities):
            initial_communities = communities
            logger.info(f"社区数目增加到: {len(initial_communities)}")
        else:
            logger.info("社区数目没有增加，停止迭代。")
            break

    logger.info("社区检测完成。")
    return initial_communities
