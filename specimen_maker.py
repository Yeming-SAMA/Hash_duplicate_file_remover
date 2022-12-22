#此代码用于对指定目录下的所有文件记录文件名和hash并输出至json文件

'''
将文件名和哈希值存储在字典中
使用 json.dump 函数将字典转换为 JSON 并写入文件
'''

import os
import hashlib
import json

# 要搜索的目录
directory = r'x:\xxx'

# 存储文件名和哈希值的字典
data = {}

'''
此步骤只记录普通文件
若需记录目录，可使用 os.path.isdir 函数来检查文件是否是目录
并在必要时递归遍历目录
'''

# 遍历目录中的所有文件和子目录
for root, dirs, files in os.walk(directory):
    # 遍历目录中的所有文件

    for filename in files:
        filepath = os.path.join(root, filename)

        # 计算文件的哈希值
        with open(filepath, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()  
            #可使用hashlib.sha256 或 hashlib.md5 或 hashlib.sha1

        # 将文件名和哈希值添加到字典中
        data[filename] = file_hash

# 将字典转换为 JSON 并写入文件
with open('hashes.json', 'w') as f:
    json.dump(data, f)
