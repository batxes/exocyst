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
mark=s.place_marker((669.177, 645.17, 408.491), (0, 0, 1), 21.9005)
if "Cog2_GFPN" not in marker_sets:
  s=new_marker_set('Cog2_GFPN')
  marker_sets["Cog2_GFPN"]=s
s= marker_sets["Cog2_GFPN"]
mark=s.place_marker((464.423, 550.766, 374.635), (1, 0.5, 0), 21.9005)
if "Cog2_GFPC" not in marker_sets:
  s=new_marker_set('Cog2_GFPC')
  marker_sets["Cog2_GFPC"]=s
s= marker_sets["Cog2_GFPC"]
mark=s.place_marker((458.669, 421.621, 421.734), (1, 0.5, 0), 21.9005)
if "Cog2_Anch" not in marker_sets:
  s=new_marker_set('Cog2_Anch')
  marker_sets["Cog2_Anch"]=s
s= marker_sets["Cog2_Anch"]
mark=s.place_marker((675.299, 473.515, 633.745), (1, 0.5, 0), 21.9005)
if "Cog3_GFPN" not in marker_sets:
  s=new_marker_set('Cog3_GFPN')
  marker_sets["Cog3_GFPN"]=s
s= marker_sets["Cog3_GFPN"]
mark=s.place_marker((498.03, 536.995, 403.485), (1, 0.87, 0), 21.9005)
if "Cog3_GFPC" not in marker_sets:
  s=new_marker_set('Cog3_GFPC')
  marker_sets["Cog3_GFPC"]=s
s= marker_sets["Cog3_GFPC"]
mark=s.place_marker((479.26, 557.138, 396.075), (1, 0.87, 0), 21.9005)
if "Cog3_Anch" not in marker_sets:
  s=new_marker_set('Cog3_Anch')
  marker_sets["Cog3_Anch"]=s
s= marker_sets["Cog3_Anch"]
mark=s.place_marker((627.135, 472.037, 268.237), (1, 0.87, 0), 21.9005)
if "Cog4_GFPN" not in marker_sets:
  s=new_marker_set('Cog4_GFPN')
  marker_sets["Cog4_GFPN"]=s
s= marker_sets["Cog4_GFPN"]
mark=s.place_marker((711.708, 474.129, 451.8), (0.97, 0.51, 0.75), 21.9005)
if "Cog4_GFPC" not in marker_sets:
  s=new_marker_set('Cog4_GFPC')
  marker_sets["Cog4_GFPC"]=s
s= marker_sets["Cog4_GFPC"]
mark=s.place_marker((740.741, 379.646, 330.747), (0.97, 0.51, 0.75), 21.9005)
if "Cog4_Anch" not in marker_sets:
  s=new_marker_set('Cog4_Anch')
  marker_sets["Cog4_Anch"]=s
s= marker_sets["Cog4_Anch"]
mark=s.place_marker((371.973, 689.775, 520.434), (0.97, 0.51, 0.75), 21.9005)
if "Cog5_GFPN" not in marker_sets:
  s=new_marker_set('Cog5_GFPN')
  marker_sets["Cog5_GFPN"]=s
s= marker_sets["Cog5_GFPN"]
mark=s.place_marker((565.487, 543.987, 468.98), (0.39, 0.31, 0.14), 21.9005)
if "Cog5_GFPC" not in marker_sets:
  s=new_marker_set('Cog5_GFPC')
  marker_sets["Cog5_GFPC"]=s
s= marker_sets["Cog5_GFPC"]
mark=s.place_marker((436.243, 505.618, 398.652), (0.39, 0.31, 0.14), 21.9005)
if "Cog5_Anch" not in marker_sets:
  s=new_marker_set('Cog5_Anch')
  marker_sets["Cog5_Anch"]=s
s= marker_sets["Cog5_Anch"]
mark=s.place_marker((611.118, 452.736, 568.878), (0.39, 0.31, 0.14), 21.9005)
if "Cog6_GFPN" not in marker_sets:
  s=new_marker_set('Cog6_GFPN')
  marker_sets["Cog6_GFPN"]=s
s= marker_sets["Cog6_GFPN"]
mark=s.place_marker((482.613, 516.719, 422.985), (0.6, 0.31, 0.64), 21.9005)
if "Cog6_GFPC" not in marker_sets:
  s=new_marker_set('Cog6_GFPC')
  marker_sets["Cog6_GFPC"]=s
s= marker_sets["Cog6_GFPC"]
mark=s.place_marker((547.934, 592.083, 408.008), (0.6, 0.31, 0.64), 21.9005)
if "Cog6_Anch" not in marker_sets:
  s=new_marker_set('Cog6_Anch')
  marker_sets["Cog6_Anch"]=s
s= marker_sets["Cog6_Anch"]
mark=s.place_marker((569.818, 489.002, 270.667), (0.6, 0.31, 0.64), 21.9005)
if "Cog7_GFPN" not in marker_sets:
  s=new_marker_set('Cog7_GFPN')
  marker_sets["Cog7_GFPN"]=s
s= marker_sets["Cog7_GFPN"]
mark=s.place_marker((525.592, 589.51, 448.341), (0.89, 0.1, 0.1), 21.9005)
if "Cog7_GFPC" not in marker_sets:
  s=new_marker_set('Cog7_GFPC')
  marker_sets["Cog7_GFPC"]=s
s= marker_sets["Cog7_GFPC"]
mark=s.place_marker((418.571, 478.336, 454.148), (0.89, 0.1, 0.1), 21.9005)
if "Cog7_Anch" not in marker_sets:
  s=new_marker_set('Cog7_Anch')
  marker_sets["Cog7_Anch"]=s
s= marker_sets["Cog7_Anch"]
mark=s.place_marker((532.522, 361.201, 500.706), (0.89, 0.1, 0.1), 21.9005)
if "Cog8_GFPC" not in marker_sets:
  s=new_marker_set('Cog8_GFPC')
  marker_sets["Cog8_GFPC"]=s
s= marker_sets["Cog8_GFPC"]
mark=s.place_marker((500.718, 545.975, 453.609), (0.3, 0.69, 0.29), 21.9005)
if "Cog8_Anch" not in marker_sets:
  s=new_marker_set('Cog8_Anch')
  marker_sets["Cog8_Anch"]=s
s= marker_sets["Cog8_Anch"]
mark=s.place_marker((546.969, 500.04, 602.642), (0.3, 0.69, 0.29), 21.9005)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
