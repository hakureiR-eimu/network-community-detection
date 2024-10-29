def print_communities(communities):
    """
    格式化输出社区划分结果。
    :param communities:
    :return:
    """
    for i, community in enumerate(communities, 1):
        print(f"社区{i}:{community}")

