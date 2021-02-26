import pandas as pd
import spacy
from spacy.tokens import Span

def display_ner(doc, include_punct=False):
    """Generate data frame for visualization of spaCy doc with custom attributes."""

    rows = []
    for i, t in enumerate(doc):
        if not t.is_punct or include_punct:
            row = {'token': i, 
                   'text': t.text, 'lemma': t.lemma_, 
                   'pos': t.pos_, 'dep': t.dep_, 'ent_type': t.ent_type_,
                   'ent_iob_': t.ent_iob_}
            
            if doc.has_extension('has_coref'):
                if doc._.coref_clusters is not None and \
                   t.has_extension('in_coref') and t._.in_coref: # neuralcoref attributes
                    row['in_coref'] = t._.in_coref
                    row['main_coref'] = t._.coref_clusters[0].main.text
                else:
                    row['in_coref'] = None
                    row['main_coref'] = None
            if t.has_extension('ref_n'): # referent attribute
                row['ref_n'] = t._.ref_n
                row['ref_t'] = t._.ref_t
            if t.has_extension('ref_ent'): # ref_n/ref_t
                row['ref_ent'] = t._.ref_ent
            rows.append(row)
    
    df = pd.DataFrame(rows).set_index('token')
    df.index.name = None
    
    return df


def reset_pipeline(nlp, pipes):
    # remove all custom pipes
    custom_pipes = [pipe for (pipe, _) in nlp.pipeline
                    if pipe not in ['tagger', 'parser', 'ner',
                                    'tok2vec', 'attribute_ruler', 'lemmatizer']]
    for pipe in custom_pipes:
        _ = nlp.remove_pipe(pipe)
    # re-add specified pipes
    for pipe in pipes:
        if 'neuralcoref' == pipe or 'neuralcoref' in str(pipe.__class__):
            nlp.add_pipe(pipe, name='neural_coref')
        else:
            nlp.add_pipe(pipe)

    print(f"Model: {nlp.meta['name']}, Language: {nlp.meta['lang']}")
    print(*nlp.pipeline, sep='\n')


def print_dep_tree(doc, skip_punct=True):
    """Utility function to pretty print the dependency tree."""
    
    def print_recursive(root, indent, skip_punct):
        if not root.dep_ == 'punct' or not skip_punct:
            print(" "*indent + f"{root} [{root.pos_}, {root.dep_}]")
        for left in root.lefts:
            print_recursive(left, indent=indent+4, skip_punct=skip_punct)
        for right in root.rights:
            print_recursive(right, indent=indent+4, skip_punct=skip_punct)

    for sent in doc.sents: # iterate over all sentences in a doc
        print_recursive(sent.root, indent=0, skip_punct=skip_punct) 


# acronyms created after cooccurrence analysis
_acronyms = {
    'AMC': 'American Motors Corp',
    'AMI': 'American Medical International Inc',
    'ARCO': 'Atlantic Richfield Co',
    'BIL': 'Brierley Investments Ltd',
    'BP': 'British Petroleum Co Plc',
    'BPI': 'Banco Portugues de Investmento Sarl',
    'CGCT': 'Cie Generale de Constructions',
    'DAF': 'Delhi Australia Fund',
    'EC': 'European Community',
    'ETL': 'Equiticorp Tasman Ltd',
    'FCC': 'Federal Communications Commission',
    'FDA': 'Food and Drug Administration',
    'FHLBB': 'Federal Home Loan Bank Board',
    'FIRB': 'Foreign Investment Review Board',
    'FTC': 'Federal Trade Commission',
    'ICC': 'Interstate Commerce Commission',
    'IDC': 'International Digital Communications Planning Inc',
    'ITJ': 'International Telecom Japan Inc',
    'KDD': 'Kokusai Denshin Denwa Co Ltd',
    'PCGG': 'Presidential Commission on Good Government',
    'PSA': 'Pacific Southwest Airlines',
    'SMC': 'San Miguel Corp',
    'TWA': 'Trans World Airlines Inc',
    'UCPB': 'United Coconut Planters Bank'
}

# add acronyms (all acronyms are organizations)
alias_lookup = {acro: (text, 'ORG') for (acro, text) in _acronyms.items()}

alias_lookup['SEC'] = ('Securities and Exchange Commission', 'GOV')
    
alias_list = {('U.S. Department of Justice', 'GOV'): 
                ['U.S. Department of Justice',
                 'Department of Justice', 
                 'U.S. Justice Department', 
                 'Justice Department'],
              ('U.S. Department of Transportation', 'GOV'): 
                ['U.S. Department of Transportation',
                 'U.S. Transportation Department',
                 'Department of Transportation',
                 'Transportation Department',
                 'DOT'],
              ('USAir Group Inc', 'ORG'):
                ['USAir Group Inc', 'USAir Group Inc.',
                 'US Air Corp', 'US Air Corp.',
                 'USAir Group', 'USAir Group Inc', 'USAir Group Inc.',
                 'US Air', 'USAir', 'U.S. Air', 'USAIR Group',
                 'U.S. Air Group Inc.'],
              ('Trans World Airlines Inc', 'ORG'):
                ['Transworld Airlines', 'Transworld Airlines Inc', 'Trans World Airlines'],
}         

# invert alias_list; overwrites entries in acronyms like DOT
alias_lookup.update({alias: ent for (ent, aliases) in alias_list.items() 
                                for alias in aliases})
