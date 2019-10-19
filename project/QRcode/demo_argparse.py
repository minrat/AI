import os
import argparse
argparser = argparse.ArgumentParser()
argparser.add_argument('content', help='内容')
argparser.add_argument('-v', '--version', type=int, choices=range(1, 41), default=1, help='版本')
argparser.add_argument('-l', '--level', choices=list('LMQH'), default='H', help='级别')
argparser.add_argument('-p', '--picture', help='背景图片')
argparser.add_argument('-c', '--colorized', action='store_true', help="")
argparser.add_argument('-con', '--contrast', type=float, default=1.0, help='对比度')
argparser.add_argument('-b', '--brightness', type=float, default=1.0, help='明亮度')
argparser.add_argument('-n', '--name', help="名称")
argparser.add_argument('-d', '--directory', default=os.getcwd(), help='输出位置')
args = argparser.parse_args()
