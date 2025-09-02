# SALOME-Voronoi

Interface between Salome and Vorpalite from the [Geogram](https://github.com/BrunoLevy/geogram) programming library for polyhedral mesh generation. 
Note the Vorpalite program has many features (such as parallel tetrahedral meshing among other), but this script is primary intented for Centroidal Voronoi diagram computation.

![](https://github.com/MoiseRousseau/SALOME-Voronoi/blob/master/gallery/sample.png "Sample Voronoi diagram made from NETGEN-3D-2D-1D seeds")

## Installation

Below instructions were tested using Ubuntu 22.04 and Salome 9.14.
They should work for other Linux distributions without so much modifications.

1. Clone this repository on your computer.

2. Install Vorpalite dependencies: 
```
sudo apt install libboost-dev libcgal-dev libglu1-mesa-dev libxxf86vm-dev libxtst-dev libxrandr-dev libxinerama-dev libxcursor-dev doxygen cmake g++
```
3. Compile Vorpalite executable using the dedicated script `install_vorpalite.sh`. Note that you can use more recent version of geogram if you wish.

4. Add Vorpalite and the Voronoi plugin to `salome` launcher. For instance:

```
    #[geogram]
    context.addToPath(r"/opt/geogram/bin")
    context.setVariable(r"GEOGRAMPLUGIN_ROOT_DIR", r"/opt/salome/SALOME-Voronoi")
    context.setVariable(r"SMESH_PYPLUGIN_DIR", r"${GEOGRAMPLUGIN_ROOT_DIR}", overwrite=True)
    context.addToPythonPath(r"GEOGRAMPLUGIN_ROOT_DIR")
```

5. Your plugin is operational. You can now start converting meshes with the menu `Mesh/Plugins/Voronoi/Convert to Voronoi` or the toolbar icon <img src="mesh_plugins_geogram.png" width="32px" alt="Voronoi plugin icon">.


## Use the plugin

0. Launch plugin GUI with `Mesh/Plugins/Voronoi/Convert to Voronoi`.

1. (Mandatory) Select the boundary mesh. This mesh will define the boundary of the Voronoi diagram. Only the 2D elements will be used.

2. (Optional) Select the seeds mesh. This mesh will define the seeds from where the Voronoi cell will be computed. Only the node will be used. If no mesh is specified, Vorpalite will create and optimize the seeds and their locations to create a Centroidal Voronoi Diagram.

3. Type the parameter to pass to Vorpalite. By default, Vorpalite is set to polygonal meshing mode (`profile=poly`), generate unique ids for the vertices (`generate_ids=true`) and will merge the boundary the with same normal (`simplify=tets_voronoi_boundary`). If no seeds mesh is specified, you should add the command `nb_pts=X` to create X seeds. A description of available parameter can be found by running in a terminal `vorpalite -h`

4. Check "Create groups from seeds mesh nodes group" to create groups of volume based on the existing nodes groups in your seed mesh.

5. Click OK to launch the Voronoi Diagram computation.

6. Go back to the terminal to have a look at the output of vorpalite while it generates the mesh.

7. Once the mesh generation is finished, the mesh is automatically imported in SALOME MESH with the `_Voronoi` suffix name. Click on the eye next to it to display it.


## Examples

### Subsurface flow simulation in backfilled open-pits

Comparison of a 50K elements tetrahedral and polyhedral meshes.
Polyhedral mesh was generated in nearly 60 seconds on a i7-6820HQ machine given the domain boundary and argument `n_pts=50000` to Vorpalite.
![](https://github.com/MoiseRousseau/SALOME-Voronoi/blob/master/gallery/backfilled_pit.png "Sample Voronoi diagram made from NETGEN-3D-2D-1D seeds")

If you make beautiful meshes with my script, please send me picture of it so I can add it here!


## Authors

* **Moïse Rousseau** - *Initial work*

## Getting involved

Feel free to contact me if you have problems or comments, it will help me to improve the plugin.

## Further reading

* https://link.springer.com/chapter/10.1007%2F978-3-030-23436-2_3
* http://alice.loria.fr/
* http://alice.loria.fr/index.php/erc-vorpaline.html

## License

File in this repository are licensed under the GPL version 3 License - see the [LICENSE.md](LICENSE.md) file for details. About the Vorpalite program and Geogram library, please see this [page](http://alice.loria.fr/software/geogram/doc/html/geogram_license.html).
