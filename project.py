import argparse 
# import pathlib
from pathlib import Path

def main():
	# args = get_args()
	# print(vars(get_args()))
	args = get_args()

	path = args.path
	print(path)

	if args.type == 'movie':
		handle_movies()
	else:
		handle_shows()


def handle_movies():
	...

def handle_shows():
	...

def get_args():
	parser = argparse.ArgumentParser(prog='project',
				description='Rename files for Plex use',)

	parser.add_argument('path',
			type=str,
			help='the path to the files')

	# parser.add_argument('Library',
	# 		metavar='library_path',
	# 		type=str,
	# 		help='the path where the files should be stored after renaming')

	parser.add_argument('-l', '--library', 
			metavar='library_type',
			type=str,
			choices=['tv', 'movie'],
			default='movie',
			help='The type of media (tv show or movie)',
			dest='type')

	# args = parser.parse_args()
	return parser.parse_args()


if __name__ == '__main__':
	main()