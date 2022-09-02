<h2>pharmacophore selection using hydration site analysis</h2>
<p>This is an example to show how to use Flare 3D-RISM or GIST hydration site analyzation to select pharmacophore generated by Ligandscout.</p>

<h2>Sotfware</h2>
<h3>Flare V6: 3D-RISM and GIST</h3>
<p>Available from cresset: https://www.cresset-group.com/flare</p>

<h3>Ligandscout V4.4.9</h3>
<p>Available from inteligand: https://www.inteligand.com/ligandscout</p>

<h3>GridDataFormat</h3>
<p>Available : https://pypi.org/project/GridDataFormats</p>
<pre line="1" lang="python">
pip install GridDataFormats
</pre>
   
<h3>LXML</h3>
<p>Available: https://pypi.org/project/lxml</p>
<pre line="1" lang="python">
pip install lxml
</pre>

<h2>Examples</h2>
<h3>Show &Delta;G at a coordination point</h3>
<img src="https://github.com/gkxiao/gisttools/blob/master/example/benzene/gist.png">
<pre line="1" lang="python">
>>> from gridData import Grid
>>> g =  Grid("local_dG.dx")
>>> g.interpolated(77.363,25.254,44.668)
array([0.73119007])
>>> g.interpolated(77.882,28.203,40.039)
array([-0.23544697])
>>> g.interpolated(77.46,24.744,40.978)
array([0.00361614])
>>>
</pre>
<h3 id="ph4">Score a pharmacophore feature</h3>
<img src="https://github.com/gkxiao/gisttools/blob/master/example/benzene/gist_feature_score.png" width="400" height="363">
<pre line="1" lang="python">
>>> from gridData import Grid
>>> dG =  Grid("G:/work/3oot_gist/Local_unhappy_water.dx")
>>> # PDB 3OOT xtal-ligand O33 (oxygen of the HBD) 
>>> dG_O33 = dG.interpolated(-8.43,-28.11,-4.07)
>>> print('dG =',dG_O33,'kcal/mol')
dG = [1.52537911] kcal/mol
>>>
</pre>
<h3>Water density at a coordination point</h3>
<p>Show the water density at coordination point (-12.305, 42.442, 9.476) and (-9.244, 45.091, 6.068).</p>
<pre line="1" lang="python">
> dx_at_coord.py 1ke8_3drism_density.dx -12.305 42.442 9.476
-12.305 42.442 9.476 0.30545268630371786
> dx_at_coord.py 1ke8_3drism_density.dx -9.244 45.091 6.068
-9.244 45.091 6.068 3.234434937898573
</pre>
<h3>Jupyter notebook</h3>
<p>And jupyter notebook to show how to use 3D-RISM water density to score the features from the ligandscout pharmacophore model.</p>


<h2>Reference</h2>
<ol>
   <li>Hu, B.; Lill, M. A. Protein Pharmacophore Selection Using Hydration-Site Analysis. J. Chem. Inf. Model. 2012, 52 (4), 1046–1060. https://doi.org/10.1021/ci200620h.</li>
   <li>Yoshida, S.; Uehara, S.; Kondo, N.; Takahashi, Y.; Yamamoto, S.; Kameda, A.; Kawagoe, S.; Inoue, N.; Yamada, M.; Yoshimura, N.; et al. Peptide-to-Small Molecule: A Pharmacophore-Guided Small Molecule Lead Generation Strategy from High-Affinity Macrocyclic Peptides. 2022. https://doi.org/10.1021/acs.jmedchem.2c00919.</li>
  <li>Jung, S. W.; Kim, M.; Ramsey, S.; Kurtzman, T.; Cho, A. E. Water Pharmacophore: Designing Ligands Using Molecular Dynamics Simulations with Water. Sci. Rep. 2018, 8 (1), 10400. https://doi.org/10.1038/s41598-018-28546-z.</li>
</ol>
