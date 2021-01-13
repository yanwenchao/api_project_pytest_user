"""
==================
Author: 严文超
2020/12/4 15:18
==================
"""

import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 公共方法目录路径
COMMON_DIR = os.path.join(BASE_DIR,"common_tools")

# 配置文件目录路径
CONFIG_DIR = os.path.join(BASE_DIR,"config_files")

# 数据文件目录路径
DATA_DIR = os.path.join(BASE_DIR,"data")

# 日志文件目录路径
LOGS_DIR = os.path.join(BASE_DIR,"logs")

# 测试报告文件目录路径
REPORTS_DIR = os.path.join(BASE_DIR,"reports")

# 测试用例文件目录路径
CASE_DIR = os.path.join(BASE_DIR,"test_cases")