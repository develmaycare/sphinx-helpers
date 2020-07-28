#! /usr/bin/env python

# It would be admirable to support PEP 350.
# http://www.python.org/dev/peps/pep-0350/

# This format is also interesting.
# http://www.approxion.com/?p=39

from subprocess import getstatusoutput


def print_todos(section_title, path):

    print("*" * len(section_title))
    print(section_title)
    print("*" * len(section_title))
    print("")

    (status, output) = getstatusoutput('cd ../ && find %s -type f -name "*.py"' % path)
    files = output.split("\n")

    for f in files:
        (status, output) = getstatusoutput('cd ../ && grep "# TODO:" %s' % f)
        if status > 0:
            #print "SKIP", f
            continue

        #print "MATCH", f

        #(status, output) = getstatusoutput('grep "^[ ]*# " %s' % f)
        (status, output) = getstatusoutput('cd ../ && cat %s' % f)
        lines = output.split("\n")

        inside_todo = False
        start_of_todo = False

        print(f)
        print("=" * len(f))
        print("")

        for line in lines:
            line = line.lstrip()

            if "# TODO:" in line:
                inside_todo = True
                start_of_todo = True
                print(line.replace("# TODO: ", ""))
            elif len(line) == 0:
                if inside_todo:
                    print("")
                inside_todo = False
                start_of_todo = False
            elif line[0] == "#":
                if inside_todo:
                    print(line.replace("# ", ""))
            else:
                pass


title = "To-dos from Source"
print("#" * len(title))
print(title)
print("#" * len(title))
print("")

# Now call print_todos() ...
print_todos("Contrib Apps", "source/contrib")
print_todos("Local Apps", "source/local")
print_todos("Shared Apps", "source/shared")
