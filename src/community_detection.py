# community_detection.py
import logging
from collections import defaultdict

import networkx as nx
import community as community_louvain
from logger_config import logger
import time

def log_communities(partition):
    """
    检测社区的数量并记录每个社区的节点数量。

    参数:
    - partition (dict): 节点到社区的映射，格式 {节点: 社区编号}.
    """

    # 统计每个社区中的节点
    community_nodes = defaultdict(list)
    for node, community in partition.items():
        community_nodes[community].append(node)

    # 计算社区数量
    num_communities = len(community_nodes)
    logger.info(f"社区总数: {num_communities}")
    # print(f"Total number of communities: {num_communities}")

    # 记录每个社区的节点数量
    for community, nodes in community_nodes.items():
        community_size = len(nodes)
        logger.info(f"社区： {community} 拥有 {community_size} 节点")
        # print(f"Community {community} has {community_size} nodes")
def detect_communities(G, iteration=1):
    """
    使用Girvan-Newman算法检测社区。

    参数：
    G - 输入图（NetworkX图对象）
    iteration - 迭代次数（用于多次检测）

    返回：
    communities - 检测到的社区
    """
    start_time = time.time()
    logger.info("开始检测社区...")

    # 输出图的基本信息
    logger.info(f"图的节点数: {G.number_of_nodes()}")
    logger.info(f"图的边数: {G.number_of_edges()}")

    # 初始检测社区
    initial_communities = list(nx.connected_components(G))
    logger.info(f"初始检测到的社区数: {len(initial_communities)}")

    # 使用Girvan-Newman算法
    partition = community_louvain.best_partition(G)

    logger.info("社区检测完成。")
    log_communities(partition)
    end_time = time.time()
    run_time = end_time-start_time
    logging.info(f"算法总时间:{run_time:.2f} seconds")
    return partition
