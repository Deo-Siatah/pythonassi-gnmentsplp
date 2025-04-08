import os 

#Ask for a filename

filename=input("Enter a filename:")
try:
    #Check if the file exists
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} does not exist")
except FileNotFoundError as e:
    print(e)
    
    #try to read the file
    with open (filename,"r") as file:
        file.read()
except PermissionError:
    print(f"You do not have permission to read {filename}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")