
import tensorflow as tf
'''
当前AI的发展，CPU处理的事情繁多，伴随GPU的性能大幅提升，参与实际运算。
因此，可选择运算设备： CPU（主流的Intel）、GPU（主流 NVIDIA开发套件）
'''

# 通过tf.device将运算指定到特定的设备上。
# support mode: cpu & gpu
with tf.device('/cpu:0'):
    a = tf.constant([1.0, 2.0, 3.0], shape=[3], name='a')
    b = tf.constant([1.0, 2.0, 3.0], shape=[3], name='b')

with tf.device('/cpu:0'):
     c = a+b

# 通过log_device_placement参数来记录运行每一个运算的设备。
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

# 执行运算
out = sess.run(c)

print(out)


"""
运行结果：
D:\Program Files\Python36\lib\site-packages\h5py\__init__.py:34: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
Device mapping: no known devices.
add: (Add): /job:localhost/replica:0/task:0/device:CPU:0
a: (Const): /job:localhost/replica:0/task:0/device:CPU:0
b: (Const): /job:localhost/replica:0/task:0/device:CPU:0
2019-02-27 17:24:13.247774: I tensorflow/core/common_runtime/direct_session.cc:307] Device mapping:

2019-02-27 17:24:13.249729: I tensorflow/core/common_runtime/placer.cc:927] add: (Add)/job:localhost/replica:0/task:0/device:CPU:0
2019-02-27 17:24:13.250186: I tensorflow/core/common_runtime/placer.cc:927] a: (Const)/job:localhost/replica:0/task:0/device:CPU:0
2019-02-27 17:24:13.250642: I tensorflow/core/common_runtime/placer.cc:927] b: (Const)/job:localhost/replica:0/task:0/device:CPU:0
[2. 4. 6.]
"""
