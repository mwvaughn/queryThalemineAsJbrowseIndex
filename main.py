import json

# GET text query to ThaleMine names API, return JSON with 
# tracks transformed into Jbrowse index namespace

# 3702 is the species domain
# startswith is a search mode, alternative is equals
# There are no other search modes
# Term is a freetext term

# url='https://apps.araport.org/thalemine/service/jbrowse/names/3702'
# json_path='location.tracks'
# arg: {"location":{"ref":"Chr4","start":13038360,"objectName":"AT4G25530","tracks":["SequenceFeature","Gene"],"end":13042443},"name":"FWA"}

def map_filter(arg):

        nutrax = []
        traxfound = 0

        for track in arg['location']['tracks']:
            if track == 'Gene':
                nutrax.append('TAIR10_loci')
                traxfound = traxfound + 1
            if track == 'Pseudogene':
                nutrax.append('TAIR10_pseudogenes')
                traxfound = traxfound + 1
            if track == 'TransposableElement':
                nutrax.append('TAIR10_transposons')
                traxfound = traxfound + 1
            elif track == 'TransposableElementGene':
                nutrax.append('TAIR10_transposons')
            	traxfound = traxfound + 1
            elif track == 'MRNA':
                nutrax.append('TAIR10_gene_models')
                traxfound = traxfound + 1
            elif (track == 'miRNA' or track == 'rRNA' or track == 'snRNA' or track == 'snoRNA' or track == 'tRNA'):
                nutrax.append('TAIR10_ncrnas')
                traxfound = traxfound + 1
                
        # Return a JSON stanza only if any of the conforming track types were found    
        if traxfound >= 1:
            arg['location']['tracks'] = nutrax
#            print json.dumps(arg, indent=4)
            return arg
