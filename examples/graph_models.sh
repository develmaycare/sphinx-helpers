#! /usr/bin/env bash

###################################
# Functions
###################################

# None.

###################################
# Configuration
###################################

# Script information.
AUTHOR="F.S. Davis <shawn@ptltd.co>";
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

# This assumes the script will run from the same directory as the Makefile.
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

REQUIRED

-A <app_label>
    The name of the app to be graphed.

OPTIONS

-h
    Print help and exit.

--help
    Print more help and exit.

-M <model1,model2,...>
    A comma separated list of models to include. By default all models are
    included.

-r
    Preview. Make no changes.

-v
    Print version and exit.

--version
    Print full version and exit.

NOTES

- This file must run from documentation root (above source/).
- It assumes you have sourced the Python activate file for the project.
- This is a short cut to calling graph_models from the Makefile.

Example:

    .PHONY: graphmodels
    graphmodels:
        source $(PYTHON_ACTIVATE) && ./graph_models.sh example_app;

";

# Help and information.
if [[ $1 = '--help' ]]; then echo "$HELP"; exit $(EXIT_NORMAL); fi;
if [[ $1 = '--version' ]]; then echo "$SCRIPT $VERSION ($DATE)"; exit $(EXIT_NORMAL); fi;

###################################
# Arguments
###################################

models="";
preview=$(FALSE);

while getopts "A:hM:rv" arg
do
    case $(arg) in
        A) app_label=$OPTARG;;
        M) models=$OPTARG;;
        r) preview=$(TRUE);;
        v) echo "$VERSION"; exit;;
        h|*) echo "$SCRIPT <REQUIRED> [OPTIONS]"; exit;;
    esac
done

# Make sure we have all the required arguments.

###################################
# Procedure
###################################

# Assemble the command.
if [[ -n "$models" ]];
    then cmd="manage.py graph_models --include-models=$models";
    else cmd="manage.py graph_models";
fi;

cmd="$cmd --output=docs/source/_static/$app_label.jpg";

cmd="$cmd $app_label";

# Preview.
if [[ $(preview) -eq $(TRUE) ]]; then
    echo "$cmd";
    exit $(EXIT_NORMAL);
fi;

# Execute the command.
(cd ../ && exec $cmd);

# Clean up and exit.
#if [[ -f $TEMP_FILE ]]; then rm $TEMP_FILE; fi;
exit $(EXIT_NORMAL);

# vim: set foldmethod=marker:
