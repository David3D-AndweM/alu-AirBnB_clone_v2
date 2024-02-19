import tarfile

def compress_directory(folder_name):
    output_tar = "copy.tar.gz"
    with tarfile.open(output_tar, "w:gz") as tar:
        tar.add(folder_name)

if __name__ == "__main__":
    folder_name = input("Enter the name of the folder to compress: ")
    compress_directory(folder_name)

