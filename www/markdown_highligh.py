import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

class HighlightRenderer(mistune.Renderer):

    def block_code(self, code, lang):

        guess = 'python3'
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                   mistune.escape(code)
        if code.lstrip().startswith('<?php>'):
            guess = 'php'
        elif code.lstrip().startswith('<'):
            guess = 'html'
        elif code.lstrip().startswith(('function','var','$')):
            guess = 'javascript'

        lexer = get_lexer_by_name(lang or guess,stripall=True)
        formatter = HtmlFormatter()
        return highlight(code,lexer,formatter)

renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)

def formatter(content):
    return markdown(content)

