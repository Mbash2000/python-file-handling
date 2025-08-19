# error_handling_lab.py

def read_file_with_error_handling():
    filename = input("📂 Enter the filename you want to read: ")

    try:
        with open(filename, 'r') as file:
            print("✅ File content:")
            print(file.read())
    
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist. Please check the name and try again.")
    
    except PermissionError:
        print(f"⚠️ Error: You don’t have permission to read '{filename}'.")
    
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    read_file_with_error_handling()
