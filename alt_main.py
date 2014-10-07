# Alternative version of main.py
# just to illustrate map/filter techniques from Python

MAPPING = {
    'Gene': 'TAIR10_loci',
    'Pseudogene': 'TAIR10_pseudogenes',
    'TransposableElement': 'TAIR10_transposons',
    'TransposableElementGene': 'TAIR10_transposons',
    'MRNA': 'TAIR10_gene_models',
    'miRNA': 'TAIR10_ncrnas',
    'rRNA': 'TAIR10_ncrnas',
    'snRNA': 'TAIR10_ncrnas',
    'snoRNA': 'TAIR10_ncrnas',
    'tRNA': 'TAIR10_ncrnas'
}

def process(arg):
    new_tracks = filter(
        None, [MAPPING.get(elt) for elt in arg['location']['tracks']])
    if new_tracks:
        arg['location']['tracks'] = new_tracks
        return arg
