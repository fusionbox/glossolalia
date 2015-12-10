# -*- coding: utf-8 -*-
import argparse
import os
import polib

from .pseudo import types

PSEUDO_TYPE_CLASSES = {
    "brackets": types.BracketsPseudoType,
    "unicode": types.UnicodePseudoType,
    "planguage": types.PLanguagePseudoType,
    "extend": types.ExtendPseudoType,
    "mixed": types.MixedPseudoTypes
}


def translate(infile, outfile, type="mixed"):
    po = polib.pofile(infile)

    # Our fake language doesn't have any special plural forms, so remove
    # the placeholder.
    if po.metadata.get('Plural-Forms') == 'nplurals=INTEGER; plural=EXPRESSION;':
        del po.metadata['Plural-Forms']


    translator = PSEUDO_TYPE_CLASSES[type]("po")

    for entry in po:
        entry.msgstr = translator.compile(entry.msgid)

    po.save(outfile)


def main():
    parser = argparse.ArgumentParser(description="Create pseudo translation files.")
    parser.add_argument("infile", metavar="infile", help="the path to the source file")
    parser.add_argument("outfile", metavar="outfile", help="The path to save the psuedo translation to. Defaults to infile.", nargs='?')
    parser.add_argument("--type", dest="type", default="mixed", choices=PSEUDO_TYPE_CLASSES.keys(), help="The type of psuedo translation")

    args = parser.parse_args()

    translate(args.infile, args.outfile or args.infile, type=args.type)

if __name__ == "__main__":
    main()
