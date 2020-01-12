from os.path import exists, isdir, split, splitext, join
from platform import system


def name_dupe(path):
    """
        Renames the file or directory until it doesn't exist
        in the destination with that name anymore, by appending
        the filename with an index wrapped in parenthesis.
        (Windows platforms)

        file.txt => file (1).txt => file (2).txt
    """

    if system() != "Windows":
        raise OSError("For use with Windows filesystems.")

    path_ = path
    (root, filename) = split(path_)

    if isdir(path_):
        title=filename
        ext = None
    else:
        (title, ext)=splitext(filename)

    filecount=0
    while exists(path_):
        filecount += 1
        new_title=title + " (" + str(filecount) + ")"
        if ext:
            new_title = new_title + ext
        path_ = join(root, new_title)
    
    return path_
