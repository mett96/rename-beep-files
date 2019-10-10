# Rename Beep File
This small script removes all the `+` characters and replaces them with a space contained in the file name.

It is a very simple tool but very useful when directly downloading zip files from folders from the [Beep site](https://beep.metid.polimi.it).
## Instructions

Install the package.
```
pip install rename-beep-files
```

To show the help menu digit
```
rename-beep-files -h
```

> usage: renamebeepfiles [-h] [-r] [paths [paths ...]]
>
>Process renames all the file into the target directory.
>
>positional arguments:
>  paths            Specify all the folders in which execute the renaming
>
>optional arguments:
>  -h, --help       show this help message and exit
>  -r, --recursive  Execute the rename action recursively into all
>                   subdirectories of targeted folder


