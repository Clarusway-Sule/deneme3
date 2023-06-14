def listfolderpaths(path=os.getcwd()):
        folderlist = []
        for name in os.listdir(path):
            pathname = os.path.join(path, name)
            if not is_private(name) and os.path.isdir(pathname):
                folderlist.append(pathname)
        return folderlist
degiisklik yapmam istendi.. burada kucuk bir degisiklik yapiyorum..
def listfolderpaths(path=os.getcwd()):
    return [os.path.join(path, name) for name in os.listdir(path) if (not is_private(name) and os.path.isdir(os.path.join(path, name)))]

def listfilepaths(path=os.getcwd()):
    return [os.path.join(path, name) for name in os.listdir(path) if (not is_private(name) and os.path.isfile(os.path.join(path, name)))]

def list_files(image_dir, pattern):
    return [image for image in glob.glob(osp.join(image_dir, pattern))]
def list_files(image_dir, pattern):
    return [image for image in glob.glob(osp.join(image_dir, pattern))]
def list_files(image_dir, pattern):
    return [image for image in glob.glob(osp.join(image_dir, pattern))]
def list_files(image_dir, pattern):
    return [image for image in glob.glob(osp.join(image_dir, pattern))]

list_images(r"C\Users\Picture", ".jpg")

