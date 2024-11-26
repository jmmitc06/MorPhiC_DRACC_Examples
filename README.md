# Overview

This repository contains example analysis for MorPhiC. Ultimately, we will have more examples here of metabolomics processing for different experimental designs used for MorPhiC. 

## Analysis Types

Different gene KOs or cell types may require different workflows or different parameters. The processing can be subdivided into the following:

1. "regular" methods - this includes traditional HILIC and RP LC-MS datasets without chemoselective derivatization or stable isotope labelling. This is the majority of the data in the atlas and the HMGCS2 processing is the reference implementation.

2. derivatization methods - in this workflow, metabolites are first derivatized (covallently modified) to yield a permanently charged form of the metabolites. The derivatization is specific for certain functional groups, so the same sample derivatized using different reagents (e.g., DmPA vs. DnHZ) will allow for the detection of different sets of metabolites in the sample. (SOON - this will be in V2, but final form still being decided - annotation is extra challenging here)

3. isotope tracing - in these experiments, a tracer compound containing a stable isotope is enriched in the media (most commonly a 13C isotopologue of a common metabolite such as glucose or glutamine). How this data needs to be processed depends on the parameters of the labelling experiment (e.g., if 15N is enriched, we need to look for 15N isotopologues) (SOON - expect this in V3 release, experiment in progress now)

Many experiments include MS2 data. Such data is handled in the same manner for all experiments during the annotation notebook(s).

## MorPhiC Datasets

Below is a list of MorPhiC datasets and how they were processed. The processing is located in a directory with the gene name(s). 

Gene(s), processing type, subdatasets

* HMGCS2 (this is a representative "regular" mode analysis)
    * Cell Pellet
        * HILIC neg - regular 
        * RP pos - regular

## Preparing the Environment

Development is done on MacOS using Python3.11, you will need a functioning python interpreter, preferably 3.11 or later, and some way to run jupyter notebooks. 

Processing is done using the asari ecosystem. You can install all needed python packages by `pip3 install pcpfm`

For .raw to .mzML conversion, you can use the convert.py script located in the HMGCS2 directory, but you will need to update the path to the executable. You can get the executable by running `pcpfm download_extras`, accept the license terms, then look in the site-packages directory to find the correct path: e.g., `/Users/USER/Library/Python/VERSION/lib/python/site-packages/pcpfm/`.

## Regular Analysis WalkThrough

You should be able to follow the notebooks in order with minor modifications for paths. 

You should first prepare the MS2 data using the prep_MS2.ipynb. Alternatively, you can just download the mzML version of the dataset from the box link. 

## Todo

* Authentic standard annotations are difficult to apply to old datasets, may be an instrument configuration / method change or a bug, not sure.

* Output formats are very verbose, have redundant information, etc. This needs to be fixed before data release. 

* Annotation confidence - in general, level 2 annotations >> level 4 in terms of accuracy, however level 2 does not imply that all annotations are correct. Unlike other -omics datasets, annotation in metabolomics remains a significant challenge.

## Atlas Prototype 

See this url: https://ipsc-atlas.web.app/