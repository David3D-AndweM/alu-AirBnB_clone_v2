import os
import tarfile
import time

def create_version():
    # Create a folder for versions if it doesn't exist
    versions_folder = 'versions'
    if not os.path.exists(versions_folder):
        os.makedirs(versions_folder)

    # Get the current time to use as the version name
    current_time = time.strftime('%Y%m%d%H%M%S')

    # Define the name of the tar file
    tar_filename = f'{versions_folder}/website_{current_time}.tar.gz'

    # Folder to compress
    repository_folder = '.'  # Assumes the script is run from the repository root

    # Create a tar file and add files from the repository folder
    with tarfile.open(tar_filename, 'w:gz') as tar:
        tar.add(repository_folder, arcname=os.path.basename(repository_folder))

    print(f'Created version: {tar_filename}')

if __name__ == "__main__":
    create_version()

