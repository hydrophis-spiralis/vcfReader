

import pandas as pd


class VariantCall:
    def __init__(self,CHROM= None	,POS= None	,ID= None,	REF= None	,ALT= None,	QUAL= None,	FILTER= None,	INFO= None,*args, **kwargs):
        print(args)
        print(kwargs)


class VCFReader:
    def __init__(self, filename):
        self.file_handler = open(filename)
        self.read_header()

    def read_header(self):
        header = True
        self.header_lines = []
        while header:
            next_line = next(self.file_handler)
            if next_line.startswith('##'):
                self.header_lines.append(next_line)
            elif next_line.startswith('#'):
                break
            else:
                raise ValueError()

        self.table_header = next_line[1:].split('\t')

    def parse_header(self):
        list(filter(lambda x: x.startswith('##INFO'),  self.header_lines))

    def __iter__(self):
        return self

    def __next__(self):
        next_line = next(self.file_handler)
        cells = next_line.split('\t')
        return VariantCall(cells[0])

VariantCall(my_par = 10)

