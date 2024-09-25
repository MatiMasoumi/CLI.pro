import argparse
import os
import shutil
import datetime

LOG_FILE='logs.txt'

def log_command(command ,args ,outcome):
  with open(LOG_FILE ,'a') as log:
    log.write(f'{datetime.datetime.now()}:Command:{command}, Arguments:{args}, Outcome:{outcome}\n')

def list_directory(path='.'):
  try:
    contents = os.listdir(path)
    for item in contents:
      print(item)
    log_command('ls',[path],'Success')
  except Exception as e:
    log_command('ls',[path],f'Error:{e}')
    print(f'Error:{e}')


def change_directory(path):
  try:
    os.chdir(path)
    log_command('cd',[path],'Success')
  except Exception as e:
    log_command('cd',[path],f'Error:{e}')
    print(f'Error:{e}')


def make_directory(path):
  try:
    os.mkdir(path)
    log_command('mkdir',[path],'Success')
  except Exception as e:
    log_command('mkdir',[path],f'Error:{e}')
    print(f'Error:{e}')



def remove_directory(path):
  try:
    os.rmdir(path)
    log_command('rmdir',[path],'Success')
  except Exception as e:
    log_command('rmdir',[path],f'Error:{e}')
    print(f'Error:{e}')


def remove_file(file):
  try:
    os.remove(file)
    log_command('rm',[file],'Success')
  except Exception as e:
    log_command('rm',[file],f'Error:{e}')
    print(f'Error:{e}')
def remove_directory_recursively(directory):
  try:
    shutil.rmtree(directory)
    log_command('rm -r',[directory],'Success')
  except Exception as e:
    log_command('rm -r',[directory],f'Error:{e}')
    print(f'Error:{e}')



def copy(source, destination):
  try:
    if os.path.isdir(source):
      shutil.copytree(source, destination)
    else:
      shutil.copy(source, destination)
    log_command('cp',[source, destination],'Success')
  except Exception as e:
    log_command('cp',[source, destination],f'Error:{e}')
    print(f'Error:{e}')



def move(source, destination):
  try:
    shutil.move(source, destination)
    log_command('mv',[source, destination],'Success')
  except Exception as e:
    log_command('mv',[source, destination],f'Error:{e}')
    print(f'Error:{e}')


def find(path,pattern):
  try:
    for root ,dirs,files in os.walk(path):
      for name in files:
        if pattern in name:
          print(os.path.join(root,name))
      for name in dirs:
        if pattern in name:
            print(os.path.join(root,name))
    log_command('find',[path,pattern],'Success')
  except Exception as e:
    log_command('find',[path,pattern],f'Error:{e}')
    print(f'Error:{e}')



def cat(file):
  try:
    with open(file,'r') as f:
      print(f.read())
    log_command('cat',[file],'Success')
  except Exception as e:
    log_command('cat',[file],f'Error:{e}')
    print(f'Error:{e}')
def main():
  parser = argparse.ArgumentParser(description='Python CLI Tool for file Manipulation')
  subparsers = parser.add_subparsers(dest='command')

  subparsers.add_parser('ls',help='List directory contents').add_argument('path',nargs='?',default='.')
  subparsers.add_parser('cd',help='change directory').add_argument('path',help='Directory path')
  subparsers.add_parser('mkdir',help='Make directory').add_argument('path',help='Directory path')
  subparsers.add_parser('rmdir',help='Remove directory').add_argument('path',help='Directory path')
  subparsers.add_parser('rm',help='Remove file').add_argument('file',help='File path')
  subparsers.add_parser('rm -r',help='Remove directory recursively').add_argument('directory',help='Directory path')

  cp_parser=subparsers.add_parser('cp',help='copy file or directory')
  cp_parser.add_argument('source',help='Source path')
  cp_parser.add_argument('destination',help='Destination path')

  mv_parser=subparsers.add_parser('mv',help='move file or directory')
  mv_parser.add_argument('source',help='Source path')
  mv_parser.add_argument('destination',help='Destination path')

  find_parser=subparsers.add_parser('find',help='find file maching pattern')
  find_parser.add_argument('path',help='Search path')
  find_parser.add_argument('pattern',help='Pattern to search for')

  subparsers.add_parser('cat',help='Output file contents').add_argument('file',help='file path')


  args,unknow=parser.parse_known_args()
  command=args.command

  if command is None:
    print('No command proviced.Use --help for more information.')
    
  if command == 'ls':
    list_directory(args.path if args.path else '.')
  elif command == 'cd':
    change_directory(args.path)
  elif command == 'mkdir':
    make_directory(args.path)
  elif command == 'rmdir':
    remove_directory(args.path)
  elif command == 'rm':
    remove_file(args.file)
  elif command == 'rm -r':
    remove_directory_recursively(args.directory)
  elif command == 'cp':
    copy(args.source, args.destination)
  elif command == 'mv':
    move(args.source, args.destination)
  elif command == 'find':
    find(args.path,args.pattern)
  elif command == 'cat':
    cat(args.file)
  else:
    print('unknow command')
  
if __name__ == '__main__':
  main()