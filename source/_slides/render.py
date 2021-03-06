#!/usr/bin/env python

import argparse
import codecs
import jinja2
import markdown

# extensions = ['extra', 'nl2br']
extensions = ['extra']

def process_slides(input, output):
    with codecs.open(output, 'w', encoding='utf8') as outfile:
        md = codecs.open(input, encoding='utf8').read()

        md_slides = md.split('\n---\n')
        # The first slide is always the header information for the slides
        header_info = parse_metadata(md_slides[0].strip())
        # Only use the slides after the first one
        md_slides = md_slides[1:]

        print 'Compiled %s slides.' % len(md_slides)

        slides = []

        # Process each slide separately.
        for md_slide in md_slides:
            slide = {}
            sections = md_slide.split('\n\n')
            # Extract metadata at the beginning of the slide (look for key: value)
            # pairs.
            metadata_section = sections[0]
            metadata = parse_metadata(metadata_section)
            slide.update(metadata)
            remainder_index = metadata and 1 or 0
            # Get the content from the rest of the slide.
            content_section = '\n\n'.join(sections[remainder_index:])
            html = markdown.markdown(content_section, extensions)
            slide['content'] = postprocess_html(html, metadata)

            slides.append(slide)

        template = jinja2.Template(open('base.html').read())

        outfile.write(template.render(locals()))


def parse_metadata(section):
    """Given the first part of a slide, returns metadata associated with it."""
    metadata = {}
    metadata_lines = section.split('\n')
    for line in metadata_lines:
        colon_index = line.find(':')
        if colon_index != -1:
            key = line[:colon_index].strip()
            val = line[colon_index + 1:].strip()
            metadata[key] = val

    return metadata


def postprocess_html(html, metadata):
    """Returns processed HTML to fit into the slide template format."""
    if metadata.get('build_lists') and metadata['build_lists'] == 'true':
        class_attr = 'build'
        if metadata.get('fade') and metadata['fade'] == 'true':
            class_attr += ' fade'
        html = html.replace('<ul>', '<ul class="' + class_attr + '">')
        html = html.replace('<ol>', '<ol class="' + class_attr + '">')
    return html


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--output", dest="outfilename",
                      help="write output to FILE", metavar="OUTFILE")
    parser.add_argument("-i", "--input", dest="infilename",
                      help="write input to FILE", metavar="INFILE")

    args = parser.parse_args()

    process_slides(args.infilename, args.outfilename)
