import os
import json
import collections

from markdownwriter import MarkdownWriter
from markdownwriter import MarkdownTable

markdown = MarkdownWriter()
markdown.addHeader('Netflix categories', 2)
markdown.addSimpleLineBreak()

def sort(dictionary):
    return collections.OrderedDict(sorted(dictionary.items()))

with open('categories.json', 'r') as f:
    categories = sort(json.loads(f.read()))

    for categoryName, categoryValue in categories.iteritems():
        if type(categoryValue) is dict:
            markdown.addHeader(categoryName, 4)

            table = MarkdownTable(["Subcategory", "URL"])
            for subcategoryName, subcategoryId in sort(categoryValue).iteritems():
                table.addRow([subcategoryName, 'https://www.netflix.com/browse/genre/%s' % subcategoryId])
            markdown.addTable(table)
            markdown.addSimpleLineBreak()


with open('README.md', 'w') as f:
    f.write(markdown.getStream())
