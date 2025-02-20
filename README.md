# 1D setups

The repository contains all information to create working configurations for the stations give as folders in the repository. This information contains the environmental forcing like initial conditions for salinity and temperature, time varying surface forcing from ERA5 and a selection of bio-geochemical models to chose from.
In total there is M=12 station and N=7 biogechemical models - normally requirering 84 different setups to cover them all. As the format of a FABM yaml configuration file is independent of the driver model setup - i.e. it can be used for both 1D and 3D setups without modifications - a given FABM yaml file can be reused without modifications. The site specific configuration is done by the driver model - in this case GOTM - and it requires snippets of YAML text to be changed between different bio-geochemical simulations. The benefit is that the 84 configurations has been reduced to 12 (stations) + 7 (FABM yaml files) + 7 (GOTM yaml snippets) = 26.

The basic configurations have been downloaded from iGOTM (igotm.bolding-bruggeman.com) based on a list of stations defined in OceanICU WP6.
The FABM yaml files for the individual bio-geochemical models are obtained from the repositories of the different models and stored in the folder fabm-yaml.

## How to create a working setup

In order to create a working setup two different methods are supported:

   1. manually edit the _gotm.yaml_ and substitute the _fabm:_ section with the content of the relevant file in the gotm-snippets folder and copy the relevant FABM yaml file to the setup folder.
   2. use the provided Python to perform the task automatically

#### Manual method

Do the following steps

###### Edit _gotm.yaml_

   1. Enter the folder of a site
   2. Create a copy of gotm.yaml:
       `copy gotm.yaml gotm.yaml.org`
   2. Open the _gotm.yaml_ file in an editor
   3. Search and replace the _fabm: section_
       1. Search for _fabm:_
       1. Delete down to the _eq_state:_ section
       3. Insert the content of the relevant file from the _gotm_snippets_ folder
   5. Save the file and exit

###### Copy _fabm.yaml_

   1. Copy the relevant FABM yaml file to <site_dir>/fabm.yaml

#### Script method

Execute the following command with appropriate arguments

```
python config_set.py BATS ergom 
```

## Executing GOTM

The format of the GOTM and FABM yaml files corresponds to GOTM version 6 which must be compiled and in the PATH.
To run a configured setup simply do in the setup folder:

```
gotm
```
