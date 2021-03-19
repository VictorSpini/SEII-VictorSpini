# OS Module - Use Underlying Operating System Functionality

import datetime
import os

# print(dir(os))
# print(os.getcwd())
os.chdir('/home/Spini/Documentos/SistEmbarcados/Semana02')
# print(os.getcwd())

# os.mkdir('OS-demo/Sub-Dir')
# os.makedirs('OS-demo/Sub-Dir')
# os.removedirs('OS-demo/Sub-Dir')

# os.rename('test.txt', 'demo.txt')
# print(os.listdir())

# print(os.stat('demo.txt'))
# print(os.stat('demo.txt').st_size)
# print(os.stat('demo.txt').st_mtime)

# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

# for dirpath, dirnames, filenames in os.walk(
#         '/home/Spini/Documentos/SistEmbarcados/Semana02'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('File:', filenames)
#     print()

# print(os.environ.get('HOME'))

# file_path = os.path.join(os.environ.get('HOME'), 'demo.txt')
# print(file_path)

print(os.path.basename('/tmp/demo.txt'))
print(os.path.dirname('/tmp/demo.txt'))
print(os.path.split('/tmp/demo.txt'))
print(os.path.exists('/tmp/demo.txt'))
print(os.path.splitext('/tmp/demo.txt'))
print(dir(os.path))
