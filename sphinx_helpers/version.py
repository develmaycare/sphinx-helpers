major = 0
minor = 9
patch = 0
status = "d"
build = ""
name = ""


def get_release():
    r = "%s.%s.%s" % (major, minor, patch)

    if status:
        r += "-%s" % status

    return r


def get_version():
    return "%s.%s" % (major, minor)


RELEASE = get_release()
VERSION = get_version()

