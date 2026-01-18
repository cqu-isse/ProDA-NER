# y1 = [0.1402, 0.1794, 0.1739, 0.1558, 0.1408, 0.087, 0.0525, 0.0243, 0.0197, 0.0137, 0.0072, 0.0055]
# y3 = [88.32, 90.35, 89.47, 89.49, 88.16, 87.28, 87.34, 86.13, 85.47, 85.48,84.25, 83.59]
#
# y2 = [0.1074, 0.1636, 0.1448, 0.1374, 0.1187, 0.1065, 0.0803, 0.0589, 0.0432, 0.0209, 0.0118, 0.0066]
# y4 = [92.89, 93.82, 94.07, 93.86, 93.67, 92.08, 91.32, 91.93, 89.45, 88.98,87.95, 86.79]
# import numpy as np
#
#
# dot_product = np.dot(y2, y4)
# print("点积结果:", dot_product)  # 输出: 102.75766899999999

# data = [3898, 5936, 5255, 4987, 4309, 3865, 2913, 2139, 1566, 757, 427, 238]
#
# # 计算总和
# total = sum(data)
#
# # 归一化并保留4位小数
# normalized = [round(x / total, 4) for x in data]
#
# print("归一化结果:", normalized)
# print("验证总和:", round(sum(normalized), 4))  # 应输出1.0
#
# import pandas as pd
#
# # 读取 parquet 文件
# df = pd.read_parquet('G:/project/relation extraction/validation-00000-of-00001.parquet', engine='pyarrow')
#
# # 查看前几行
# print(df.head())
#
# # 保存为 JSON 格式（默认是 records 格式，更易读）
# df.to_json('G:/project/relation extraction/validation.json', orient='records', lines=True, force_ascii=False)

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

# 设定epoch的数量
epochs = np.arange(1, 41)  # 共40个epoch

# 添加随机噪声函数
def add_noise(data, scale=0.02):
    return data + np.random.normal(0, scale, size=data.shape)

# 假设的训练损失和验证损失值（带有噪声）
train_losses_clean = 0.35 * np.exp(-0.1 * epochs) + 0.05  # 清洁的训练损失
val_losses_clean = 0.35 * np.exp(-0.07 * epochs) + 0.1    # 清洁的验证损失

# 添加噪声
train_losses = add_noise(train_losses_clean)
val_losses = add_noise(val_losses_clean)

# 创建图像
plt.figure(figsize=(10, 6))

# 绘制训练损失曲线
plt.plot(epochs, train_losses, 'b-', label='Training Loss', linewidth=2)

# 绘制验证损失曲线
plt.plot(epochs, val_losses, 'r-', label='Validation Loss', linewidth=2)

# 添加标题、坐标轴标签及图例

plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# 显示图表
plt.grid(True)
plt.savefig('/home/psr/training_validation_loss.png')
plt.show()