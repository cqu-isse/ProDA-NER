# import matplotlib.pyplot as plt
# import numpy as np
#
# # 数据准备
# x = list(range(1, 13))
# y1 = [3142, 4021, 3898, 3493, 3156, 1950, 1176, 544, 442, 308, 162, 124]
# y2 = [3898, 5936, 5255, 4987, 4309, 3865, 2913, 2139, 1566, 757, 427, 238]
# y3 = [88.32, 90.35, 89.47, 88.79, 88.16, 87.28, 87.34, 86.13, 85.47, 85.48,84.25, 83.59]
# y4 = [92.89, 93.82, 94.57, 93.86, 93.07, 92.08, 91.32, 91.93, 89.45, 88.98,87.95, 86.79]
# # 创建画布和子图
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
#
# # 第一幅柱状图
# ax1.bar(x, y1, color='skyblue', edgecolor='black')
#
# ax1.set_xlabel('Entity Length - Original', fontsize=12)
# ax1.set_ylabel('Frequency', fontsize=12)
# ax1.set_xticks(x)
# ax1.grid(axis='y', linestyle='--', alpha=0.7)
#
# # 第二幅柱状图
# ax2.bar(x, y2, color='lightsalmon', edgecolor='black')
#
# ax2.set_xlabel('Entity Length - Augmented', fontsize=12)
# ax2.set_ylabel('Frequency', fontsize=12)
# ax2.set_xticks(x)
# ax2.grid(axis='y', linestyle='--', alpha=0.7)
#
# # 添加数据标签
# for i, v in enumerate(y1):
#     ax1.text(i+1, v+50, str(v), ha='center')
# for i, v in enumerate(y2):
#     ax2.text(i+1, v+50, str(v), ha='center')
#
# plt.savefig("G:/桌面/bar_chart.png")
# # 调整布局
# plt.tight_layout()
# plt.show()







import matplotlib.pyplot as plt
import numpy as np

# 数据准备
x = list(range(1, 13))
y1_f1 = [88.32, 90.35, 89.47, 88.09, 88.16, 87.28, 87.34, 86.13, 85.47, 85.48, 84.25, 83.59]
y1_precision = [89.74, 92.11, 91.01, 91.72, 90.64, 88.69, 88.63, 87.74, 87.86, 87.07, 85.58, 84.12]
y1_recall = [86.92, 88.63, 87.96, 84.74, 85.81, 85.89, 86.07, 84.54, 83.21, 83.91, 82.94, 83.06]

y2_f1 = [92.89, 93.82, 94.07, 93.86, 93.67, 92.08, 91.32, 91.93, 89.45, 88.98, 87.95, 86.79]
y2_precision = [93.91, 95.38, 95.41, 95.29, 94.06, 93.39, 92.56, 93.58, 91.29, 91.67, 89.08, 88.17]
y2_recall = [91.89, 92.28, 92.77, 92.44, 93.26, 90.79, 90.08, 90.30, 87.63, 86.45, 86.83, 85.42]

# 创建画布和子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# 颜色定义 - 红蓝橙配色方案
colors = {
    'f1': '#E63946',    # 红色
    'precision': '#87CEFA',  # 浅天蓝
    'recall': '#F77F00'   # 橙色
}

# 第一幅折线图（原始数据）
ax1.plot(x, y1_f1, marker='o', color=colors['f1'], linewidth=2, markersize=6, label='F1')
ax1.plot(x, y1_precision, marker='^', color=colors['precision'], linewidth=2, markersize=6, label='Precision')
ax1.plot(x, y1_recall, marker='s', color=colors['recall'], linewidth=2, markersize=6, label='Recall')

ax1.set_xlabel('Entity Length', fontsize=12)
ax1.set_ylabel('Score (%)', fontsize=12)
ax1.set_xticks(x)
ax1.set_ylim(80, 95)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(loc='lower left')

# 第二幅折线图（增强数据）
ax2.plot(x, y2_f1, marker='o', color=colors['f1'], linewidth=2, markersize=6, label='F1')
ax2.plot(x, y2_precision, marker='^', color=colors['precision'], linewidth=2, markersize=6, label='Precision')
ax2.plot(x, y2_recall, marker='s', color=colors['recall'], linewidth=2, markersize=6, label='Recall')

ax2.set_xlabel('Entity Length', fontsize=12)
ax2.set_ylabel('Score (%)', fontsize=12)
ax2.set_xticks(x)
ax2.set_ylim(82, 97)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.legend(loc='lower left')

# 调整布局并保存
plt.tight_layout()
plt.savefig("G:/桌面/metrics_comparison.png", dpi=300, bbox_inches='tight')
plt.show()