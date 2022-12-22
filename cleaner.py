#此代码用于基于 specimen_maker.py 生成的json对指定目录进行遍历并删除符合的文件

import os
import hashlib
import json

# 要搜索的目录
directory = r'x:\x'

# 读取 hashes.json 文件
with open('hashes.json', 'r') as f:
    hashes = json.load(f)

'''
此步骤同时处理普通文件和目录
若需此步骤只处理普通文件
可使用 os.path.isfile 函数来检查文件是否是普通文件。
'''

# 遍历目录中的所有文件和子目录
for root, dirs, files in os.walk(directory):
    # 遍历目录中的所有文件
    for filename in files:
        filepath = os.path.join(root, filename)

        # 若文件名和哈希值与 hashes.json 中的值完全匹配，则输出文件路径并删除
        # 可使用hashlib.sha256 或 hashlib.md5 或 hashlib.sha1
        if filename in hashes and hashlib.sha256(open(filepath, 'rb').read()).hexdigest() == hashes[filename]:
            print(filepath)
            os.remove(filepath)



