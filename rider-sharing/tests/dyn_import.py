import os
import importlib

src_dir = 'src'
def dyn_import():

    # Iterate over the files in the src directory
    for file in os.listdir(src_dir):
        if file.endswith('.py'):  # Filter only Python files
            module_name = file[:-3]  # Extract the module name without the .py extension
            file_path = os.path.join(src_dir, file)  # Construct the file path
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print(f"imported {file_path}")
            for name, value in vars(module).items():
                # callable(value)
                if name not in globals():
                    globals()[name] = value

    imported = True

    print(f"Dyn import success {imported}")
