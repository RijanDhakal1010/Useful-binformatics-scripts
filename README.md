# The folders are demarcated accoridng to the language they hold. This repo is for scripts/code and scripts/code only. Actual data files can be easily replicated and as such I have decided to document how to generate data instead of storing it here.  

# Bash

## This folder, like its namesake has bash scripts.

**Auto_concatanate.sh**

This file takes all the scripts in a parent_directory/child_directories/list_of_file and concatates all the list_of_files and gives the output files the names in the pattern of {child_directories}.cat and puts them is a desktop folder /home/user/Desktop/dump.

**Auto_gdown.sh**

This script automates the gdown commandline untility to use download links to grab files from google drive. The list of links should be supplied as a sysargv right after the scripts names.

**Auto_taxon.sh**

This script takes a list of species and then generates detailed taxonomic information on the species using the enterex suit of tools. If you do not have the enterez suit of tools installed on your computer you can use this one-liner to install is `sh -c "$(curl -fsSL ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"`. For this specific file use supply the list of species as the first sysargv.

**biostar_peptide_download_help_scripts_1.sh**

This script reads the output of the protein_download.sh file and outputs the assembly accession of the species at play.

**biostar_peptide_download_help_scripts_2.sh**

This script reads the output of the protein_download.sh file and outputs the assembly accession of the species at play.

**TarSucks.sh**

The tar utility does not quite work like other tools when give a list of files in once go froma pipe. For example `ls -l | tar` is not a good idea since tar can take multiple files at the same time and does not untar the list files at hand so much as work on all the files at the same time. Since that is not what I want, and what I do want is to untar all the files in a directory, this script is designed to automate that task by iterating through the tar files in the folder.

# Python

## This folder, like its namesake has python scripts.

**convert_enterez_stdout_to_2d_table_format_1.py**

The stdout from enterez comes out in a format that is not easy to convert into a table. The data comes out in the following format:

1. Species name

Kingdom kingdom_name

Phyllum Phyllum_name

Clade Clade_name

2. Species name

Kingdom kingdom_name

Phyllum Phyllum_name

Clade Clade_name

The above format is somewhat difficult to convert to a table like this:

| Species      | Kingdom |Phyllum|Clade|
| ----------- | ----------- |-----|------|
| Species_1      | Kingdom_name       |phyllum_name|Clade_name|
| Species_2   | kingdome_name        |phyllum_name|Clade_name|

**csv_to_rdb.py**

This file take the base_chnage.tab file produced by cafe and changes it to a relational database. This should make parsing the data easier than just going through the text.

**onekp_html_parser.py**

Since the R package to access the onekp database is not working, the only option we have is to use the html table\journal of hyperlinks available at [Onekp html website](http://www.onekp.com/public_data.html). To be honest we can only hope that the people who made this website keep it up. Since a stable API to the database seems to be absent, this for now seems to be the only way available to easily access the data. There is cyverse, but I have not gotten around to automating access to cyverse. This link should print out in this format : https://drive.google.com/uc?id=1GrB19Tl87zAbpqh3wgO8NCi9xR371MZq but they are generated in a different format with extraneous characters thah hamper *gdown*, to counter this it is best if *onekp_html_parser.py* prints the links out with the extraneous characters removed. The links are genererated in the format https://drive.google.com/uc?export=download&id=1nQ12-E0755E6O24XOGkHVdGPBwoTQFhU.

**Shuffle.py**

This script need three sysargvs with flags in the following format

1. The --pickle flag should be used to supply the location of the picke that holds the connection between the codenames and realnames. The codenames should be the keys and the realnames should be the values in the dict, a spcies can have two codes but a code can only have one species.

2. The --loc_one flag should be used to supply the location of the bulk downloaded archive files that hold the transcriptomes. 

3. The --loc_two flag should be used to supply the location of where the filitered list will be plastered.

If the above params are supplied in a sane and proper matter, then the script will take the pickled dict, go to the --loc_one path and take the list-specified species, change the archived files' names and move them to the --loc_two specified path.

When I say sane, I mean files and folders that actually do exist.