#note that this trick won't currently work in the binder
import os
import pickle
import pyvista as pv
import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.facecolor'] = 'black'

with open(r'J:\downlist.pkl','rb') as fd:
    downlist = pickle.load(fd)
    
for dl in downlist:
    #print(dl.shape)
    for x in dl:
        for y in x:
            #print(len(y), y, type(y))
            if 'wm' in y[0]:
                y[0] = 'wm'
            if 'Cbr' in y[0] or 'Cbn' in y[0] or 'Cbo' in y[0]:
                y[0] = 'W'
            if 'R' in y[0]:
                #print(y)
                if 'P' in y[0] or 'L' in y[0]:
                    y[0] = 'W'
                else:
                    y[0] = 'R'
            if 'CH' in y[0]:
                y[0] = 'CH'
            if 'D' in y[0]:
                y[0] = y[0][0:1]
            if 'C' in y[0] and 'CH' not in y[0]:
                y[0] = y[0][0:1]
    
darray = np.full((downlist[0].shape[0],downlist[0].shape[1],len(downlist)), 'B', dtype='U10')    
#d_int = np.full((downlist[0].shape[0],downlist[0].shape[1],len(downlist)), np.nan)    #good for xarray plot
d_int = np.full((downlist[0].shape[0],downlist[0].shape[1],len(downlist)), -999)    #good for 3D plot

for index, d in enumerate(downlist):
    darray[:,:,index] = downlist[index][:,:,0]
    
dmap = {}
dmap['O'] = 0
dmap['C'] = 1
dmap['Cbr'] = 6
dmap['Cbo'] = 6
dmap['Cbn'] = 6
dmap['R'] = 2
dmap['W'] = 6
dmap['D'] = 3
dmap['CH'] = 4
dmap['wm'] = 5
dmap['cm'] = 5
dmap['ch'] = 5
dmap['st'] = 5
dmap['ar'] = 5
dmap['sp'] = 5
dmap['pt'] = 5
dmap['td'] = 5

for key in dmap:
    d_int[np.where(darray == key)] = dmap[key]

da = xr.DataArray(data=d_int,dims=["x","y","z"],
                  coords=dict(x=(["x"],range(0,downlist[0].shape[0])), y=(["y"],range(0,downlist[0].shape[1])), z=(["z"],range(0,len(downlist)))  )   )       

import matplotlib.pyplot as plt
plt.rcParams['axes.facecolor'] = 'black'

fg = da.plot(x='x',y='y',col='z',levels=[0,1,2,3,3,4,5,6],colors=["green","white","gray","brown","brown","red","blue"], size=4,aspect=downlist[0].shape[0]/downlist[0].shape[1])

grid = pv.UniformGrid()

#cell data
grid.dimensions = np.array(darray.shape) + 1
grid.spacing=(1,1,1)
grid.cell_data["map"] = d_int.flatten(order="F")
grid.plot()

plotter = pv.Plotter(notebook=False)
annotations={0:"Out",1:"C",2:"R",3:"D",4:"CH",5:"Bad",6:"Wet"}
#plotter.show_axes()
#plotter.show_bounds(grid=True)
plotter.add_mesh(grid,cmap=["green","white","gray","brown","brown","red","blue"],nan_color='black',annotations=annotations,nan_opacity=0,opacity=0.5,style='wireframe')
plotter.show()

#to remove all the empty default cells, use ghost cells
ghost = grid.cast_to_unstructured_grid()

ghosts = np.argwhere(grid["map"] == -999)

# This will act on the mesh inplace to mark those cell indices as ghosts
ghost = ghost.remove_cells(ghosts)
ghost

pv.global_theme.background = 'black'
plotter = pv.Plotter(notebook=False)
annotations={0:"Out",1:"C",2:"R",3:"D",4:"CH",5:"Bad",6:"Wet"}
#plotter.show_axes()
#plotter.show_bounds(grid=True)
#plotter.add_mesh(ghost,cmap=["green","white","gray","brown","brown","red","blue"],nan_color='black',annotations=annotations,nan_opacity=0,opacity=0.5,style='wireframe')
plotter.add_mesh(ghost,cmap=["green","white","gray","brown","brown","red","blue"],nan_color='black',annotations=annotations, scalars='map')
#plotter.add_mesh(ghost,cmap="Spectral",nan_color='black',annotations=annotations,nan_opacity=0,opacity=0.3,style='wireframe')
plotter.show()

ghost.save('ghost.vtu')


