import Module.basic, Module.advanced ##Package안의 모듈 Import
a = 10
b = 20
Module.basic.add(a, b)
Module.advanced.mul(a, b)

import Module ## __init__.py 실행된다.
Module.basic.add(a, b)
Module.advanced.mul(a, b)

from Module import *
basic.add(a, b)
## advanced.mul(a,b ) __init__.py에 추가되지 않았기 때문에 Error

