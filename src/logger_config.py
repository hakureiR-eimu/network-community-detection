import logging
import os
from datetime import datetime

# 确保log目录存在
os.makedirs('log',exist_ok=True)

# 配置日志
# 生成唯一的日志文件名
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 当前时间戳
log_file_name = f'app_{timestamp}.log'
log_file_path = os.path.join('log', log_file_name)


logging.basicConfig(
    level=logging.DEBUG,  # 设置日志级别
    format='%(asctime)s - %(levelname)s - %(message)s',  # 日志格式
    handlers=[
        logging.FileHandler(log_file_path,encoding='utf-8'),  # 保存日志到文件
        logging.StreamHandler()  # 打印日志到控制台
    ]
)

logger = logging.getLogger()