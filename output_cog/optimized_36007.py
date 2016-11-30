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
if "Cog2_GFPN" not in marker_sets:
  s=new_marker_set('Cog2_GFPN')
  marker_sets["Cog2_GFPN"]=s
s= marker_sets["Cog2_GFPN"]
mark=s.place_marker((562.956, 606.319, 542.196), (0.89, 0.1, 0.1), 18.4716)
if "Cog2_0" not in marker_sets:
  s=new_marker_set('Cog2_0')
  marker_sets["Cog2_0"]=s
s= marker_sets["Cog2_0"]
mark=s.place_marker((596.15, 663.749, 549.123), (0.89, 0.1, 0.1), 17.1475)
if "Cog2_1" not in marker_sets:
  s=new_marker_set('Cog2_1')
  marker_sets["Cog2_1"]=s
s= marker_sets["Cog2_1"]
mark=s.place_marker((641.974, 731.843, 544.088), (0.89, 0.1, 0.1), 17.1475)
if "Cog2_GFPC" not in marker_sets:
  s=new_marker_set('Cog2_GFPC')
  marker_sets["Cog2_GFPC"]=s
s= marker_sets["Cog2_GFPC"]
mark=s.place_marker((592.522, 674.052, 426.156), (0.89, 0.1, 0.1), 18.4716)
if "Cog2_Anch" not in marker_sets:
  s=new_marker_set('Cog2_Anch')
  marker_sets["Cog2_Anch"]=s
s= marker_sets["Cog2_Anch"]
mark=s.place_marker((759.202, 885.626, 574.56), (0.89, 0.1, 0.1), 18.4716)
if "Cog3_GFPN" not in marker_sets:
  s=new_marker_set('Cog3_GFPN')
  marker_sets["Cog3_GFPN"]=s
s= marker_sets["Cog3_GFPN"]
mark=s.place_marker((595.975, 638.826, 544.225), (1, 1, 0), 18.4716)
if "Cog3_0" not in marker_sets:
  s=new_marker_set('Cog3_0')
  marker_sets["Cog3_0"]=s
s= marker_sets["Cog3_0"]
mark=s.place_marker((596.085, 637.578, 544.122), (1, 1, 0.2), 17.1475)
if "Cog3_1" not in marker_sets:
  s=new_marker_set('Cog3_1')
  marker_sets["Cog3_1"]=s
s= marker_sets["Cog3_1"]
mark=s.place_marker((619.908, 631.963, 559.218), (1, 1, 0.2), 17.1475)
if "Cog3_2" not in marker_sets:
  s=new_marker_set('Cog3_2')
  marker_sets["Cog3_2"]=s
s= marker_sets["Cog3_2"]
mark=s.place_marker((623.668, 618.75, 534.281), (1, 1, 0.2), 17.1475)
if "Cog3_3" not in marker_sets:
  s=new_marker_set('Cog3_3')
  marker_sets["Cog3_3"]=s
s= marker_sets["Cog3_3"]
mark=s.place_marker((625.929, 591.73, 526.085), (1, 1, 0.2), 17.1475)
if "Cog3_4" not in marker_sets:
  s=new_marker_set('Cog3_4')
  marker_sets["Cog3_4"]=s
s= marker_sets["Cog3_4"]
mark=s.place_marker((633.805, 565.636, 533.295), (1, 1, 0.2), 17.1475)
if "Cog3_5" not in marker_sets:
  s=new_marker_set('Cog3_5')
  marker_sets["Cog3_5"]=s
s= marker_sets["Cog3_5"]
mark=s.place_marker((660.225, 573.585, 527.633), (1, 1, 0.2), 17.1475)
if "Cog3_GFPC" not in marker_sets:
  s=new_marker_set('Cog3_GFPC')
  marker_sets["Cog3_GFPC"]=s
s= marker_sets["Cog3_GFPC"]
mark=s.place_marker((572.778, 627.147, 555.985), (1, 1, 0.4), 18.4716)
if "Cog3_Anch" not in marker_sets:
  s=new_marker_set('Cog3_Anch')
  marker_sets["Cog3_Anch"]=s
s= marker_sets["Cog3_Anch"]
mark=s.place_marker((752.186, 523.515, 505.736), (1, 1, 0.4), 18.4716)
if "Cog4_GFPN" not in marker_sets:
  s=new_marker_set('Cog4_GFPN')
  marker_sets["Cog4_GFPN"]=s
s= marker_sets["Cog4_GFPN"]
mark=s.place_marker((812.378, 708.375, 561.014), (0, 0, 0.8), 18.4716)
if "Cog4_0" not in marker_sets:
  s=new_marker_set('Cog4_0')
  marker_sets["Cog4_0"]=s
s= marker_sets["Cog4_0"]
mark=s.place_marker((812.378, 708.375, 561.014), (0, 0, 0.8), 17.1475)
if "Cog4_1" not in marker_sets:
  s=new_marker_set('Cog4_1')
  marker_sets["Cog4_1"]=s
s= marker_sets["Cog4_1"]
mark=s.place_marker((788.42, 693.575, 554.235), (0, 0, 0.8), 17.1475)
if "Cog4_2" not in marker_sets:
  s=new_marker_set('Cog4_2')
  marker_sets["Cog4_2"]=s
s= marker_sets["Cog4_2"]
mark=s.place_marker((763.224, 680.928, 549.174), (0, 0, 0.8), 17.1475)
if "Cog4_3" not in marker_sets:
  s=new_marker_set('Cog4_3')
  marker_sets["Cog4_3"]=s
s= marker_sets["Cog4_3"]
mark=s.place_marker((736.597, 670.432, 547.303), (0, 0, 0.8), 17.1475)
if "Cog4_4" not in marker_sets:
  s=new_marker_set('Cog4_4')
  marker_sets["Cog4_4"]=s
s= marker_sets["Cog4_4"]
mark=s.place_marker((708.503, 664.522, 549.023), (0, 0, 0.8), 17.1475)
if "Cog4_5" not in marker_sets:
  s=new_marker_set('Cog4_5')
  marker_sets["Cog4_5"]=s
s= marker_sets["Cog4_5"]
mark=s.place_marker((680.54, 664.384, 556.108), (0, 0, 0.8), 17.1475)
if "Cog4_6" not in marker_sets:
  s=new_marker_set('Cog4_6')
  marker_sets["Cog4_6"]=s
s= marker_sets["Cog4_6"]
mark=s.place_marker((652.873, 665.534, 564.758), (0, 0, 0.8), 17.1475)
if "Cog4_GFPC" not in marker_sets:
  s=new_marker_set('Cog4_GFPC')
  marker_sets["Cog4_GFPC"]=s
s= marker_sets["Cog4_GFPC"]
mark=s.place_marker((881.64, 606.623, 464.7), (0, 0, 0.8), 18.4716)
if "Cog4_Anch" not in marker_sets:
  s=new_marker_set('Cog4_Anch')
  marker_sets["Cog4_Anch"]=s
s= marker_sets["Cog4_Anch"]
mark=s.place_marker((417.405, 721.536, 663.307), (0, 0, 0.8), 18.4716)
if "Cog5_GFPN" not in marker_sets:
  s=new_marker_set('Cog5_GFPN')
  marker_sets["Cog5_GFPN"]=s
s= marker_sets["Cog5_GFPN"]
mark=s.place_marker((650.76, 705.733, 581.794), (0.3, 0.3, 0.3), 18.4716)
if "Cog5_0" not in marker_sets:
  s=new_marker_set('Cog5_0')
  marker_sets["Cog5_0"]=s
s= marker_sets["Cog5_0"]
mark=s.place_marker((650.76, 705.733, 581.794), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_1" not in marker_sets:
  s=new_marker_set('Cog5_1')
  marker_sets["Cog5_1"]=s
s= marker_sets["Cog5_1"]
mark=s.place_marker((659.342, 704.629, 553.65), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_2" not in marker_sets:
  s=new_marker_set('Cog5_2')
  marker_sets["Cog5_2"]=s
s= marker_sets["Cog5_2"]
mark=s.place_marker((654.86, 708.098, 525.134), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_3" not in marker_sets:
  s=new_marker_set('Cog5_3')
  marker_sets["Cog5_3"]=s
s= marker_sets["Cog5_3"]
mark=s.place_marker((634.771, 724.381, 511.672), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_GFPC" not in marker_sets:
  s=new_marker_set('Cog5_GFPC')
  marker_sets["Cog5_GFPC"]=s
s= marker_sets["Cog5_GFPC"]
mark=s.place_marker((547.772, 636.033, 494.28), (0.3, 0.3, 0.3), 18.4716)
if "Cog5_Anch" not in marker_sets:
  s=new_marker_set('Cog5_Anch')
  marker_sets["Cog5_Anch"]=s
s= marker_sets["Cog5_Anch"]
mark=s.place_marker((711.716, 821.821, 525.234), (0.3, 0.3, 0.3), 18.4716)
if "Cog6_GFPN" not in marker_sets:
  s=new_marker_set('Cog6_GFPN')
  marker_sets["Cog6_GFPN"]=s
s= marker_sets["Cog6_GFPN"]
mark=s.place_marker((585.639, 660.6, 523.058), (0.21, 0.49, 0.72), 18.4716)
if "Cog6_0" not in marker_sets:
  s=new_marker_set('Cog6_0')
  marker_sets["Cog6_0"]=s
s= marker_sets["Cog6_0"]
mark=s.place_marker((585.427, 660.722, 522.537), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_1" not in marker_sets:
  s=new_marker_set('Cog6_1')
  marker_sets["Cog6_1"]=s
s= marker_sets["Cog6_1"]
mark=s.place_marker((575.83, 635.38, 515.65), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_2" not in marker_sets:
  s=new_marker_set('Cog6_2')
  marker_sets["Cog6_2"]=s
s= marker_sets["Cog6_2"]
mark=s.place_marker((576.633, 612.086, 530.809), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_3" not in marker_sets:
  s=new_marker_set('Cog6_3')
  marker_sets["Cog6_3"]=s
s= marker_sets["Cog6_3"]
mark=s.place_marker((594.531, 595.519, 544.457), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_4" not in marker_sets:
  s=new_marker_set('Cog6_4')
  marker_sets["Cog6_4"]=s
s= marker_sets["Cog6_4"]
mark=s.place_marker((604.14, 580.78, 566.423), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_5" not in marker_sets:
  s=new_marker_set('Cog6_5')
  marker_sets["Cog6_5"]=s
s= marker_sets["Cog6_5"]
mark=s.place_marker((632.169, 582.803, 567.955), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_6" not in marker_sets:
  s=new_marker_set('Cog6_6')
  marker_sets["Cog6_6"]=s
s= marker_sets["Cog6_6"]
mark=s.place_marker((658.672, 577.447, 560.433), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_GFPC" not in marker_sets:
  s=new_marker_set('Cog6_GFPC')
  marker_sets["Cog6_GFPC"]=s
s= marker_sets["Cog6_GFPC"]
mark=s.place_marker((625.652, 636.703, 612.493), (0.21, 0.49, 0.72), 18.4716)
if "Cog6_Anch" not in marker_sets:
  s=new_marker_set('Cog6_Anch')
  marker_sets["Cog6_Anch"]=s
s= marker_sets["Cog6_Anch"]
mark=s.place_marker((692.507, 519.993, 503.511), (0.21, 0.49, 0.72), 18.4716)
if "Cog7_GFPN" not in marker_sets:
  s=new_marker_set('Cog7_GFPN')
  marker_sets["Cog7_GFPN"]=s
s= marker_sets["Cog7_GFPN"]
mark=s.place_marker((601.128, 675.644, 608.623), (0.7, 0.7, 0.7), 18.4716)
if "Cog7_0" not in marker_sets:
  s=new_marker_set('Cog7_0')
  marker_sets["Cog7_0"]=s
s= marker_sets["Cog7_0"]
mark=s.place_marker((602.373, 683.471, 583.793), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_1" not in marker_sets:
  s=new_marker_set('Cog7_1')
  marker_sets["Cog7_1"]=s
s= marker_sets["Cog7_1"]
mark=s.place_marker((606.535, 702.651, 529.544), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_2" not in marker_sets:
  s=new_marker_set('Cog7_2')
  marker_sets["Cog7_2"]=s
s= marker_sets["Cog7_2"]
mark=s.place_marker((610.868, 720.972, 475.118), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_GFPC" not in marker_sets:
  s=new_marker_set('Cog7_GFPC')
  marker_sets["Cog7_GFPC"]=s
s= marker_sets["Cog7_GFPC"]
mark=s.place_marker((533.719, 694.295, 470.952), (0.7, 0.7, 0.7), 18.4716)
if "Cog7_Anch" not in marker_sets:
  s=new_marker_set('Cog7_Anch')
  marker_sets["Cog7_Anch"]=s
s= marker_sets["Cog7_Anch"]
mark=s.place_marker((672.807, 765.909, 404.604), (0.7, 0.7, 0.7), 18.4716)
if "Cog8_0" not in marker_sets:
  s=new_marker_set('Cog8_0')
  marker_sets["Cog8_0"]=s
s= marker_sets["Cog8_0"]
mark=s.place_marker((561.908, 658.564, 494.186), (1, 0.5, 0), 17.1475)
if "Cog8_1" not in marker_sets:
  s=new_marker_set('Cog8_1')
  marker_sets["Cog8_1"]=s
s= marker_sets["Cog8_1"]
mark=s.place_marker((570.71, 684.786, 498.34), (1, 0.5, 0), 17.1475)
if "Cog8_2" not in marker_sets:
  s=new_marker_set('Cog8_2')
  marker_sets["Cog8_2"]=s
s= marker_sets["Cog8_2"]
mark=s.place_marker((579.208, 710.732, 505.218), (1, 0.5, 0), 17.1475)
if "Cog8_3" not in marker_sets:
  s=new_marker_set('Cog8_3')
  marker_sets["Cog8_3"]=s
s= marker_sets["Cog8_3"]
mark=s.place_marker((583.822, 730.038, 525.221), (1, 0.5, 0), 17.1475)
if "Cog8_4" not in marker_sets:
  s=new_marker_set('Cog8_4')
  marker_sets["Cog8_4"]=s
s= marker_sets["Cog8_4"]
mark=s.place_marker((597.94, 745.14, 544.199), (1, 0.5, 0), 17.1475)
if "Cog8_5" not in marker_sets:
  s=new_marker_set('Cog8_5')
  marker_sets["Cog8_5"]=s
s= marker_sets["Cog8_5"]
mark=s.place_marker((611.905, 765.062, 557.578), (1, 0.5, 0), 17.1475)
if "Cog8_GFPC" not in marker_sets:
  s=new_marker_set('Cog8_GFPC')
  marker_sets["Cog8_GFPC"]=s
s= marker_sets["Cog8_GFPC"]
mark=s.place_marker((590.523, 686.806, 560.614), (1, 0.6, 0.1), 18.4716)
if "Cog8_Anch" not in marker_sets:
  s=new_marker_set('Cog8_Anch')
  marker_sets["Cog8_Anch"]=s
s= marker_sets["Cog8_Anch"]
mark=s.place_marker((632.939, 843.689, 553.686), (1, 0.6, 0.1), 18.4716)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
