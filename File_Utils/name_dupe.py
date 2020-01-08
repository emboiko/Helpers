from os.path import exists, isdir, split, join

def name_dupe(future_destination):
    """
        Renames the file or directory (by reference) until it doesn't exist
        in the destination with that name anymore, by appending
        the filename with an index wrapped in parenthesis.
    """

    if isdir(future_destination):
        (root, filename)=split(future_destination)
        new_title=filename

        filecount=0
        while exists(future_destination):
            filecount += 1
            new_title=filename + " (" + str(filecount) + ")"
            future_destination=join(root, new_title)
        
        return new_title

    else:
        (root, filename)=split(future_destination)
        (title, ext)=splitext(filename)
        new_title=title

        filecount=0
        while exists(future_destination):
            filecount += 1
            new_title=title + " (" + str(filecount) + ")"
            future_destination=join(root, new_title + ext)
        
        return new_title + ext
