# This script goes through the notebooks given in the argument and prepends a preamble for use in colab

import argparse
from pathlib import Path
import json

def main():
    parser = argparse.ArgumentParser(description="Insert the given preamble to the given notebooks")
    parser.add_argument('preamble_notebook', help="Path to the notebook containing the preamble files", type=Path)
    parser.add_argument('notebooks', help="Path to the notebooks which should be converted", nargs='+', type=Path)
    parser.add_argument('--output-dir', help="Path where to save the converted notebooks", type=Path, default=Path('./colab'))
    args = parser.parse_args()

    with open(args.preamble_notebook) as fp:
        preamble_json = json.load(fp)

    notebooks_to_convert = [p for notebook in args.notebooks for p in notebook.glob('**/*.ipynb')]
    print(preamble_json)
    for notebook_path in notebooks_to_convert:
        with open(notebook_path) as fp:
            notebook_to_convert = json.load(fp)
        if 'metadata' not in notebook_to_convert:
            notebook_to_convert['metadata'] = dict()
        notebook_to_convert['metadata'].update(preamble_json['metadata'])
        notebook_to_convert['cells'] = preamble_json['cells'] + notebook_to_convert['cells']
        output_path = args.output_dir/notebook_path.name
        with open(output_path, 'w') as fp:
            json.dump(notebook_to_convert, fp)

    
if __name__ == '__main__':
    main()