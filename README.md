# Lexical Scanner
- The Mid-term "Compiler" project by Duc Tran Van, Duy Duong Duc, Anh Le Tuan.
# Installation
- Install the required packages by the following command:
```cmd
pip install -r requirements.txt
```
# Input
- The input file was stored in `./input` directory
- Starting file is `main.py`.
```py
def generate_token(file):
    # Some hidden code

generate_token("{input_file_name}")
```
- Put `{input_file_name}.vc` file in `./input` directory and put file name in `generate_token` function.
- Run the `main.py` file.
# Output
- The output was stored in `./output/{input_file_name}` directory.
- `graph.dat` file:
    - Contains info about automata-graph.
    - Categories are `ALPHABET`, `STATE`, `INITIAL_STATE`, `ACCEPTING_STATES`, and `TRANSITIONS`.
    - Each element will be included consequently under the categories.
    - Each category ends with a blank line
- `table.dat` file:
    - Contains info about automata-graph by display into a table.
    - The first row is the alphabet.
    - The first column is the state.
    - Each cell is a next_state which display the transition `state -> alphabet -> next_state`
- `{input_file_name}.vctok` file:
    - Contains info about the token.
    - Each line contains a token.
- `{input_file_name}.verbose.vctok` file:
    - Contains info about the token with detailed information.
    - Each line contains a token with `kind`, `spelling`, and `position`