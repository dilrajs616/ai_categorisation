def process_txt(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Process lines to merge multiline category values
    processed_lines = []
    current_line = ""

    for line in lines:
        line = line.strip()
        if line.startswith("http"):
            # If the line starts with 'http', it's a new URL/category pair
            if current_line:
                processed_lines.append(current_line)
            current_line = line
        else:
            # Otherwise, append the line to the previous one
            current_line += ' ' + line

    # Add the last line to processed lines
    if current_line:
        processed_lines.append(current_line)

    # Write the processed data to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in processed_lines:
            outfile.write(line + "\n")

# Example usage:
input_file = 'output.csv'  # Replace with your input file path
output_file = 'refactored_output.csv'  # Replace with your desired output file path

process_txt(input_file, output_file)
