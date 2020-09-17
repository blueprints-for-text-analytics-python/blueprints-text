import pandas as pd
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from umap import UMAP
import plotly.express as px
import plotly.graph_objs as go

def plot_embeddings(model, search=[], topn=0, show_all=False, train_all=False, 
                    labels=False, colors=True, n_dims=2, algo='pca', **kwargs):

    def closest(word, model, search, topn):
        """Find the closest word in a given list of search words, if in top-n."""
        closest_word = model.most_similar_to_given(word, search)
        if word == closest_word or \
           word in [w for w, _ in model.most_similar(closest_word, topn=topn)]:
            return closest_word 
        else:
            return 'other'

    # eliminate kwargs of other methods if supplied
    if algo != 'tsne': ###
        kwargs.pop('perplexity', None) ###
    if algo != 'umap': ###
        kwargs.pop('n_neighbors', None) ###
        kwargs.pop('min_dist', None) ###
        kwargs.pop('spread', None) ###

    # define the reducer
    if algo == 'umap':
        reducer = UMAP(n_components=n_dims, metric='cosine', **kwargs)
    elif algo == 'tsne':
        reducer = TSNE(n_components=n_dims, **kwargs)
    else:
        reducer = PCA(n_components=n_dims, **kwargs)

    if len(search) == 0: # no search words: show all
        show_all = True
    if show_all:  # to show all, all must be trained
        train_all = True
        
    # identify words to plot
    if show_all:
        words = [w for w in model.vocab]
    else:
        words = search + [sim_word for w in search 
                         for sim_word, _ in model.most_similar(w, topn=topn)]
        words = list(set(words)) # make word list it unique for t-SNE

    # reduce
    wv = [model[word] for word in words]
    if not train_all:
        print(f"Calculating {algo} for {len(words)} words ...", end="") 
        reduced_wv = reducer.fit_transform(wv)
    else:
        print(f"Calculating {algo} for {len(model.vocab)} words ...", end="") 
        reducer.fit(model.vectors)
        reduced_wv = reducer.transform(wv)
    print(f" done.") ###

    # create data frame for ploty express visualization
    # with x, y (, z) and meta data for styling
    if n_dims == 2:
        df = pd.DataFrame.from_records(reduced_wv, columns=['x', 'y'])
    else:
        df = pd.DataFrame.from_records(reduced_wv, columns=['x', 'y', 'z'])

    df['word']  = words
    params = {}

    if show_all:
        df['size'] = 1
        params.update({'size_max': 3, 'size': 'size' })
    else:
        df['size'] = df['word'].map(lambda w: 30 if w in search else 5)
        params.update({'size': 'size'})

    if len(search) > 0: # colorize with closest search word
        df['label'] = df['word'].map(lambda w: w if labels or w in search else '')
        params.update({'text': 'label'})
        if colors:
            df['color'] = df['word'].apply(closest, model=model, search=search, topn=topn)
            params.update({'color': 'color'})

    params.update({'hover_data': {c: False for c in df.columns}, 'hover_name': 'word'})

    # generate scatter plot
    if n_dims == 2:
        params.update({'width': 800, 'height': 400})
        fig = px.scatter(df, x="x", y="y", opacity=0.3, **params)
        fig.update_xaxes(showticklabels=False, showgrid=True, title='', zeroline=False, visible=True)
        fig.update_yaxes(showticklabels=False, showgrid=True, title='', zeroline=False, visible=True)
    else:
        params.update({'width': 900, 'height': 700})
        df['z'] = df['z']*2/3 # scale 3d box
        fig = px.scatter_3d(df, x="x", y="y", z="z", opacity=0.5, **params)
        fig.update_layout(scene = dict(xaxis = go.layout.scene.XAxis(title = '', showticklabels=False),
                                       yaxis = go.layout.scene.YAxis(title = '', showticklabels=False),
                                       zaxis = go.layout.scene.ZAxis(title = '', showticklabels=False)))
    fig.update_traces(textposition='middle center', marker={'line': {'width': 0}})
    fig.update_layout(font=dict(family="Franklin Gothic", size=12, color="#000000"))
    fig.show()
    return fig
