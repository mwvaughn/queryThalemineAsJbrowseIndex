Data API: queryThalemineAsJbrowseIndex
======================================

Objective: Query the Intermine Jbrowse names API and transform the result into the namespace used by the AIP Jbrowse index. Expects to pass parameter "startswith=$TERM" where TERM is the search term. An example would be

https://apps.araport.org/thalemine/service/jbrowse/names/3702?startswith=FWA

```
# Original query

{"location":
    {"ref":"Chr1",
     "start":658657,
     "objectName":"AT1G02920",
     "tracks":["SequenceFeature","Gene"],
     "end":659771},
 "name":"glutathione S-transferase 7"}

# Transformed response

{"location":
    {"ref":"Chr1",
     "start":658657,
     "objectName":"AT1G02920",
     "tracks":["TAIR10_loci"],
     "end":659771},
 "name":"glutathione S-transferase 7"}
 ```
