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
mark=s.place_marker((246, 928, 866), (0, 0, 1), 21.9005)
if "Cog2_GFPN" not in marker_sets:
  s=new_marker_set('Cog2_GFPN')
  marker_sets["Cog2_GFPN"]=s
s= marker_sets["Cog2_GFPN"]
mark=s.place_marker((431, 791, 731), (1, 0.5, 0), 21.9005)
if "Cog2_GFPC" not in marker_sets:
  s=new_marker_set('Cog2_GFPC')
  marker_sets["Cog2_GFPC"]=s
s= marker_sets["Cog2_GFPC"]
mark=s.place_marker((430, 343, 36), (1, 0.5, 0), 21.9005)
if "Cog2_Anch" not in marker_sets:
  s=new_marker_set('Cog2_Anch')
  marker_sets["Cog2_Anch"]=s
s= marker_sets["Cog2_Anch"]
mark=s.place_marker((508, 572, 697), (1, 0.5, 0), 21.9005)
if "Cog3_GFPN" not in marker_sets:
  s=new_marker_set('Cog3_GFPN')
  marker_sets["Cog3_GFPN"]=s
s= marker_sets["Cog3_GFPN"]
mark=s.place_marker((886, 116, 894), (1, 0.87, 0), 21.9005)
if "Cog3_GFPC" not in marker_sets:
  s=new_marker_set('Cog3_GFPC')
  marker_sets["Cog3_GFPC"]=s
s= marker_sets["Cog3_GFPC"]
mark=s.place_marker((54, 137, 841), (1, 0.87, 0), 21.9005)
if "Cog3_Anch" not in marker_sets:
  s=new_marker_set('Cog3_Anch')
  marker_sets["Cog3_Anch"]=s
s= marker_sets["Cog3_Anch"]
mark=s.place_marker((872, 131, 249), (1, 0.87, 0), 21.9005)
if "Cog4_GFPN" not in marker_sets:
  s=new_marker_set('Cog4_GFPN')
  marker_sets["Cog4_GFPN"]=s
s= marker_sets["Cog4_GFPN"]
mark=s.place_marker((776, 545, 823), (0.97, 0.51, 0.75), 21.9005)
if "Cog4_GFPC" not in marker_sets:
  s=new_marker_set('Cog4_GFPC')
  marker_sets["Cog4_GFPC"]=s
s= marker_sets["Cog4_GFPC"]
mark=s.place_marker((881, 416, 642), (0.97, 0.51, 0.75), 21.9005)
if "Cog4_Anch" not in marker_sets:
  s=new_marker_set('Cog4_Anch')
  marker_sets["Cog4_Anch"]=s
s= marker_sets["Cog4_Anch"]
mark=s.place_marker((955, 153, 94), (0.97, 0.51, 0.75), 21.9005)
if "Cog5_GFPN" not in marker_sets:
  s=new_marker_set('Cog5_GFPN')
  marker_sets["Cog5_GFPN"]=s
s= marker_sets["Cog5_GFPN"]
mark=s.place_marker((975, 211, 421), (0.39, 0.31, 0.14), 21.9005)
if "Cog5_GFPC" not in marker_sets:
  s=new_marker_set('Cog5_GFPC')
  marker_sets["Cog5_GFPC"]=s
s= marker_sets["Cog5_GFPC"]
mark=s.place_marker((548, 801, 137), (0.39, 0.31, 0.14), 21.9005)
if "Cog5_Anch" not in marker_sets:
  s=new_marker_set('Cog5_Anch')
  marker_sets["Cog5_Anch"]=s
s= marker_sets["Cog5_Anch"]
mark=s.place_marker((601, 125, 209), (0.39, 0.31, 0.14), 21.9005)
if "Cog6_GFPN" not in marker_sets:
  s=new_marker_set('Cog6_GFPN')
  marker_sets["Cog6_GFPN"]=s
s= marker_sets["Cog6_GFPN"]
mark=s.place_marker((573, 173, 37), (0.6, 0.31, 0.64), 21.9005)
if "Cog6_GFPC" not in marker_sets:
  s=new_marker_set('Cog6_GFPC')
  marker_sets["Cog6_GFPC"]=s
s= marker_sets["Cog6_GFPC"]
mark=s.place_marker((449, 369, 845), (0.6, 0.31, 0.64), 21.9005)
if "Cog6_Anch" not in marker_sets:
  s=new_marker_set('Cog6_Anch')
  marker_sets["Cog6_Anch"]=s
s= marker_sets["Cog6_Anch"]
mark=s.place_marker((969, 180, 21), (0.6, 0.31, 0.64), 21.9005)
if "Cog7_GFPN" not in marker_sets:
  s=new_marker_set('Cog7_GFPN')
  marker_sets["Cog7_GFPN"]=s
s= marker_sets["Cog7_GFPN"]
mark=s.place_marker((167, 202, 257), (0.89, 0.1, 0.1), 21.9005)
if "Cog7_GFPC" not in marker_sets:
  s=new_marker_set('Cog7_GFPC')
  marker_sets["Cog7_GFPC"]=s
s= marker_sets["Cog7_GFPC"]
mark=s.place_marker((314, 705, 225), (0.89, 0.1, 0.1), 21.9005)
if "Cog7_Anch" not in marker_sets:
  s=new_marker_set('Cog7_Anch')
  marker_sets["Cog7_Anch"]=s
s= marker_sets["Cog7_Anch"]
mark=s.place_marker((469, 65, 488), (0.89, 0.1, 0.1), 21.9005)
if "Cog8_GFPC" not in marker_sets:
  s=new_marker_set('Cog8_GFPC')
  marker_sets["Cog8_GFPC"]=s
s= marker_sets["Cog8_GFPC"]
mark=s.place_marker((507, 494, 456), (0.3, 0.69, 0.29), 21.9005)
if "Cog8_Anch" not in marker_sets:
  s=new_marker_set('Cog8_Anch')
  marker_sets["Cog8_Anch"]=s
s= marker_sets["Cog8_Anch"]
mark=s.place_marker((626, 228, 592), (0.3, 0.69, 0.29), 21.9005)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
