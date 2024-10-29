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

    # 输出社区划分结果
    print("发现的社区划分：")
    print_communities(communities)


if __name__ == "__main__":
    main()
