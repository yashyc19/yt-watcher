# create a visually pleaseing dummy cli based image
# using the click library

import click
import numpy as np

@click.command()
@click.option('--rows', default=5, help='Number of rows in the dataframe')
@click.option('--columns', default=5, help='Number of columns in the dataframe')
def main(rows, columns):
    # create a dataframe with the dummy data
    data = np.random.randint(0, 100, size=(rows, columns))
    click.echo(data)

if __name__ == '__main__':
    main()

# Run the script using the command:
# python main.py --rows 5 --columns 5
