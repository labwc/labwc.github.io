#!/usr/bin/env python3

import sys
import re

headings = re.compile('<(h[12])>([^<]*)</h[12]>')
strong = re.compile('<p><strong>([^<]*)</strong>')
HEADING_LEVELS = { 'h1': 0, 'h2': 1 }
PERMA_LINK_CHAR='🔗'

def build_loc(sections):
	# Build index on top of the man page
	out = list()
	yield '<div class="LOC">'
	for lvl, text, link in sections:
		if lvl == 0:
			continue
		out.append(f'<a href="#{link}">{text.capitalize()}</a>')
	yield ' | '.join(out)
	yield '</div>'

def add_header_ids(buf):
	# Add on-hover perma links for headers
	sections = list()
	for match in headings.finditer(buf):
		all, el, value = (match.group(x) for x in range(3))
		target = value.lower().replace(' ', '_')
		sections.append((HEADING_LEVELS[el], value, target))
		buf = buf.replace(all, f'<{el} id="{target}">' +
			f'<a class="perma" href="#{target}">{PERMA_LINK_CHAR}</a>{value}</{el}>')
	buf = buf.replace('<!--%%%TOC%%%-->', '\n'.join(build_loc(sections)))
	return buf

def add_item_ids(buf):
	# Add on-hover perma links for entries other than headers
	for match in strong.finditer(buf):
		all, value = (match.group(x) for x in range(2))
		target = f'entry_{value.lower()}'
		for repl in (' ', '&gt;'):
			target = target.replace(repl, '_')
		for repl in ('"', "'", '&lt;', '\n', '/'):
			target = target.replace(repl, '')
		target = target.rstrip('_')
		buf = buf.replace(all, f'<p><strong id="{target}">' +
			f'<a class="perma" href="#{target}">{PERMA_LINK_CHAR}</a>{value}</strong>')
	return buf

def fix_bullet_formatting(buf):
	# Really ought to try to understand+fix this upstream,
	# but for now, let's just get it working
	return buf.replace("·</p>\n<p>", "· ")

def main(argv):
	with open(argv[0], 'r') as file:
		buf = file.read()

	buf = fix_bullet_formatting(buf)
	buf = add_header_ids(buf)
	buf = add_item_ids(buf)

	with open(argv[0], 'w') as file:
		file.write(buf)

if __name__ == "__main__":
	main(sys.argv[1:])

