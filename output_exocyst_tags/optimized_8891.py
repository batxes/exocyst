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
mark=s.place_marker((540.974, 474.303, 686.227), (0.15, 0.78, 0.66), 21.9005)
if "Sec3_GFPC" not in marker_sets:
  s=new_marker_set('Sec3_GFPC')
  marker_sets["Sec3_GFPC"]=s
s= marker_sets["Sec3_GFPC"]
mark=s.place_marker((506.111, 441.655, 672.038), (0.15, 0.78, 0.66), 31.586)
if "Sec3_Anch" not in marker_sets:
  s=new_marker_set('Sec3_Anch')
  marker_sets["Sec3_Anch"]=s
s= marker_sets["Sec3_Anch"]
mark=s.place_marker((391.096, 550.544, 510.122), (0.15, 0.58, 0.66), 26.9335)
if "Sec5_GFPN" not in marker_sets:
  s=new_marker_set('Sec5_GFPN')
  marker_sets["Sec5_GFPN"]=s
s= marker_sets["Sec5_GFPN"]
mark=s.place_marker((521.019, 515.008, 687.479), (0.38, 0.24, 0.37), 21.9005)
if "Sec5_GFPC" not in marker_sets:
  s=new_marker_set('Sec5_GFPC')
  marker_sets["Sec5_GFPC"]=s
s= marker_sets["Sec5_GFPC"]
mark=s.place_marker((498.902, 431.585, 638.227), (0.38, 0.24, 0.37), 31.586)
if "Sec6_GFPN" not in marker_sets:
  s=new_marker_set('Sec6_GFPN')
  marker_sets["Sec6_GFPN"]=s
s= marker_sets["Sec6_GFPN"]
mark=s.place_marker((466.184, 491.011, 689.28), (0.84, 0.98, 0.24), 21.9005)
if "Sec6_GFPC" not in marker_sets:
  s=new_marker_set('Sec6_GFPC')
  marker_sets["Sec6_GFPC"]=s
s= marker_sets["Sec6_GFPC"]
mark=s.place_marker((569.456, 597.391, 555.353), (0.84, 0.98, 0.24), 31.586)
if "Sec6_Anch" not in marker_sets:
  s=new_marker_set('Sec6_Anch')
  marker_sets["Sec6_Anch"]=s
s= marker_sets["Sec6_Anch"]
mark=s.place_marker((733.43, 525.336, 602.632), (0.84, 0.78, 0.24), 26.9335)
if "Sec8_GFPC" not in marker_sets:
  s=new_marker_set('Sec8_GFPC')
  marker_sets["Sec8_GFPC"]=s
s= marker_sets["Sec8_GFPC"]
mark=s.place_marker((578.515, 551.897, 507.087), (0.62, 0.67, 0.45), 31.586)
if "Sec8_Anch" not in marker_sets:
  s=new_marker_set('Sec8_Anch')
  marker_sets["Sec8_Anch"]=s
s= marker_sets["Sec8_Anch"]
mark=s.place_marker((356.97, 500.472, 533.271), (0.62, 0.47, 0.45), 26.9335)
if "Sec10_GFPN" not in marker_sets:
  s=new_marker_set('Sec10_GFPN')
  marker_sets["Sec10_GFPN"]=s
s= marker_sets["Sec10_GFPN"]
mark=s.place_marker((603.07, 597.591, 490.008), (0, 0.91, 0), 21.9005)
if "Sec10_GFPC" not in marker_sets:
  s=new_marker_set('Sec10_GFPC')
  marker_sets["Sec10_GFPC"]=s
s= marker_sets["Sec10_GFPC"]
mark=s.place_marker((518.113, 368.802, 578.341), (0, 0.91, 0), 31.586)
if "Sec10_Anch" not in marker_sets:
  s=new_marker_set('Sec10_Anch')
  marker_sets["Sec10_Anch"]=s
s= marker_sets["Sec10_Anch"]
mark=s.place_marker((672.627, 602.011, 678.548), (0, 0.71, 0), 26.9335)
if "Sec15_GFPN" not in marker_sets:
  s=new_marker_set('Sec15_GFPN')
  marker_sets["Sec15_GFPN"]=s
s= marker_sets["Sec15_GFPN"]
mark=s.place_marker((507.198, 597.388, 709.887), (0.11, 0.51, 0.86), 21.9005)
if "Sec15_GFPC" not in marker_sets:
  s=new_marker_set('Sec15_GFPC')
  marker_sets["Sec15_GFPC"]=s
s= marker_sets["Sec15_GFPC"]
mark=s.place_marker((600.671, 542.136, 463.276), (0.11, 0.51, 0.86), 31.586)
if "Sec15_Anch" not in marker_sets:
  s=new_marker_set('Sec15_Anch')
  marker_sets["Sec15_Anch"]=s
s= marker_sets["Sec15_Anch"]
mark=s.place_marker((657.575, 391.566, 509.52), (0.11, 0.31, 0.86), 26.9335)
if "Exo70_GFPN" not in marker_sets:
  s=new_marker_set('Exo70_GFPN')
  marker_sets["Exo70_GFPN"]=s
s= marker_sets["Exo70_GFPN"]
mark=s.place_marker((530.797, 438.244, 668.19), (0.89, 0.47, 0.4), 21.9005)
if "Exo70_GFPC" not in marker_sets:
  s=new_marker_set('Exo70_GFPC')
  marker_sets["Exo70_GFPC"]=s
s= marker_sets["Exo70_GFPC"]
mark=s.place_marker((552.448, 578.303, 472.945), (0.89, 0.47, 0.4), 31.586)
if "Exo70_Anch" not in marker_sets:
  s=new_marker_set('Exo70_Anch')
  marker_sets["Exo70_Anch"]=s
s= marker_sets["Exo70_Anch"]
mark=s.place_marker((700.386, 544.859, 773.889), (0.89, 0.27, 0.4), 26.9335)
if "Exo84_GFPN" not in marker_sets:
  s=new_marker_set('Exo84_GFPN')
  marker_sets["Exo84_GFPN"]=s
s= marker_sets["Exo84_GFPN"]
mark=s.place_marker((542.823, 524.01, 676.102), (0.5, 0.7, 0), 31.586)
if "Exo84_GFPC" not in marker_sets:
  s=new_marker_set('Exo84_GFPC')
  marker_sets["Exo84_GFPC"]=s
s= marker_sets["Exo84_GFPC"]
mark=s.place_marker((497.767, 427.017, 610.493), (0.5, 0.7, 0), 31.586)
if "Exo84_Anch" not in marker_sets:
  s=new_marker_set('Exo84_Anch')
  marker_sets["Exo84_Anch"]=s
s= marker_sets["Exo84_Anch"]
mark=s.place_marker((692.869, 397.874, 580.084), (0.5, 0.5, 0), 26.9335)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])