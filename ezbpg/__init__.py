from ezbpg.ioutil import purify, csviter
from ezbpg.matcher import Matcher

def ingest(edgeseq):
    return Matcher(edgeseq)

def slurp(path):
    edgeseq = purify(csviter(path))
    return ingest(edgeseq)
