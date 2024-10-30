import os

from data_loader import load_data
from community_detection import detect_communities
from utils import save_communities


def main():
    # 加载数据集
    G = load_data()
    if G is None:
        print("图加载失败")
        return

    communities = detect_communities(G, iteration=1)

    # 创建 output 文件夹（如果不存在）
    if not os.path.exists('output'):
        os.makedirs('output')

    # 输出社区划分结果
    save_communities(communities)


if __name__ == "__main__":
    main()
