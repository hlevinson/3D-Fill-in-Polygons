# 3D-Fill-in-Polygons

Instructions:

- Activate environment `source activate 3dimage` (to list `conda env list`).
- To satisfy dependencies:

```python
conda install pip
pip install shapely, vispy
```

- `jupyter notebook` - to open notebook in browser.
 


## Key Files
- `parser.py`: parses voxels `seg_file.txt`
- `Polygonplay.ipynb`: Create grid from parsed voxel data
- `renderer.py`: `vispy/opengl` based renderer

## TODO
- Lalit: Make renderer a function
- Howard: Everything else
