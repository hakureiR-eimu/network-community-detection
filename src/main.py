import os

from data_loader import load_data
from community_detection import detect_communities
from utils import print_communities


def main():
    # 加载数据集
    G = load_data()
    if G is None:
        print("图加载失败")
        return
    # 检测社区，选择第10次迭代的结果
    communities = detect_communities(G, iteration=1)

    # 创建 output 文件夹（如果不存在）
    if not os.path.exists('output'):
        os.makedirs('output')

    # 输出社区划分结果
    print("发现的社区划分：")
    print_communities(communities)
    # 将社区集合写入文件
    output_file = 'output/communities.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, community in enumerate(communities):
            f.write(f"Community {i + 1}: {', '.join(map(str, community))}\n")


if __name__ == "__main__":
    main()
