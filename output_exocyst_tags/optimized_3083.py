import _surface
import chimera
try:
  import chimera.runCommand
except:
  pass
from VolumePath import markerset as ms
try:
  from VolumePath import Marker_Set, Link
  new_marker_set=Marker_Set
except:
  from VolumePath import volume_path_dialog
  d= volume_path_dialog(True)
  new_marker_set= d.new_marker_set
marker_sets={}
surf_sets={}
if "Sec3_GFPN" not in marker_sets:
  s=new_marker_set('Sec3_GFPN')
  marker_sets["Sec3_GFPN"]=s
s= marker_sets["Sec3_GFPN"]
mark=s.place_marker((585.688, 457.069, 503.664), (0.15, 0.78, 0.66), 21.9005)
if "Sec3_GFPC" not in marker_sets:
  s=new_marker_set('Sec3_GFPC')
  marker_sets["Sec3_GFPC"]=s
s= marker_sets["Sec3_GFPC"]
mark=s.place_marker((570.545, 436.243, 459.611), (0.15, 0.78, 0.66), 31.586)
if "Sec3_Anch" not in marker_sets:
  s=new_marker_set('Sec3_Anch')
  marker_sets["Sec3_Anch"]=s
s= marker_sets["Sec3_Anch"]
mark=s.place_marker((353.105, 498.057, 445.265), (0.15, 0.58, 0.66), 26.9335)
if "Sec5_GFPN" not in marker_sets:
  s=new_marker_set('Sec5_GFPN')
  marker_sets["Sec5_GFPN"]=s
s= marker_sets["Sec5_GFPN"]
mark=s.place_marker((552.182, 450.121, 533.387), (0.38, 0.24, 0.37), 21.9005)
if "Sec5_GFPC" not in marker_sets:
  s=new_marker_set('Sec5_GFPC')
  marker_sets["Sec5_GFPC"]=s
s= marker_sets["Sec5_GFPC"]
mark=s.place_marker((553.357, 453.619, 434.069), (0.38, 0.24, 0.37), 31.586)
if "Sec6_GFPN" not in marker_sets:
  s=new_marker_set('Sec6_GFPN')
  marker_sets["Sec6_GFPN"]=s
s= marker_sets["Sec6_GFPN"]
mark=s.place_marker((526.035, 407.22, 500.803), (0.84, 0.98, 0.24), 21.9005)
if "Sec6_GFPC" not in marker_sets:
  s=new_marker_set('Sec6_GFPC')
  marker_sets["Sec6_GFPC"]=s
s= marker_sets["Sec6_GFPC"]
mark=s.place_marker((478.935, 585.292, 558.421), (0.84, 0.98, 0.24), 31.586)
if "Sec6_Anch" not in marker_sets:
  s=new_marker_set('Sec6_Anch')
  marker_sets["Sec6_Anch"]=s
s= marker_sets["Sec6_Anch"]
mark=s.place_marker((656.236, 655.313, 550.447), (0.84, 0.78, 0.24), 26.9335)
if "Sec8_GFPC" not in marker_sets:
  s=new_marker_set('Sec8_GFPC')
  marker_sets["Sec8_GFPC"]=s
s= marker_sets["Sec8_GFPC"]
mark=s.place_marker((481.795, 621.234, 504.069), (0.62, 0.67, 0.45), 31.586)
if "Sec8_Anch" not in marker_sets:
  s=new_marker_set('Sec8_Anch')
  marker_sets["Sec8_Anch"]=s
s= marker_sets["Sec8_Anch"]
mark=s.place_marker((366.059, 448.963, 405.594), (0.62, 0.47, 0.45), 26.9335)
if "Sec10_GFPN" not in marker_sets:
  s=new_marker_set('Sec10_GFPN')
  marker_sets["Sec10_GFPN"]=s
s= marker_sets["Sec10_GFPN"]
mark=s.place_marker((461.297, 667.166, 529.894), (0, 0.91, 0), 21.9005)
if "Sec10_GFPC" not in marker_sets:
  s=new_marker_set('Sec10_GFPC')
  marker_sets["Sec10_GFPC"]=s
s= marker_sets["Sec10_GFPC"]
mark=s.place_marker((568.385, 494.71, 358.903), (0, 0.91, 0), 31.586)
if "Sec10_Anch" not in marker_sets:
  s=new_marker_set('Sec10_Anch')
  marker_sets["Sec10_Anch"]=s
s= marker_sets["Sec10_Anch"]
mark=s.place_marker((623.776, 570.642, 639.539), (0, 0.71, 0), 26.9335)
if "Sec15_GFPN" not in marker_sets:
  s=new_marker_set('Sec15_GFPN')
  marker_sets["Sec15_GFPN"]=s
s= marker_sets["Sec15_GFPN"]
mark=s.place_marker((585.162, 535.26, 479.792), (0.11, 0.51, 0.86), 21.9005)
if "Sec15_GFPC" not in marker_sets:
  s=new_marker_set('Sec15_GFPC')
  marker_sets["Sec15_GFPC"]=s
s= marker_sets["Sec15_GFPC"]
mark=s.place_marker((478.194, 667.639, 483.741), (0.11, 0.51, 0.86), 31.586)
if "Sec15_Anch" not in marker_sets:
  s=new_marker_set('Sec15_Anch')
  marker_sets["Sec15_Anch"]=s
s= marker_sets["Sec15_Anch"]
mark=s.place_marker((608.861, 646.191, 379.678), (0.11, 0.31, 0.86), 26.9335)
if "Exo70_GFPN" not in marker_sets:
  s=new_marker_set('Exo70_GFPN')
  marker_sets["Exo70_GFPN"]=s
s= marker_sets["Exo70_GFPN"]
mark=s.place_marker((588.019, 455.66, 458.307), (0.89, 0.47, 0.4), 21.9005)
if "Exo70_GFPC" not in marker_sets:
  s=new_marker_set('Exo70_GFPC')
  marker_sets["Exo70_GFPC"]=s
s= marker_sets["Exo70_GFPC"]
mark=s.place_marker((433.088, 630.746, 507.866), (0.89, 0.47, 0.4), 31.586)
if "Exo70_Anch" not in marker_sets:
  s=new_marker_set('Exo70_Anch')
  marker_sets["Exo70_Anch"]=s
s= marker_sets["Exo70_Anch"]
mark=s.place_marker((709.652, 504.08, 646.426), (0.89, 0.27, 0.4), 26.9335)
if "Exo84_GFPN" not in marker_sets:
  s=new_marker_set('Exo84_GFPN')
  marker_sets["Exo84_GFPN"]=s
s= marker_sets["Exo84_GFPN"]
mark=s.place_marker((555.761, 476.364, 543.761), (0.5, 0.7, 0), 31.586)
if "Exo84_GFPC" not in marker_sets:
  s=new_marker_set('Exo84_GFPC')
  marker_sets["Exo84_GFPC"]=s
s= marker_sets["Exo84_GFPC"]
mark=s.place_marker((541.102, 470.184, 418.474), (0.5, 0.7, 0), 31.586)
if "Exo84_Anch" not in marker_sets:
  s=new_marker_set('Exo84_Anch')
  marker_sets["Exo84_Anch"]=s
s= marker_sets["Exo84_Anch"]
mark=s.place_marker((671.766, 621.228, 427.288), (0.5, 0.5, 0), 26.9335)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
