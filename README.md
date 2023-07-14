# Generating Output from LAMMPS JSON file

## What is this?
This Python script will generate output with basic parsing and conversion from LAMMPS [by Sandia Labs](https://www.lammps.org/) JSON output into more managable data. Python offers a suite of tools that make it very fast to design and implement into more managable formats like CSV, Graphs, and so on. This means that other languages can take these outputs and use their tools for faster or more comfortable syntax for who ever. 

## How to use it?

### LAMMPS Output

This section will come with an assumption that you know how LAMMPS works and how it produces outputs.

The following line of code will produce a JSON file with a style of output comptatible with the Python Script:

```
fix    ID atom_ID print time_step_interval """{"timestep": $(step), "args": $(args), ...}""" title "" file filename.json screen no
```

The command invokes from the `fix` command and it then uses the formatting provided through the print command to generate output for time steps. The following list contains all the main interchangable parts of the line, for the most part you can modify large chunks of it

1.    ***ID*** variable name assigned to the fix, used for unfixing when needed. So really there is nothing special with this one you can name it whatever you want as long as you remember when you apply your unfix command.

2.    ***atom_ID*** is a keyword identifier in LAMMPS. For this command the most ideal would be `all` which will just grab all atoms in the system for the measurement. However, you can specify your types according to your project. This was originally applied to a small protein.

3.    ***time_step_interval*** needs to be an integer, it will then for every timestep multiple of that number it will grab the following statement and insert it into the JSON file. Usually you need to identify this for your specific MD simulation but that is up to the script writer in the first place.

4.    ***"args": $(args), ...*** here you can grab any LAMMPS thermo variable or `compute` outputs and have it linked here. This is divided into two parts. The first *args* is for the name of the parameter, this will then be used in the output to track columns or lines on your graph. The second *args* is the name of the variable that you assigned. I typically named both the same but it works regardless of the naming they have as long as the second *args* has the specific variable name that is being output.

5.    ***filename*** replace this with your appropriate filename.

### Python Output

Once you have generated a JSON output you can start now parsing it. Start by indentifying the appropriate file path of the output for your system. I typically just put them in the same directory for ease of use, but it just depends on what you want to do.

The following is how to call the Python script:
```bash
python3 lmptoJSON.py input.json [-optional flags]
```

This may change from system to system, or how you named Python interpreter in your path. The optional flags are the following:

- `-legend` or `-l` links into your graphical output the legend where the names are derived from the column names in the JSON.
- `-show` or `-s` will automatically show you the graph, depending on your system you may need some additional feature like -X11 to actually see it, but most guiwill handle this just fine.
- `-save` or `-f` will save the graphical output as a `.png` with the same file name.

Once you have your output you are done and ready to go with a graph!


## Upcoming changes

Currently the major plan is to add file output beyond just graphical output. Right now that means CSV at least. However, I am going to do some reasearch and see about getting optiosn for small size/faster read/writes as well. Also feel free to open issues or to make suggetions and I will take them into consideration.
