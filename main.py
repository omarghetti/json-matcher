import ijson
import json


## Method takes the two files and cycles through items to generate dict containing matches details
## we are just using lemmas from tokens and lemmas from the definition, discarding everything else to reduce memory usage
## An ulterior optimization could be made using "dep" field in token Items

def get_matches(file1, file2):
    definitions = ijson.items(open(file2), 'item.term_lemmas')
    matches = []
    for index, element in enumerate(definitions):
        documents = ijson.items(open(file1), "item.analyzed_doc.tokens")
        for doc_index, doc_element in enumerate(documents):
            tokens = [x['lemma'] for x in doc_element]
            for i in range(len(tokens)-len(element)):
                if tokens[i:i+len(element)] == element:
                    new_match = {
                        'doc_id': doc_index + 1,
                        'definition_id': index + 1,
                        'start': doc_element[i]['start'],
                        'end': doc_element[i+len(element)-1]['end']
                    }
                    matches.append(new_match)
    with open('sample-data/matches.json', 'a') as f:
        f.writelines(json.dumps(matches, ensure_ascii=False, indent=4),)
        f.close()



if __name__ == '__main__':
    get_matches('sample-data/documents.json', 'sample-data/definitions.json')
