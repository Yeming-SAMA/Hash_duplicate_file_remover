#此代码用于基于sample_maker_GPT.py生成的json对指定目录进行遍历并删除符合的文件
'''
由ChatGPT生成的帮助内容
在这个程序中，我们使用 os.walk 函数遍历目录中的所有文件和子目录
我们使用 hashlib.sha256 函数计算文件的哈希值
然后与 hashes.json 中的值进行比较
如果文件名和哈希值与 hashes.json 中的值完全匹配，则打印文件路径。

请注意，这个程序同时考虑了普通文件和目录
如果您希望这个程序只考虑普通文件
您可以使用 os.path.isfile 函数来检查文件是否是普通文件。
'''


import os
import hashlib
import json

# 要搜索的目录
directory = r'x:\x'

# 读取 hashes.json 文件
with open('hashes.json', 'r') as f:
    hashes = json.load(f)

# 遍历目录中的所有文件和子目录
for root, dirs, files in os.walk(directory):
    # 遍历目录中的所有文件
    for filename in files:
        filepath = os.path.join(root, filename)

        # 如果文件名和哈希值与 hashes.json 中的值完全匹配，则打印文件路径
        if filename in hashes and hashlib.sha256(open(filepath, 'rb').read()).hexdigest() == hashes[filename]:
            print(filepath)
            os.remove(filepath)



