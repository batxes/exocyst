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
mark=s.place_marker((452.25, 542.286, 492.08), (0.15, 0.78, 0.66), 2)
if "Sec3_GFPC" not in marker_sets:
  s=new_marker_set('Sec3_GFPC')
  marker_sets["Sec3_GFPC"]=s
s= marker_sets["Sec3_GFPC"]
mark=s.place_marker((422.307, 518.031, 526.873), (0.15, 0.78, 0.66), 2)
if "Sec3_Anch" not in marker_sets:
  s=new_marker_set('Sec3_Anch')
  marker_sets["Sec3_Anch"]=s
s= marker_sets["Sec3_Anch"]
mark=s.place_marker((497.009, 306.663, 486.71), (0.15, 0.58, 0.66), 2)
if "Sec5_GFPN" not in marker_sets:
  s=new_marker_set('Sec5_GFPN')
  marker_sets["Sec5_GFPN"]=s
s= marker_sets["Sec5_GFPN"]
mark=s.place_marker((483.096, 528.551, 497.237), (0.38, 0.24, 0.37), 2)
if "Sec5_GFPC" not in marker_sets:
  s=new_marker_set('Sec5_GFPC')
  marker_sets["Sec5_GFPC"]=s
s= marker_sets["Sec5_GFPC"]
mark=s.place_marker((399.085, 485.531, 510.933), (0.38, 0.24, 0.37), 2)
if "Sec6_GFPN" not in marker_sets:
  s=new_marker_set('Sec6_GFPN')
  marker_sets["Sec6_GFPN"]=s
s= marker_sets["Sec6_GFPN"]
mark=s.place_marker((475.139, 500.646, 549.303), (0.84, 0.98, 0.24), 2)
if "Sec6_GFPC" not in marker_sets:
  s=new_marker_set('Sec6_GFPC')
  marker_sets["Sec6_GFPC"]=s
s= marker_sets["Sec6_GFPC"]
mark=s.place_marker((463.163, 448.151, 366.263), (0.84, 0.98, 0.24), 2)
if "Sec6_Anch" not in marker_sets:
  s=new_marker_set('Sec6_Anch')
  marker_sets["Sec6_Anch"]=s
s= marker_sets["Sec6_Anch"]
mark=s.place_marker((423.358, 589.653, 280.3), (0.84, 0.78, 0.24), 2)
if "Sec8_GFPC" not in marker_sets:
  s=new_marker_set('Sec8_GFPC')
  marker_sets["Sec8_GFPC"]=s
s= marker_sets["Sec8_GFPC"]
mark=s.place_marker((397.481, 435.285, 396.787), (0.62, 0.67, 0.45), 2)
if "Sec8_Anch" not in marker_sets:
  s=new_marker_set('Sec8_Anch')
  marker_sets["Sec8_Anch"]=s
s= marker_sets["Sec8_Anch"]
mark=s.place_marker((457.766, 312.114, 559.189), (0.62, 0.47, 0.45), 2)
if "Sec10_GFPN" not in marker_sets:
  s=new_marker_set('Sec10_GFPN')
  marker_sets["Sec10_GFPN"]=s
s= marker_sets["Sec10_GFPN"]
mark=s.place_marker((461.37, 459.603, 334.456), (0, 0.91, 0), 2)
if "Sec10_GFPC" not in marker_sets:
  s=new_marker_set('Sec10_GFPC')
  marker_sets["Sec10_GFPC"]=s
s= marker_sets["Sec10_GFPC"]
mark=s.place_marker((321.464, 463.925, 491.214), (0, 0.91, 0), 2)
if "Sec10_Anch" not in marker_sets:
  s=new_marker_set('Sec10_Anch')
  marker_sets["Sec10_Anch"]=s
s= marker_sets["Sec10_Anch"]
mark=s.place_marker((549.906, 554.619, 331.935), (0, 0.71, 0), 2)
if "Sec15_GFPN" not in marker_sets:
  s=new_marker_set('Sec15_GFPN')
  marker_sets["Sec15_GFPN"]=s
s= marker_sets["Sec15_GFPN"]
mark=s.place_marker((420.639, 516.57, 430.707), (0.11, 0.51, 0.86), 2)
if "Sec15_GFPC" not in marker_sets:
  s=new_marker_set('Sec15_GFPC')
  marker_sets["Sec15_GFPC"]=s
s= marker_sets["Sec15_GFPC"]
mark=s.place_marker((361.302, 417.406, 366.31), (0.11, 0.51, 0.86), 2)
if "Sec15_Anch" not in marker_sets:
  s=new_marker_set('Sec15_Anch')
  marker_sets["Sec15_Anch"]=s
s= marker_sets["Sec15_Anch"]
mark=s.place_marker((263.159, 551.133, 368.797), (0.11, 0.31, 0.86), 2)
if "Exo70_GFPN" not in marker_sets:
  s=new_marker_set('Exo70_GFPN')
  marker_sets["Exo70_GFPN"]=s
s= marker_sets["Exo70_GFPN"]
mark=s.place_marker((414.232, 529.538, 502.19), (0.89, 0.47, 0.4), 2)
if "Exo70_GFPC" not in marker_sets:
  s=new_marker_set('Exo70_GFPC')
  marker_sets["Exo70_GFPC"]=s
s= marker_sets["Exo70_GFPC"]
mark=s.place_marker((395.034, 379.324, 364.988), (0.89, 0.47, 0.4), 2)
if "Exo70_Anch" not in marker_sets:
  s=new_marker_set('Exo70_Anch')
  marker_sets["Exo70_Anch"]=s
s= marker_sets["Exo70_Anch"]
mark=s.place_marker((509.963, 703.963, 400.71), (0.89, 0.27, 0.4), 2)
if "Exo84_GFPN" not in marker_sets:
  s=new_marker_set('Exo84_GFPN')
  marker_sets["Exo84_GFPN"]=s
s= marker_sets["Exo84_GFPN"]
mark=s.place_marker((484.167, 529.899, 466.221), (0.5, 0.7, 0), 2)
if "Exo84_GFPC" not in marker_sets:
  s=new_marker_set('Exo84_GFPC')
  marker_sets["Exo84_GFPC"]=s
s= marker_sets["Exo84_GFPC"]
mark=s.place_marker((381.405, 457.09, 488.981), (0.5, 0.7, 0), 2)
if "Exo84_Anch" not in marker_sets:
  s=new_marker_set('Exo84_Anch')
  marker_sets["Exo84_Anch"]=s
s= marker_sets["Exo84_Anch"]
mark=s.place_marker((292.706, 611.017, 387.815), (0.5, 0.5, 0), 2)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
