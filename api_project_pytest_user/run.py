"""
==================
Author: 严文超
2020/12/16 14:57
==================
"""
import os
import pytest

# pytest.main(['-v','-s'])

# 1、生成allure报告数据到指定路径reports;
pytest.main(["--alluredir=result/reports",'-v'])

# 2、 启动allure服务
os.system('allure serve result/reports')