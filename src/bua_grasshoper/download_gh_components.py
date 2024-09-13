import os
import shutil
import urllib.request
from pkg_resources import resource_filename
from zipfile import ZipFile

# todo: imoprt bua.config as bua_config

# Path in the user computer

# Path to the Grasshopper components zip file in the repository
gh_components_url = ""

def download_file_from_github(repo, tag, file_path, target_location):
    """
    Downloads a ZIP file from a GitHub repository release and saves it to the target location.

    :param repo: GitHub repository in 'owner/repo' format
    :param tag: Release tag to fetch the file from
    :param file_path: Path to the ZIP file in the repository
    :param target_location: Local directory to save the downloaded ZIP file
    """
    # Construct the URL for the raw file download
    url = f'https://github.com/{repo}/releases/download/{tag}/{file_path}'
    dst = os.path.join(target_location, os.path.basename(file_path))

    # Download the ZIP file
    try:
        print(f"Downloading {file_path} from {url}...")
        urllib.request.urlretrieve(url, dst)
        print(f"Downloaded {file_path} to {dst}")

        # Unzip the downloaded file if it is a ZIP file
        if dst.lower().endswith('.zip'):
            unzip_file(dst, target_location)
    except Exception as e:
        print(f"Failed to download {file_path} from {url}. Error: {e}")


def unzip_file(zip_path, extract_to):
    """
    Unzips a ZIP file to the specified directory.

    :param zip_path: Path to the ZIP file
    :param extract_to: Directory to extract the contents to
    """
    print(f"Unzipping {zip_path} to {extract_to}...")

    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    print(f"Extraction complete. Contents extracted to {extract_to}")


def copy_package_files(target_location):
    """
    Copies specified files from the package to the target location.

    :param target_location: Directory to copy the files to
    """
    # Define the files to copy from the package
    files_to_copy = [
        'data/file1.txt',
        'data/file2.txt',
    ]

    for file_path in files_to_copy:
        src = resource_filename(__name__, file_path)
        dst = os.path.join(target_location, os.path.basename(file_path))

        if not os.path.exists(dst):
            shutil.copy(src, dst)
            print(f"Copied {file_path} to {target_location}")
        else:
            print(f"{file_path} already exists in {target_location}")


def download_files():
    # Define the target location
    target_location = os.path.join(os.path.expanduser("~"), "your_package_data")

    # Ensure the target directory exists
    if not os.path.exists(target_location):
        os.makedirs(target_location)

    # Download and unzip files from GitHub
    github_repo = 'owner/repo'  # Replace with your repo
    release_tag = 'v1.0.0'  # Replace with your release tag
    github_files_to_download = [
        'file3.zip',  # Replace with your ZIP file name
    ]

    for file_path in github_files_to_download:
        download_file_from_github(github_repo, release_tag, file_path, target_location)

    # Copy files from the package
    copy_package_files(target_location)


if __name__ == "__main__":
    download_files()
