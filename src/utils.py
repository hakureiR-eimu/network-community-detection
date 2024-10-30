import os


def print_communities(communities):
    """
    格式化输出社区划分结果。
    :param communities:
    :return:
    """
    for i, community in enumerate(communities, 1):
        print(f"社区{i}:{community}")


def save_communities(partition, output_dir="output", filename="communities.output"):
    """
    保存 Louvain 算法生成的社区结果到指定文件夹。

    参数:
    - partition (dict): Louvain 算法生成的节点到社区的映射，格式 {节点: 社区编号}.
    - output_dir (str): 保存结果的文件夹路径，默认为 "output".
    - filename (str): 输出文件的名称，默认为 "communities.txt".
    """
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 构建输出文件的完整路径
    output_path = os.path.join(output_dir, filename)

    # 将社区划分结果写入文件
    with open(output_path, "w") as f:
        for node, community in partition.items():
            f.write(f"{node}\t{community}\n")

    print(f"Community structure saved to {output_path}")
