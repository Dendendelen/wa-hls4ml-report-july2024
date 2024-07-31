import matplotlib.pyplot as plt
import numpy as np
import os

def plot_histogram(y_mlp, y_gnn, name, x_axis, filename, folder_name, log=False):
    ''' plot a single histogram '''

    rms_mlp = np.sqrt(np.mean(np.square(y_mlp)))
    rms_gnn = np.sqrt(np.mean(np.square(y_gnn)))

    plt.figure(figsize=(10,6))
    _, bins, _  = plt.hist(y_mlp, 20, color='gold', alpha=1.0, label="MLP (RMSE = "+"{0:.3f}".format(rms_mlp)+")")
    plt.hist(y_gnn, bins=bins, color='teal', alpha=0.7, label="GNN (RMSE = "+"{0:.3f}".format(rms_gnn)+")")
    plt.legend(loc='upper right') 

    plt.title(name)
    plt.ylabel('Number')
    plt.xlabel(x_axis)

    directory = folder_name+'/histograms/'

    if not os.path.exists(directory):
        os.makedirs(directory)

    if log:
        plt.yscale('log')
        plt.savefig(directory+filename+'_log_hist.pdf')
    else:
        plt.savefig(directory+filename+'_hist.pdf')

    plt.close()


def plot_histograms(output_features, folder_name):
    '''Plot all histograms for features '''

    i = 0

    for feature in output_features:

        feature_diff_mlp = np.load("mlp/"+feature+".npy")
        feature_diff_gnn = np.load("gnn/"+feature+".npy")

        plot_histogram(feature_diff_mlp, feature_diff_gnn, 'Residual of '+feature, 'Error of '+feature, feature, folder_name, False)
        plot_histogram(feature_diff_mlp, feature_diff_gnn, 'Log Residual of '+feature, 'Error of '+feature, feature, folder_name, True)

        print("Finished plots for "+feature)

        i += 1

output_features = ["WorstLatency_hls", "IntervalMax_hls", "FF_hls", "LUT_hls", "BRAM_18K_hls", "DSP_hls"]
plot_histograms(output_features, "testing_hist")