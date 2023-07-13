# Graph Output from LAMMPS JSON file

This is a python script for converting the LAMMPS JSON file output from the following line of code:

```
fix    ID atom_ID print time_step_interval """{"timestep": $(step), "args": $(args), ...}""" title "" file filename.json screen no
```

This is derived from the `fix` command in LAMMPS.
1.    ***ID*** variable name assigned to the fix, used for unfixing when needed.
2.    ***atom_ID*** assigns which atoms the fix will apply, you will want to use `all` keyword typically.
3.    ***time_step_interval*** needs to be an integer, it will then for every timestep multiple of that number it will grab the following statement and insert it into the file
4.    ***"args": $(args), ...*** here you can grab any LAMMPS thermo variable and have it print out, make sure to match an appropriate name, typically I just grab the name of the variable and assign it in as well.
5.    ***filename*** replace this with your appropriate filename.

The output can then be passed into this script and will output a figure, it will not be saved now but can be saved by added the `savefig()` method to your graph.

## Upcoming chnages

I will probably add a few this in future namely passing in command line arguments and maybe a little more clarity on the LAMMPS JSON output.
