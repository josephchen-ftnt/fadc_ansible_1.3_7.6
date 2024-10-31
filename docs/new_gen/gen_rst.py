import sys

def replace_name_in_article(name, usage, file_path):
    # Read the article from the input file
    with open(file_path, 'r') as file:
        article = file.read()
    
    # Replace all occurrences of ##NAME## with the given name
    updated_article = article.replace('##MODULE_NAME##', name)
    updated_article = updated_article.replace('##MODULE_USAGE##', usage)
    return updated_article

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python replace_name_in_article.py <name> <usage> <input_file_path> <output_file_path>")
        sys.exit(1)

    # Get the name and file paths from command-line arguments
    name = sys.argv[1]
    usage = sys.argv[2]
    input_file_path = sys.argv[3]
    output_file_path = sys.argv[4]

    # Call the function and get the updated article
    updated_article = replace_name_in_article(name, usage, input_file_path)

    # Print the updated article
    # print(updated_article)

    # Write the updated article to an output file
    with open(output_file_path, 'w') as file:
        file.write(updated_article)