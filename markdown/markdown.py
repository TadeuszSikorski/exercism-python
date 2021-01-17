import re


IMPORTANT_TEXT = re.compile(r"__(.*)__")
EMPHASIZED_TEXT = re.compile(r"_(.*)_")
ORDERED_LIST = re.compile(r"^\* (.*)", flags=re.MULTILINE)
HEADER = re.compile(r"^(#{1,6}) (.*)$", flags=re.MULTILINE)
UNORDERED_LIST = re.compile(r"(\n?<li>.*</li>)", flags=re.S)
PARAGRAPH = re.compile(r"^(?!<[hlu])(.*?$)", flags=re.MULTILINE)


def parse(markdown):
    markdown = IMPORTANT_TEXT.sub(r"<strong>\1</strong>", markdown)
    markdown = EMPHASIZED_TEXT.sub(r"<em>\1</em>", markdown)
    markdown = ORDERED_LIST.sub(r"<li>\1</li>", markdown)
    number = 0 if not HEADER.search(markdown) else len(HEADER.search(markdown).group(1))
    markdown = (markdown if number == 0 else HEADER.sub(f"<h{number}>" + r"\2" + f"</h{number}>", markdown))
    markdown = UNORDERED_LIST.sub(r"<ul>\1</ul>", markdown)
    markdown = PARAGRAPH.sub(r"<p>\1</p>", markdown)
    return "".join(markdown.splitlines())
