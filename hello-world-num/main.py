import argparse

parser = argparse.ArgumentParser(description='HelloWorld Tutorial')
parser.add_argument('--num', default=1, type=int, help='input num')
args = parser.parse_args()

print(f"HelloWorld{args.num}")