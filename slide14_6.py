import os
path = '/Users/xsash/Desktop/Python/'
def Test2(path):
    for lists in os.listdir(path):
        rootDir = os.path.join(path, lists)
        print(rootDir)
        if os.path.isdir(rootDir):
            Test2(rootDir)

if __name__ == "__slide14_6__":
    print(Test2(path))