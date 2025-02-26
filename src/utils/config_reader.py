import os

def read_store_data(file_path):
    # Define absolute_path before any try blocks
    absolute_path = file_path
    try:
        # Get the absolute path to the project root
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        absolute_path = os.path.join(project_root, file_path)
        
        with open(absolute_path, 'r') as file:
            stores = [line.strip() for line in file if line.strip()]
            return stores
    except FileNotFoundError:
        # Include both paths in the error message for debugging
        raise FileNotFoundError(f"Store data file not found. \nTried paths:\n- {file_path}\n- {absolute_path}")
    except Exception as e:
        raise Exception(f"Error reading store data from {absolute_path}: {str(e)}")

def get_all_stores():
    stores = read_store_data('src/data/stores.csv')
    return stores