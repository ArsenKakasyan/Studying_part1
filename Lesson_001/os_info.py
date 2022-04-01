#собрать информацию об OS

#TODO отправить инфу о системе на GIT
import platform
import sys

os_info = 'OS info is \n {}\n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture())
print(os_info)

with open('os_info.txt', 'w') as ff:
    ff.write(os_info)