# Tree from Transcriptome
Python codes to make phylogenetic analysis easier

This repositry have collection of Python codes which can help you make a Phylogentic tree If you already have a Multiple sequence alighnemets and you want to add your species to that tree.


**First_code**
Gene_extarcter

Generally, the starting point when you are building a phylogentic tree, is to extract single gene from MSA so that you can BLAST those genes on your Trancriptome/proteome and find the exact genes so that you can add in MSA and build tree.

Gene_extracter- this is the first code I wrote with my dear friend @abhinav1602 which extrct single genes from each MSA so that you can BLAST these genes on your transcriptome/proteome.
Another feature of this code is that you can select from which species you want to extrct single genes from, Since you don't want to select random species(It's better to select a phylogentic closure species than an outgroup species)

**Second Code**
adding_proteins_to_msa

After getting the proteins from the Transcriptome the next step is to add those proteins to the respective Multiple sequence alignement. Here in this script it uses three types of files. 1. Postion.csv in which there is one column is the gene with second column the MSA file in which it has to be added.
2. proteins.fasta  - all the proteins extected from your transcriptome
3. Folder with all the MSA files in which the protein is to be added.

