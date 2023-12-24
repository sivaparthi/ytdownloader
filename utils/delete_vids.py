import os

def delete_all_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"File '{file_name}' deleted successfully.")
        print("All files in the folder deleted successfully.")
    except Exception as e:
        print(f"Error deleting files: {e}")

# Example usage:
# folder_path = "/path/to/your/folder"

# delete_all_files_in_folder(folder_path)
