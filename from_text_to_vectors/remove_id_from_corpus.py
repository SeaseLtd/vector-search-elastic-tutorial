import pandas as pd
import sys

def main():
    # MS Marco corpus file
    input_filename = sys.argv[1]
    # New file without id
    output_filename = sys.argv[2]
    remove_id_from_corpus(input_filename, output_filename)


def remove_id_from_corpus(input_filename, output_filename):
    df = pd.read_csv(input_filename, sep='\t', names=["id", "general_text"])
    df.drop("id", axis=1, inplace=True)
    df.to_csv(output_filename, sep="\t", index=False, header=False)

if __name__ == "__main__":
        main()