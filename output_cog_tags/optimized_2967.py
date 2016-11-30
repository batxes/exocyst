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
if "Cog1_Anch" not in marker_sets:
  s=new_marker_set('Cog1_Anch')
  marker_sets["Cog1_Anch"]=s
s= marker_sets["Cog1_Anch"]
mark=s.place_marker((546.583, 536.036, 198.26), (0, 0, 1), 21.9005)
if "Cog2_GFPN" not in marker_sets:
  s=new_marker_set('Cog2_GFPN')
  marker_sets["Cog2_GFPN"]=s
s= marker_sets["Cog2_GFPN"]
mark=s.place_marker((443.808, 529.853, 396.861), (1, 0.5, 0), 21.9005)
if "Cog2_GFPC" not in marker_sets:
  s=new_marker_set('Cog2_GFPC')
  marker_sets["Cog2_GFPC"]=s
s= marker_sets["Cog2_GFPC"]
mark=s.place_marker((580.687, 432.028, 478.951), (1, 0.5, 0), 21.9005)
if "Cog2_Anch" not in marker_sets:
  s=new_marker_set('Cog2_Anch')
  marker_sets["Cog2_Anch"]=s
s= marker_sets["Cog2_Anch"]
mark=s.place_marker((765.215, 520.483, 292.452), (1, 0.5, 0), 21.9005)
if "Cog3_GFPN" not in marker_sets:
  s=new_marker_set('Cog3_GFPN')
  marker_sets["Cog3_GFPN"]=s
s= marker_sets["Cog3_GFPN"]
mark=s.place_marker((477.763, 489.429, 380.515), (1, 0.87, 0), 21.9005)
if "Cog3_GFPC" not in marker_sets:
  s=new_marker_set('Cog3_GFPC')
  marker_sets["Cog3_GFPC"]=s
s= marker_sets["Cog3_GFPC"]
mark=s.place_marker((463.751, 496.157, 390.636), (1, 0.87, 0), 21.9005)
if "Cog3_Anch" not in marker_sets:
  s=new_marker_set('Cog3_Anch')
  marker_sets["Cog3_Anch"]=s
s= marker_sets["Cog3_Anch"]
mark=s.place_marker((506.886, 723.35, 439.753), (1, 0.87, 0), 21.9005)
if "Cog4_GFPN" not in marker_sets:
  s=new_marker_set('Cog4_GFPN')
  marker_sets["Cog4_GFPN"]=s
s= marker_sets["Cog4_GFPN"]
mark=s.place_marker((626.927, 642.861, 321.096), (0.97, 0.51, 0.75), 21.9005)
if "Cog4_GFPC" not in marker_sets:
  s=new_marker_set('Cog4_GFPC')
  marker_sets["Cog4_GFPC"]=s
s= marker_sets["Cog4_GFPC"]
mark=s.place_marker((574.608, 765.059, 380.419), (0.97, 0.51, 0.75), 21.9005)
if "Cog4_Anch" not in marker_sets:
  s=new_marker_set('Cog4_Anch')
  marker_sets["Cog4_Anch"]=s
s= marker_sets["Cog4_Anch"]
mark=s.place_marker((537.847, 722.811, 432.948), (0.97, 0.51, 0.75), 21.9005)
if "Cog5_GFPN" not in marker_sets:
  s=new_marker_set('Cog5_GFPN')
  marker_sets["Cog5_GFPN"]=s
s= marker_sets["Cog5_GFPN"]
mark=s.place_marker((554.687, 504.022, 358.26), (0.39, 0.31, 0.14), 21.9005)
if "Cog5_GFPC" not in marker_sets:
  s=new_marker_set('Cog5_GFPC')
  marker_sets["Cog5_GFPC"]=s
s= marker_sets["Cog5_GFPC"]
mark=s.place_marker((463.588, 490.058, 417.211), (0.39, 0.31, 0.14), 21.9005)
if "Cog5_Anch" not in marker_sets:
  s=new_marker_set('Cog5_Anch')
  marker_sets["Cog5_Anch"]=s
s= marker_sets["Cog5_Anch"]
mark=s.place_marker((673.417, 499.313, 278.722), (0.39, 0.31, 0.14), 21.9005)
if "Cog6_GFPN" not in marker_sets:
  s=new_marker_set('Cog6_GFPN')
  marker_sets["Cog6_GFPN"]=s
s= marker_sets["Cog6_GFPN"]
mark=s.place_marker((515.316, 505.368, 415.55), (0.6, 0.31, 0.64), 21.9005)
if "Cog6_GFPC" not in marker_sets:
  s=new_marker_set('Cog6_GFPC')
  marker_sets["Cog6_GFPC"]=s
s= marker_sets["Cog6_GFPC"]
mark=s.place_marker((486.845, 555.222, 315.164), (0.6, 0.31, 0.64), 21.9005)
if "Cog6_Anch" not in marker_sets:
  s=new_marker_set('Cog6_Anch')
  marker_sets["Cog6_Anch"]=s
s= marker_sets["Cog6_Anch"]
mark=s.place_marker((509.345, 613.701, 524.197), (0.6, 0.31, 0.64), 21.9005)
if "Cog7_GFPN" not in marker_sets:
  s=new_marker_set('Cog7_GFPN')
  marker_sets["Cog7_GFPN"]=s
s= marker_sets["Cog7_GFPN"]
mark=s.place_marker((494.071, 527.646, 344.063), (0.89, 0.1, 0.1), 21.9005)
if "Cog7_GFPC" not in marker_sets:
  s=new_marker_set('Cog7_GFPC')
  marker_sets["Cog7_GFPC"]=s
s= marker_sets["Cog7_GFPC"]
mark=s.place_marker((733.86, 611.257, 443.75), (0.89, 0.1, 0.1), 21.9005)
if "Cog7_Anch" not in marker_sets:
  s=new_marker_set('Cog7_Anch')
  marker_sets["Cog7_Anch"]=s
s= marker_sets["Cog7_Anch"]
mark=s.place_marker((642.816, 553.35, 516.471), (0.89, 0.1, 0.1), 21.9005)
if "Cog8_GFPC" not in marker_sets:
  s=new_marker_set('Cog8_GFPC')
  marker_sets["Cog8_GFPC"]=s
s= marker_sets["Cog8_GFPC"]
mark=s.place_marker((528.998, 481.272, 388.666), (0.3, 0.69, 0.29), 21.9005)
if "Cog8_Anch" not in marker_sets:
  s=new_marker_set('Cog8_Anch')
  marker_sets["Cog8_Anch"]=s
s= marker_sets["Cog8_Anch"]
mark=s.place_marker((667.982, 439.725, 319.055), (0.3, 0.69, 0.29), 21.9005)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
