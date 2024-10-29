import networkx as nx


def load_data(file_path='input/Cit-HepPh.txt'):
    """
    从指定文件路径记载数据集并构建Networkx图对象,跳过以#开头的注释行。
    :param file_path: 图数据文件路径，默认为'input/Cit-HepPh.txt'
    :return: NetworkX无向图
    """
    G = nx.Graph()

    # 读取文件并添加边
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                # 跳过以#开头的注释行
                if line.startswith('#'):
                    continue

                # 分割出节点
                nodes = line.split()
                if len(nodes) == 2:  # 确保每行有两个节点
                    node1, node2 = int(nodes[0]), int(nodes[1])
                    G.add_edge(node1, node2)
    except FileNotFoundError:
        print(f"文件{file_path}未找到，请确保文件路径正确。")
    except Exception as e:
        print(f"加载数据集时出错误：{e}")
