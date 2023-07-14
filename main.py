import pandas as pd
import matplotlib.pyplot as plt
import sys
import os.path

def main():
    
    filename = sys.argv[1]

    if (not os.path.isfile(filename)):
        print("File not found in path")
        exit()

    df = pd.read_json(filename, lines=True)

    x_col = df.columns[0]
    if (x_col != 'timestep'):
        print("Possible error with format of JSON please refer to README")
        exit()

    xpoints = df[x_col].values.tolist()

    for i in range(1, len(df.columns)):
        plt.plot(xpoints, df[df.columns[i]].values.tolist())

    if (('-legend' in sys.argv) or ('-l' in sys.argv)):
        plt.legend(df.columns[1:])
    if (('-show' in sys.argv) or ('-s' in sys.argv)):
        plt.show()
    if (('-save' in sys.argv) or ('-f' in sys.argv)):
        plt.savefig(os.path.splittext(filename) + '.png')

if __name__ == "__main__":
    main()
