import markdown, os

with open("template.html", "r") as f:
    template = "".join(f.readlines())

header = template.split("|")[0]
footer = template.split("|")[1]

for root, dirs, files in os.walk("../forge-1.16-tutorial-src", topdown=False):
   for name in files:
        if (".md" not in name):
            continue

        with open(root + "/" + name, "r") as f:
            md_content = "".join(f.readlines())
        html_content = markdown.markdown(md_content)
        full_content = header + html_content + footer

        filename_to_write = ".".join(name.split(".")[:-1]) + ".html"
        with open("../" + filename_to_write, "w") as f:
            f.write(full_content)