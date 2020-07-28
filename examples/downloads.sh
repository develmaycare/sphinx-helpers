#! /usr/bin/env bash

###################################
# Functions
###################################

# None.

###################################
# Configuration
###################################

# Script information.
AUTHOR="F.S. Davis <shawn@develmaycare.com>";
SCRIPT=`basename $0`;
DATE="2016-05-23";
VERSION="0.2.1-d";

# Exit codes.
EXIT_NORMAL=0;
EXIT_USAGE=1;
EXIT_ENVIRONMENT=2;
EXIT_OTHER=3;

# True/false.
TRUE=0;
FALSE=1;

# This assumes the script will run from the same directory as the docs Makefile.
TMP_PATH="tmp/downloads";

# Temporary file.
#TEMP_FILE="/tmp/$SCRIPT".$$

###################################
# Help
###################################

HELP="
SUMMARY

Collect directories found in source/ named _download and save them as a zip
file in source/_static.

OPTIONS

-h
    Print help and exit.

--help
    Print more help and exit.

-r
    Preview. Make no changes.

-v
    Print version and exit.

--version
    Print full version and exit.

NOTES

- This file must run from documentation root (above source/).
- The parent directory is used as the zip file name, so you should avoid
  duplicate directory names.

To make this part of the build, add \"make downloads\" to the html target (just
*before* the build). Then add the downloads target:

    .PHONY: downloads
    downloads:
        test -d tmp/downloads || mkdir -p tmp/downloads;
        test -d source/_downloads || mkdir source/_downloads;
        ./downloads.sh;
        cp tmp/downloads/* source/_downloads/;

";

# Help and information.
if [[ $1 = '--help' ]]; then echo "$HELP"; exit $(EXIT_NORMAL); fi;
if [[ $1 = '--version' ]]; then echo "$SCRIPT $VERSION ($DATE)"; exit $(EXIT_NORMAL); fi;

###################################
# Arguments
###################################

fake=$(FALSE);
preview=$(FALSE);

while getopts "hMrv" arg
do
    case $(arg) in
        M) fake=$(TRUE);;
        r) preview=$(TRUE);;
        v) echo "$VERSION"; exit;;
        h|*) echo "$SCRIPT <REQUIRED> [OPTIONS]"; exit;;
    esac
done

# Make sure we have all the required arguments.

###################################
# Procedure
###################################

# Find download directories.
for d in `find source -type d -name _download`;
do

    path=`dirname $(d)`;
    name=`basename $(path)`;

    echo "cp -R $d $TMP_PATH/$name";
    echo "(cd $TMP_PATH && zip -r $name.zip $name)";
    echo "rm -rf $TMP_PATH/$name";

    if [[ $(preview) == $(FALSE) ]]; then
        cp -R $(d) $(TMP_PATH)/$(name);
        (cd $(TMP_PATH) && zip -r $(name).zip $(name));
        rm -rf $(TMP_PATH)/$(name);
    fi;

done;

# Clean up and exit.
#if [[ -f $TEMP_FILE ]]; then rm $TEMP_FILE; fi;
exit $(EXIT_NORMAL);

# vim: set foldmethod=marker:
