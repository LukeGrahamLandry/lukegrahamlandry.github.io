import markdown, os
from pygments import lexers
from pygments import highlight 
from pygments.formatters import HtmlFormatter
import re
from xml.sax import saxutils as su

lex = lexers.get_lexer_by_name("java")
formatter = HtmlFormatter()

with open("template.html", "r") as f:
    template = "".join(f.readlines())

header = template.split("|")[0]
footer = template.split("|")[1]



ignore = ["about.md", "support.md", "my-mods.md", "contact.md"]
tutorials = ["java-basics", "environment-setup", "basic-items", "advanced-items", "basic-blocks", "advanced-blocks", "tools-armor", "tile-entities"]

for root, dirs, files in os.walk("../forge-1.16-tutorial-src", topdown=False):
   for name in files:
        if (".md" not in name):
            continue

        with open(root + "/" + name, "r") as f:
            md_content = "".join(f.readlines())
        html_content = markdown.markdown(md_content)

        
        code_parts = html_content.split("<code>")
        html_syntax_highlighted = code_parts[0]
        del code_parts[0]

        for part in code_parts:
            code = part.split("</code>")[0]
            code = su.unescape(code)
            end = part.split("</code>")[1]

            styled_code = highlight(code, lex, formatter)

            
            styled_code = styled_code.split('<div class="highlight"><pre>')[1]
            styled_code = styled_code.split('</div>')[0]


            html_syntax_highlighted += '<code class="highlight">'
            html_syntax_highlighted += styled_code
            html_syntax_highlighted += "</code>"
            html_syntax_highlighted += end

        full_content = header + html_syntax_highlighted + footer

        title = ".".join(name.split(".")[:-1])
        filename_to_write = title + ".html"
        with open("../" + filename_to_write, "w") as f:
            f.write(full_content)

        # ugly hack
        os.mkdir("../" + title)
        with open("../" + title + "/index.html", "w") as f:
            f.write(full_content)


with open("../code.css", "w") as f:
     f.write(formatter.get_style_defs())

with open("index.html", "r") as f:
    content = "".join(f.readlines())

with open("../index.html", "w") as f:
    f.write(content.split("|")[0] + str(tutorials) + content.split("|")[1])

