# Method-A: 传统方法
print("Hello,I am from vipJr")

# Method-B: tensorflow
# 引入工具包
import tensorflow as tf
# 创建常量
hello = tf.constant("Hello,TensorFlow, I am from vipJr")
# 创建会话
sess = tf.Session()
# 利用会话执行
print(sess.run(hello))

