import socket
from collections import Counter
from pathlib import Path


def count_words(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read().lower()
            words = text.split()
            return len(words)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def get_top_3_most_frequent_words(file_path, handle_contractions=False):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read().lower()

            if handle_contractions:
                contractions = {
                    "it's": "it is",
                    "couldn't": "could not",
                    "i'm": "i am",
                    "can't": "cannot",
                    "won't": "will not",
                    "i'll": "i will",
                    "don't": "do not",
                    "you're": "you are",
                    "that's": "that is",
                }
                for contraction, replacement in contractions.items():
                    text = text.replace(contraction, replacement)

            words = text.split()
            word_counts = Counter(words)

            return word_counts.most_common(3)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None


def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def main():
    source_directory = Path("/home/data")
    file1 = source_directory / "IF-1.txt"
    file2 = source_directory / "AlwaysRememberUsThisWay-1.txt"

    output_directory = Path("/home/data/output")
    output_directory.mkdir(parents=True, exist_ok=True)

    output_file = output_directory / "result.txt"

    output_string = ""

    file1_word_count = count_words(file1)
    if not file1_word_count:
        print(f"Error reading {file1}. Exiting.")
        return
    output_string += f"{file1} file contains {file1_word_count} words.\n"

    file2_word_count = count_words(file2)
    if not file2_word_count:
        print(f"Error reading {file2}. Exiting.")
        return
    output_string += f"\n{file2} file contains {file2_word_count} words.\n"

    output_string += f"\nBoth files collectively contain {file1_word_count + file2_word_count} words.\n"

    file1_top_3_words = get_top_3_most_frequent_words(file1)
    if not file1_top_3_words:
        print(f"Error processing {file1}. Exiting.")
        return
    output_string += (
        f"\nTop 3 most frequent words and their respective counts in {file1}:\n"
    )
    for word, count in file1_top_3_words:
        output_string += f"    '{word}' occured {count} times.\n"

    file2_top_3_words = get_top_3_most_frequent_words(file2, handle_contractions=True)
    if not file2_top_3_words:
        print(f"Error processing {file2}. Exiting.")
        return
    output_string += f"\nTop 3 most frequent words and their respective counts in {file2} (with contraction handling):\n"
    for word, count in file2_top_3_words:
        output_string += f"    '{word}' occured {count} times.\n"

    ip_address = get_ip_address()
    output_string += f"\nIP address of the machine is {ip_address}"
    print(output_string)

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(output_string)
    except Exception as e:
        print(f"Error writing to output file {output_file}: {e}")

    print(f"\nOutput written to {output_file}.")


if __name__ == "__main__":
    main()
