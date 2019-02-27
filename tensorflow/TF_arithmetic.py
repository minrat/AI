import tensorflow as tf

# 创建常量
a = tf.constant(1)
b = tf.constant(2)

# 运算
c = a + b

# 创建会话
ses = tf.Session()

# 利用会话执行目标动作
out = ses.run(c)

# 结果显示
print(out)
