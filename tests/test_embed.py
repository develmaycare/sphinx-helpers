from sphinx_helpers.embed import *

# Tests


def test_lucidchart():
    # Names specific to docutils
    name = "lucidchart"
    args = list()
    options = list()
    content = list()
    lineno = 17
    contentOffset = None
    blockText = None
    state = None
    stateMachine = None

    output = lucidchart(name, args,options, content, lineno, contentOffset, blockText, state, stateMachine)
    assert output is None

    content = [
        "ASDF1234",  # embed ID
        "width=500",
        "height=500",
    ]
    output = lucidchart(name, args, options, content, lineno, contentOffset, blockText, state, stateMachine)
    # print(output[0])
    assert "https://www.lucidchart.com/documents/embeddedchart/ASDF1234" in str(output[0])
    assert 'style="width:500; height:500"' in str(output[0])


def test_vimeo():
    # Names specific to docutils
    name = "vimeo"
    args = list()
    options = list()
    content = list()
    lineno = 17
    contentOffset = None
    blockText = None
    state = None
    stateMachine = None

    output = vimeo(name, args, options, content, lineno, contentOffset, blockText, state, stateMachine)
    assert output is None

    content = [
        "ASDF1234",  # embed ID
        "width=500",
        "height=500",
    ]
    output = vimeo(name, args, options, content, lineno, contentOffset, blockText, state, stateMachine)
    # print(output[0])
    assert "https://player.vimeo.com/video/ASDF1234" in str(output[0])
    assert 'height="500"' in str(output[0])
    assert 'width="500"' in str(output[0])


def test_wistia():
    # Names specific to docutils
    name = "wistia"
    args = list()
    options = list()
    content = list()
    lineno = 17
    contentOffset = None
    blockText = None
    state = None
    stateMachine = None

    output = wistia(name, args, options, content, lineno, contentOffset, blockText, state, stateMachine)
    assert output is None

    content = [
        "ASDF1234",  # embed ID
        "width=500",
        "height=500",
    ]
    output = wistia(name, args, options, content, lineno, contentOffset, blockText, state, stateMachine)
    # print(output[0])
    assert "https://fast.wistia.net/embed/iframe/ASDF1234?videoFoam=true" in str(output[0])
    # assert 'height="500"' in str(output[0])
    # assert 'width="500"' in str(output[0])


def test_youtube():
    # Names specific to docutils
    name = "youtube"
    args = list()
    options = list()
    content = list()
    lineno = 17
    contentOffset = None
    blockText = None
    state = None
    stateMachine = None

    output = youtube(name, args, options, content, lineno, contentOffset, blockText, state, stateMachine)
    assert output is None

    content = [
        "ASDF1234",  # embed ID
        "width=500",
        "height=500",
    ]
    output = youtube(name, args, options, content, lineno, contentOffset, blockText, state, stateMachine)
    # print(output[0])
    assert "https://www.youtube.com/embed/ASDF1234" in str(output[0])
    assert 'height="500"' in str(output[0])
    assert 'width="500"' in str(output[0])
