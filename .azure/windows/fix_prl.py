import glob, fnmatch, os, sys, re

if len(sys.argv) < 3:
    print('Not enough parameters!')
    sys.exit();

os.chdir(sys.argv[1])

libs = []

for subpath in sys.argv[2:]:
    libs += glob.glob(subpath + '/**/libQt*.a', recursive=True) + \
        glob.glob(subpath + '/**/libq*.a', recursive=True)

print("Libs:")
print(libs)
print("+"*50)

for subpath in sys.argv[2:]:
    for filename in glob.glob(subpath + '/*.prl'):
        print("For file: {}".format(filename))
        with open(filename, 'r') as file:
            file_content = file.read()
            new_content = re.sub(r'(?m)^QMAKE_PRL_BUILD_DIR.*\n?', '', file_content)
            for lib in libs:
                lib_name = lib.split('/')[-1].split('.')[0]
                new_content = re.sub(
                    r'\s((\/|\/\S*\/)' + lib_name + '\.a)+',
                    ' ' + sys.argv[1] + '/' + lib,
                    new_content,
                )
                print("        :", lib)
                print("        :", lib_name)
                print("        :", r'\s(\/' + lib_name + '\.a)+')
                print("        :", ' ' + sys.argv[1] + '/' + lib)
                print("="*60)
                print(new_content)
                print("="*60)
        with open(filename, 'w') as file:
            file.write(new_content)
