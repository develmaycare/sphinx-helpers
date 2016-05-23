"""
Tools for embedding multi-media.

"""

# noinspection PyPackageRequirements
from docutils import nodes
# noinspection PyPackageRequirements
from docutils.parsers.rst import directives

# noinspection SpellCheckingInspection
LUCIDCHART_TEMPLATE = """
<div style="width:%(width)s; height:%(height)s; position:relative;">
    <iframe
        allowfullscreen
        frameborder="0"
        style="width:%(width)s; height:%(height)s"
        src="https://www.lucidchart.com/documents/embeddedchart/%(embed_id)s"
        id="%(embed_id)s">
    </iframe>
</div>
<br>
<br>
"""


# noinspection PyUnusedLocal,PyPep8Naming
def lucidchart(name, args, options, content, lineno, contentOffset, blockText,
               state, stateMachine):
    """Embed a LucidChart graphic."""

    if len(content) == 0:
        return

    context = {
        'embed_id': content[0],
        'height': "480px",
        'width': "640px",
    }

    extra_args = content[1:]  # Because content[0] is ID
    extra_args = [ea.strip().split("=") for ea in extra_args]  # key=value
    extra_args = [ea for ea in extra_args if len(ea) == 2]  # drop bad lines
    extra_args = dict(extra_args)

    if 'width' in extra_args:
        context['width'] = extra_args.pop('width')

    if 'height' in extra_args:
        context['height'] = extra_args.pop('height')

    return [nodes.raw('', LUCIDCHART_TEMPLATE % context, format='html')]

lucidchart.content = True
directives.register_directive('lucidchart', lucidchart)


YOUTUBE_TEMPLATE = """
<iframe
    width="%(width)s"
    height="%(height)s"
    src="https://www.youtube.com/embed/%(embed_id)s"
    frameborder="0"
    allowfullscreen>
</iframe>
"""


# noinspection PyUnusedLocal,PyPep8Naming
def youtube(name, args, options, content, lineno, contentOffset, blockText,
            state, stateMachine):
    """Embed a YouTube video."""

    # See http://jasonstitt.com/youtube-in-restructured-text

    if len(content) == 0:
        return

    # See http://stackoverflow.com/q/2618020 for defaults.
    context = {
        'embed_id': content[0],
        'width': "640px",
        'height': "505px",
    }

    extra_args = content[1:]  # Because content[0] is ID
    extra_args = [ea.strip().split("=") for ea in extra_args]  # key=value
    extra_args = [ea for ea in extra_args if len(ea) == 2]  # drop bad lines
    extra_args = dict(extra_args)

    if 'width' in extra_args:
        context['width'] = extra_args.pop('width')

    if 'height' in extra_args:
        context['height'] = extra_args.pop('height')

    return [nodes.raw('', WISTIA_TEMPLATE % context, format='html')]

youtube.content = True
directives.register_directive('youtube', youtube)

WISTIA_TEMPLATE = """
<div class="wistia_responsive_padding" style="padding:61.04%% 0 0 0;position:relative;">
<div class="wistia_responsive_wrapper" style="height:100%%;left:0;position:absolute;top:0;width:100%%;">
<iframe src="https://fast.wistia.net/embed/iframe/%(embed_id)s?videoFoam=true" allowtransparency="true" frameborder="0" scrolling="no" class="wistia_embed" name="wistia_embed" allowfullscreen mozallowfullscreen webkitallowfullscreen oallowfullscreen msallowfullscreen width="%(width)s" height="%(height)s"></iframe>
</div>
</div>
<script src="https://fast.wistia.net/assets/external/E-v1.js" async></script>
<br>
<br>
"""


# noinspection PyUnusedLocal,PyPep8Naming
def wistia(name, args, options, content, lineno, contentOffset, blockText,
           state, stateMachine):
    """Embed a Wistia video."""

    if len(content) == 0:
        return

    context = {
        'embed_id': content[0],
        'width': "100%",
        'height': "100%",
    }

    extra_args = content[1:]  # Because content[0] is ID
    extra_args = [ea.strip().split("=") for ea in extra_args]  # key=value
    extra_args = [ea for ea in extra_args if len(ea) == 2]  # drop bad lines
    extra_args = dict(extra_args)

    if 'width' in extra_args:
        context['width'] = extra_args.pop('width')

    if 'height' in extra_args:
        context['height'] = extra_args.pop('height')

    return [nodes.raw('', WISTIA_TEMPLATE % context, format='html')]

wistia.content = True
directives.register_directive('wistia', wistia)
