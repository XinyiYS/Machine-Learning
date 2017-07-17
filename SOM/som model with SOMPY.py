import sompy
from sklearn.externals import joblib

from SOM import DPP


def build_som_model(data, n_row=20,n_col=30,train_info='info'):
    print('start building the model')
    map_size = [n_row,n_col]
    som = sompy.SOMFactory.build(data, map_size, mask=None, mapshape='planar', lattice='rect', normalization='var',
                                 initialization='pca', neighborhood='bubble', training='batch',
                                 name='sompy')
    som.train(n_job=-1, verbose=train_info) # train_info have 'info',None and 'debug'
                                            # n_job = -1 to maximize speed
    print('model build complete')
    return som


def init_view_map(som, n_row = 50,n_col = 50):
    # currently using default settings
    v = sompy.mapview.View2DPacked(n_row, n_col, '2D Packed View', text_size=8)
    v.show(som, what='codebook', which_dim='all', cmap=None, col_sz=6)  # which_dim='all' default
    return v

def init_hit_map(som,n_clusters, color_labels = ['r','g','b','k','c','m','y','w']):
    # cl = som.cluster(n_clusters)
    som.cluster(n_clusters)
    h = sompy.hitmap.HitMapView(10, 10, 'hitmap', text_size=8, show_text=True)
    h.show(som)
    return

dpp = DPP.DPP(data_dir='dataOut.txt')
data_to_process, chosen_attributes = dpp.get_data()

som = build_som_model(data_to_process, train_info=None)
joblib.dump(som,'SOMPY_som_model.pkl')
v = init_view_map(som)
init_hit_map(som, 5)
colors = ['r','c','b','k','m','y']*10

my_model_loaded = joblib.load('SOMPY_som_model.pkl')
print(my_model_loaded)
