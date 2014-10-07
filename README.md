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

The "queryThalemineAsJbrowseIndex" ADAMA service transforms the tracks array in the resulting JSON objects to use track names that are congruent with AIP's current Jbrowse instance. 

{"location":
    {"ref":"Chr1",
     "start":658657,
     "objectName":"AT1G02920",
     "tracks":["TAIR10_loci"],
     "end":659771},
 "name":"glutathione S-transferase 7"}
 ```

# Example invocation and response

export NS=vaughn-dev
export GITHUB_UNAME=mwvaughn
export API=https://adama-dev.tacc.utexas.edu/community/v0.3
export TOKEN=<insert your AIP OAuth2 token here>

curl -sk -L -H "Authorization: Bearer $TOKEN" "$API/$NS/query_thalemine_as_jbrowse_index_v0.1/search?startswith=FWA"

{"result":[
    {"location":
        {"start":13038360,
         "tracks":["TAIR10_loci"],
         "end":13042443,
         "ref":"Chr4",
         "objectName":"AT4G25530"},
     "name":"FWA"},
    {"location":
        {"start":13038360,
         "tracks":["TAIR10_gene_models"],
         "end":13042443,
         "ref":"Chr4",
         "objectName":"AT4G25530.1"},
     "name":"FWA"}],
 "metadata":
    {},"status":"success"}
    
