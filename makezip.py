import zipfile
import os
# 这是用来打包发布文件的，会提前删掉已有的打包文件，然后 collectstatic ，后进行打包
file_name = "plasrefine.zip"
try:
    os.remove(os.getcwd() + file_name)
    # os.remove(os.getcwd() + "/new.zip")
except:
    print("已删除")


# zip_file = zipfile.ZipFile('new.zip', 'w')
# 格式化文件大小
def size_format(size):
    if size < 1024:
        return '%i' % size + 'size'
    elif 1024 <= size < 1024000:
        return '%.1f' % float(size / 1024) + 'KB'
    elif 1024000 <= size < 1024000000:
        return '%.1f' % float(size / 1024000) + 'MB'
    elif 1024000000 <= size < 1024000000000:
        return '%.1f' % float(size / 1024000000) + 'GB'
    elif 1024000000000 <= size:
        return '%.1f' % float(size / 1024000000000) + 'TB'


# 传入列表，输出压缩包
def my_zip(zipfile_name, file_list):
    with zipfile.ZipFile(zipfile_name, 'w') as target:
        # 遍历列表
        for i in file_list:
            # 处理单独文件
            if os.path.isfile(os.getcwd() + "\\" + i):
                # print(i + "is file")
                target.write(i, compress_type=zipfile.ZIP_DEFLATED)
            else:
                # 处理文件夹
                # print(i + "not a file")
                for j in os.walk(i):
                    for n in j[2]:
                        target.write(''.join((j[0], '\\', n)))
                        # windows路径
    print('打包完成', file_name, size_format(os.path.getsize(zipfile_name)))


# python manage.py collectstatic
val = os.system(
    'C:\\Users\\FANJINGHUA\\PycharmProjects\\plasrefine_backstage\\venv\\Scripts\\activate && python C:\\Users\\FANJINGHUA\\PycharmProjects\\plasrefine_backstage\\manage.py collectstatic --noinput')
print(val)
# source /home/haomingc/virtualenv/test3/3.7/bin/activate && cd /home/haomingc/test3

# # 把zfile整个目录下所有内容，压缩为new.zip文件
# # 把c.txt文件压缩成一个压缩文件
# zip_file.write('requirements.txt', compress_type=zipfile.ZIP_DEFLATED)
# zip_file.write('manage.py', compress_type=zipfile.ZIP_DEFLATED)
# # zip_file.write('web', compress_type=zipfile.ZIP_DEFLATED)
# with zipfile.ZipFile('aa.zip', 'w') as target:
#     for i in os.walk('web'):
#         for n in i[2]:
#             target.write(''.join((i[0], '\\', n)))
#             # windows路径
# zip_file.close()
my_zip(file_name,
       ['requirements.txt', 'manage.py', 'web', 'media', 'plasrefine_backstage', 'db.sqlite3', 'static'])
