#!/usr/bin/python3

class FileSystem():
    class Dir():
        dirs = {}
        files = {}
        number = 0
    
        def __init__(self, number=1):
            self.dirs = {}
            self.files = {}
            self.number = number

    root = Dir()

    def ls(self, path):
        files = []

        if path == "/":
            files = list(self.root.files.keys()) + list(self.root.dirs.keys())
        else:
            p = self.root
            for sub_dir in path.split("/")[1:]:
                p = p.dirs[sub_dir]
            files = list(p.dirs) + list(p.files)
        print(sorted(files))
    
    def mkdir(self, path):
        p = self.root
        for sub_dir in path.split("/")[1:]:
            if sub_dir not in p.dirs:
                p.dirs[sub_dir] = self.Dir()
            p = p.dirs[sub_dir]

    def addContentToFile(self, path, content):
        dirname = path.split("/")[1:-1]
        filename = path.split("/")[-1]
        print(path+" added with contents:")
        print(content)
        p = self.root
        for subdir in dirname:
            p = p.dirs[subdir]
        p.files[filename] = content

    def readContentFromFile(self, path):
        dirname = path.split("/")[1:-1]
        filename = path.split("/")[-1]
        p = self.root
        for subdir in dirname:
            p = p.dirs[subdir]
        print(path+" contents:")
        print(p.files[filename])


def main():
    fs = FileSystem()
    fs.ls("/")
    fs.mkdir("/dir1/dir2")
    fs.mkdir("/dir3/dir4")
    fs.ls("/")
    fs.ls("/dir1")
    fs.addContentToFile("/file1", "hello")
    fs.addContentToFile("/file2", "hello")
    fs.addContentToFile("/dir1/dir2/file3", "hello")
    fs.readContentFromFile("/dir1/dir2/file3")

if __name__ == "__main__":
    main()
