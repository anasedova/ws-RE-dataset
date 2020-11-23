import pytest
import spacy
import json
from scripts.PatternSearch import PatternSearch
from scripts.commons import DYGIE_RELATIONS

nlp = spacy.load("en_core_web_sm")


@pytest.fixture(scope='session')
def get_spacy_pattern_search_data():
    sent = "Turner Sports. Turner Sports (TS) is the division of Turner Broadcasting System (a subsidiary of AT&T) responsible for sports broadcasts on Turner channels including TBS, TNT, TruTV, and CNN en Español (for occasional Spanish language simulcasts), and for operating the digital media outlets NCAA.com, NBA.com, PGATOUR.com and PGA.com. Turner Sports also operates NBA TV on behalf of the National Basketball Association."
    ann_sent = nlp(sent).to_json()
    page_annotation = [{**{"doc_id": "1507"}, **ann_sent}]
    # page_annotation_json = json.dump(page_annotation)
    ps = PatternSearch("../data/output/spacy", "../data/patterns.txt", "../data/output")
    return [
                [
                    ps,
                    page_annotation,
                    "../",
                    {"doc_key":"1507","sentences":[["Turner","Sports"],["Turner","Sports","(","TS",")","is","the","division","of","Turner","Broadcasting","System","(","a","subsidiary","of","AT&T",")","responsible","for","sports","broadcasts","on","Turner","channels","including","TBS",",","TNT",",","TruTV",",","and","CNN","en","Español","(","for","occasional","Spanish","language","simulcasts",")",",","and","for","operating","the","digital","media","outlets","NCAA.com",",","NBA.com",",","PGATOUR.com","and","PGA.com","."],["Turner","Sports","also","operates","NBA","TV","on","behalf","of","the","National","Basketball","Association","."]],"relations":[[],[[11,13,18,18,"1"]],[]],"tokensToOriginalIndices":[[[0,6],[7,13]],[[15,21],[22,28],[29,30],[30,32],[32,33],[34,36],[37,40],[41,49],[50,52],[53,59],[60,72],[73,79],[80,81],[81,82],[83,93],[94,96],[97,101],[101,102],[103,114],[115,118],[119,125],[126,136],[137,139],[140,146],[147,155],[156,165],[166,169],[169,170],[171,174],[174,175],[176,181],[181,182],[183,186],[187,190],[191,193],[194,201],[202,203],[203,206],[207,217],[218,225],[226,234],[235,245],[245,246],[246,247],[248,251],[252,255],[256,265],[266,269],[270,277],[278,283],[284,291],[292,300],[300,301],[302,309],[309,310],[311,322],[323,326],[327,334],[334,335]],[[336,342],[343,349],[350,354],[355,363],[364,367],[368,370],[371,373],[374,380],[381,383],[384,387],[388,396],[397,407],[408,419],[419,420]]],"annotatedPredicates":[[],["1"],[]]}
                ]
            ]


def test_spacy_pattern_search_data(get_spacy_pattern_search_data):
    for data in get_spacy_pattern_search_data:
        assert PatternSearch.search_patterns(data[0], data[1], data[2]) == data[3]