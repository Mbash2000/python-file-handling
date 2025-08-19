# file_read_write.py

def modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify content (e.g., convert to uppercase)
        modified_content = content.upper()

        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"✅ File has been read from '{input_file}' and modified version saved to '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    modify_file("input.txt", "output.txt")
