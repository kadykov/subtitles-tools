# %%
def delete_odd_lines(input_file, output_file):
    """
    Deletes every odd line from the input file and writes the even lines to the output file.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
    """
    with open(input_file) as file:
        lines = file.readlines()

    # Write even lines to the output file
    with open(output_file, "w") as file:
        for i, line in enumerate(lines):
            if (i + 1) % 2 == 0:  # Check if the line number is even
                file.write(line)


# Example usage
if __name__ == "__main__":
    input_file = "repeated-lines.txt"
    output_file = "unformatted.txt"
    delete_odd_lines(input_file, output_file)
    print(f"Even lines have been written to {output_file}")

# %%
