# defaults.py
# set up defaults for the pipeline
# Randall Johnson
# BSP CCR Genetics Core at Frederick National Laboratory
# Leidos Biomedical Research, Inc
# Created January 15, 2014
# Last Modified January 17, 2014

###### variables and defaults ######
# project       <-- must specify
# workdir = <current working directory>
# datadir = "/data1/johnsonra/microbiome/refdata/"
# pdiffs = 2
# bdiffs = 1
# diffs = 1 ... used in clustering

###### need to be added ######
# processors = 12

# Switch to correct working directory
try:
      PATH = args['workdir']
      if len(PATH) > 0:
            os.chdir(PATH)
except KeyError:
      print("Using default working directory.")
except OSError:
      print("Invalid value for workdir, using default directory.")

# link data files to the current working directory
# this is going to need some work...not all oligos files will be in the DATAPATH
try:
      DATAPATH = args['datadir']
except KeyError:
      DATAPATH = "/data1/johnsonra/microbiome/refdata/"

if os.path.isdir(DATAPATH):
      os.system("ln -fs " + DATAPATH + "oligos.txt .")
      os.system("ln -fs " + DATAPATH + "trainset7_112011.pds.fasta .")
      os.system("ln -fs " + DATAPATH + "trainset7_112011.pds.tax .")
      os.system("ln -fs " + DATAPATH + "LookUp_Titanium.pat .")
      os.system("ln -fs " + DATAPATH + "silva.* .")
else:
      raise Exception("Bad value for datadir.")

# make sure we have the project name ###
try:
      proj = args['project']
except KeyError:
      raise Exception("Missing project name!")

# pdiffs
try:
      pdiffs = args['pdiffs']
except KeyError:
      pdiffs = '2'

# bdiffs
try:
      bdiffs = args['bdiffs']
except KeyError:
      bdiffs = '1'