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
mark=s.place_marker((375.773, 626.035, 531.624), (0.15, 0.78, 0.66), 21.9005)
if "Sec3_GFPC" not in marker_sets:
  s=new_marker_set('Sec3_GFPC')
  marker_sets["Sec3_GFPC"]=s
s= marker_sets["Sec3_GFPC"]
mark=s.place_marker((363.738, 658.729, 490.356), (0.15, 0.78, 0.66), 31.586)
if "Sec3_Anch" not in marker_sets:
  s=new_marker_set('Sec3_Anch')
  marker_sets["Sec3_Anch"]=s
s= marker_sets["Sec3_Anch"]
mark=s.place_marker((523.788, 821.075, 491.663), (0.15, 0.58, 0.66), 26.9335)
if "Sec5_GFPN" not in marker_sets:
  s=new_marker_set('Sec5_GFPN')
  marker_sets["Sec5_GFPN"]=s
s= marker_sets["Sec5_GFPN"]
mark=s.place_marker((439.754, 659.47, 617.224), (0.38, 0.24, 0.37), 21.9005)
if "Sec5_GFPC" not in marker_sets:
  s=new_marker_set('Sec5_GFPC')
  marker_sets["Sec5_GFPC"]=s
s= marker_sets["Sec5_GFPC"]
mark=s.place_marker((381.695, 675.142, 458.087), (0.38, 0.24, 0.37), 31.586)
if "Sec6_GFPN" not in marker_sets:
  s=new_marker_set('Sec6_GFPN')
  marker_sets["Sec6_GFPN"]=s
s= marker_sets["Sec6_GFPN"]
mark=s.place_marker((381.462, 707.107, 579.784), (0.84, 0.98, 0.24), 21.9005)
if "Sec6_GFPC" not in marker_sets:
  s=new_marker_set('Sec6_GFPC')
  marker_sets["Sec6_GFPC"]=s
s= marker_sets["Sec6_GFPC"]
mark=s.place_marker((568.385, 677.999, 616.439), (0.84, 0.98, 0.24), 31.586)
if "Sec6_Anch" not in marker_sets:
  s=new_marker_set('Sec6_Anch')
  marker_sets["Sec6_Anch"]=s
s= marker_sets["Sec6_Anch"]
mark=s.place_marker((559.078, 503.2, 516.619), (0.84, 0.78, 0.24), 26.9335)
if "Sec8_GFPC" not in marker_sets:
  s=new_marker_set('Sec8_GFPC')
  marker_sets["Sec8_GFPC"]=s
s= marker_sets["Sec8_GFPC"]
mark=s.place_marker((620.602, 671.961, 548.394), (0.62, 0.67, 0.45), 31.586)
if "Sec8_Anch" not in marker_sets:
  s=new_marker_set('Sec8_Anch')
  marker_sets["Sec8_Anch"]=s
s= marker_sets["Sec8_Anch"]
mark=s.place_marker((475.596, 837.442, 476.387), (0.62, 0.47, 0.45), 26.9335)
if "Sec10_GFPN" not in marker_sets:
  s=new_marker_set('Sec10_GFPN')
  marker_sets["Sec10_GFPN"]=s
s= marker_sets["Sec10_GFPN"]
mark=s.place_marker((651.723, 667.312, 581.973), (0, 0.91, 0), 21.9005)
if "Sec10_GFPC" not in marker_sets:
  s=new_marker_set('Sec10_GFPC')
  marker_sets["Sec10_GFPC"]=s
s= marker_sets["Sec10_GFPC"]
mark=s.place_marker((429.83, 660.121, 362.948), (0, 0.91, 0), 31.586)
if "Sec10_Anch" not in marker_sets:
  s=new_marker_set('Sec10_Anch')
  marker_sets["Sec10_Anch"]=s
s= marker_sets["Sec10_Anch"]
mark=s.place_marker((508.837, 508.47, 589.644), (0, 0.71, 0), 26.9335)
if "Sec15_GFPN" not in marker_sets:
  s=new_marker_set('Sec15_GFPN')
  marker_sets["Sec15_GFPN"]=s
s= marker_sets["Sec15_GFPN"]
mark=s.place_marker((479.273, 658.369, 657.521), (0.11, 0.51, 0.86), 21.9005)
if "Sec15_GFPC" not in marker_sets:
  s=new_marker_set('Sec15_GFPC')
  marker_sets["Sec15_GFPC"]=s
s= marker_sets["Sec15_GFPC"]
mark=s.place_marker((666.488, 661.303, 510.235), (0.11, 0.51, 0.86), 31.586)
if "Sec15_Anch" not in marker_sets:
  s=new_marker_set('Sec15_Anch')
  marker_sets["Sec15_Anch"]=s
s= marker_sets["Sec15_Anch"]
mark=s.place_marker((562.62, 581.633, 408.313), (0.11, 0.31, 0.86), 26.9335)
if "Exo70_GFPN" not in marker_sets:
  s=new_marker_set('Exo70_GFPN')
  marker_sets["Exo70_GFPN"]=s
s= marker_sets["Exo70_GFPN"]
mark=s.place_marker((373.843, 634.134, 469.687), (0.89, 0.47, 0.4), 21.9005)
if "Exo70_GFPC" not in marker_sets:
  s=new_marker_set('Exo70_GFPC')
  marker_sets["Exo70_GFPC"]=s
s= marker_sets["Exo70_GFPC"]
mark=s.place_marker((633.129, 714.149, 566.47), (0.89, 0.47, 0.4), 31.586)
if "Exo70_Anch" not in marker_sets:
  s=new_marker_set('Exo70_Anch')
  marker_sets["Exo70_Anch"]=s
s= marker_sets["Exo70_Anch"]
mark=s.place_marker((429.573, 458.392, 610.189), (0.89, 0.27, 0.4), 26.9335)
if "Exo84_GFPN" not in marker_sets:
  s=new_marker_set('Exo84_GFPN')
  marker_sets["Exo84_GFPN"]=s
s= marker_sets["Exo84_GFPN"]
mark=s.place_marker((439.035, 643.604, 604.193), (0.5, 0.7, 0), 31.586)
if "Exo84_GFPC" not in marker_sets:
  s=new_marker_set('Exo84_GFPC')
  marker_sets["Exo84_GFPC"]=s
s= marker_sets["Exo84_GFPC"]
mark=s.place_marker((399.919, 682.993, 434.913), (0.5, 0.7, 0), 31.586)
if "Exo84_Anch" not in marker_sets:
  s=new_marker_set('Exo84_Anch')
  marker_sets["Exo84_Anch"]=s
s= marker_sets["Exo84_Anch"]
mark=s.place_marker((522.858, 528.359, 438.336), (0.5, 0.5, 0), 26.9335)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
