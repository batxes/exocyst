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
mark=s.place_marker((535.641, 593.745, 553.103), (0.15, 0.4, 0.6), 18.4716)
if "Sec3_0" not in marker_sets:
  s=new_marker_set('Sec3_0')
  marker_sets["Sec3_0"]=s
s= marker_sets["Sec3_0"]
mark=s.place_marker((526.163, 602.796, 577.887), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_1" not in marker_sets:
  s=new_marker_set('Sec3_1')
  marker_sets["Sec3_1"]=s
s= marker_sets["Sec3_1"]
mark=s.place_marker((517.008, 576.876, 593.127), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_2" not in marker_sets:
  s=new_marker_set('Sec3_2')
  marker_sets["Sec3_2"]=s
s= marker_sets["Sec3_2"]
mark=s.place_marker((533.014, 559.168, 613.575), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_3" not in marker_sets:
  s=new_marker_set('Sec3_3')
  marker_sets["Sec3_3"]=s
s= marker_sets["Sec3_3"]
mark=s.place_marker((558.945, 560.579, 624.306), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_4" not in marker_sets:
  s=new_marker_set('Sec3_4')
  marker_sets["Sec3_4"]=s
s= marker_sets["Sec3_4"]
mark=s.place_marker((585.896, 567.937, 627.325), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_5" not in marker_sets:
  s=new_marker_set('Sec3_5')
  marker_sets["Sec3_5"]=s
s= marker_sets["Sec3_5"]
mark=s.place_marker((611.956, 578.447, 627.431), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_6" not in marker_sets:
  s=new_marker_set('Sec3_6')
  marker_sets["Sec3_6"]=s
s= marker_sets["Sec3_6"]
mark=s.place_marker((623.838, 565.861, 649.566), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_GFPC" not in marker_sets:
  s=new_marker_set('Sec3_GFPC')
  marker_sets["Sec3_GFPC"]=s
s= marker_sets["Sec3_GFPC"]
mark=s.place_marker((521.31, 569.568, 598.694), (0.3, 0.6, 0.8), 18.4716)
if "Sec3_Anch" not in marker_sets:
  s=new_marker_set('Sec3_Anch')
  marker_sets["Sec3_Anch"]=s
s= marker_sets["Sec3_Anch"]
mark=s.place_marker((726.375, 562.158, 700.437), (0.3, 0.6, 0.8), 18.4716)
if "Sec5_GFPN" not in marker_sets:
  s=new_marker_set('Sec5_GFPN')
  marker_sets["Sec5_GFPN"]=s
s= marker_sets["Sec5_GFPN"]
mark=s.place_marker((566.996, 618.569, 556.866), (0.5, 0.3, 0.6), 18.4716)
if "Sec5_0" not in marker_sets:
  s=new_marker_set('Sec5_0')
  marker_sets["Sec5_0"]=s
s= marker_sets["Sec5_0"]
mark=s.place_marker((577.025, 624.878, 555.144), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_1" not in marker_sets:
  s=new_marker_set('Sec5_1')
  marker_sets["Sec5_1"]=s
s= marker_sets["Sec5_1"]
mark=s.place_marker((581.148, 628.54, 527.592), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_2" not in marker_sets:
  s=new_marker_set('Sec5_2')
  marker_sets["Sec5_2"]=s
s= marker_sets["Sec5_2"]
mark=s.place_marker((596.849, 607.199, 518.236), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_3" not in marker_sets:
  s=new_marker_set('Sec5_3')
  marker_sets["Sec5_3"]=s
s= marker_sets["Sec5_3"]
mark=s.place_marker((618.07, 605.189, 536.541), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_4" not in marker_sets:
  s=new_marker_set('Sec5_4')
  marker_sets["Sec5_4"]=s
s= marker_sets["Sec5_4"]
mark=s.place_marker((624.589, 595.256, 562.003), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_5" not in marker_sets:
  s=new_marker_set('Sec5_5')
  marker_sets["Sec5_5"]=s
s= marker_sets["Sec5_5"]
mark=s.place_marker((610.951, 578.559, 580.024), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_GFPC" not in marker_sets:
  s=new_marker_set('Sec5_GFPC')
  marker_sets["Sec5_GFPC"]=s
s= marker_sets["Sec5_GFPC"]
mark=s.place_marker((545.611, 538.15, 607.269), (0.7, 0.4, 0.7), 18.4716)
if "Sec6_GFPN" not in marker_sets:
  s=new_marker_set('Sec6_GFPN')
  marker_sets["Sec6_GFPN"]=s
s= marker_sets["Sec6_GFPN"]
mark=s.place_marker((547.051, 622.667, 621.128), (1, 1, 0), 18.4716)
if "Sec6_0" not in marker_sets:
  s=new_marker_set('Sec6_0')
  marker_sets["Sec6_0"]=s
s= marker_sets["Sec6_0"]
mark=s.place_marker((561.843, 608.851, 597.817), (1, 1, 0.2), 17.1475)
if "Sec6_1" not in marker_sets:
  s=new_marker_set('Sec6_1')
  marker_sets["Sec6_1"]=s
s= marker_sets["Sec6_1"]
mark=s.place_marker((578.302, 593.345, 572.578), (1, 1, 0.2), 17.1475)
if "Sec6_2" not in marker_sets:
  s=new_marker_set('Sec6_2')
  marker_sets["Sec6_2"]=s
s= marker_sets["Sec6_2"]
mark=s.place_marker((594.732, 577.836, 547.328), (1, 1, 0.2), 17.1475)
if "Sec6_3" not in marker_sets:
  s=new_marker_set('Sec6_3')
  marker_sets["Sec6_3"]=s
s= marker_sets["Sec6_3"]
mark=s.place_marker((611.131, 562.34, 522.065), (1, 1, 0.2), 17.1475)
if "Sec6_4" not in marker_sets:
  s=new_marker_set('Sec6_4')
  marker_sets["Sec6_4"]=s
s= marker_sets["Sec6_4"]
mark=s.place_marker((618.421, 553.985, 487.527), (1, 1, 0.2), 17.1475)
if "Sec6_5" not in marker_sets:
  s=new_marker_set('Sec6_5')
  marker_sets["Sec6_5"]=s
s= marker_sets["Sec6_5"]
mark=s.place_marker((627.392, 550.769, 454.163), (1, 1, 0.2), 17.1475)
if "Sec6_GFPC" not in marker_sets:
  s=new_marker_set('Sec6_GFPC')
  marker_sets["Sec6_GFPC"]=s
s= marker_sets["Sec6_GFPC"]
mark=s.place_marker((668.461, 556.663, 518.953), (1, 1, 0.4), 18.4716)
if "Sec6_Anch" not in marker_sets:
  s=new_marker_set('Sec6_Anch')
  marker_sets["Sec6_Anch"]=s
s= marker_sets["Sec6_Anch"]
mark=s.place_marker((617.586, 542.531, 361.748), (1, 1, 0.4), 18.4716)
if "Sec8_0" not in marker_sets:
  s=new_marker_set('Sec8_0')
  marker_sets["Sec8_0"]=s
s= marker_sets["Sec8_0"]
mark=s.place_marker((624.33, 513.903, 538.693), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_1" not in marker_sets:
  s=new_marker_set('Sec8_1')
  marker_sets["Sec8_1"]=s
s= marker_sets["Sec8_1"]
mark=s.place_marker((619.378, 540.278, 547.029), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_2" not in marker_sets:
  s=new_marker_set('Sec8_2')
  marker_sets["Sec8_2"]=s
s= marker_sets["Sec8_2"]
mark=s.place_marker((625.659, 528.034, 571.533), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_3" not in marker_sets:
  s=new_marker_set('Sec8_3')
  marker_sets["Sec8_3"]=s
s= marker_sets["Sec8_3"]
mark=s.place_marker((636.021, 520.138, 596.421), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_4" not in marker_sets:
  s=new_marker_set('Sec8_4')
  marker_sets["Sec8_4"]=s
s= marker_sets["Sec8_4"]
mark=s.place_marker((645.454, 523.424, 622.678), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_5" not in marker_sets:
  s=new_marker_set('Sec8_5')
  marker_sets["Sec8_5"]=s
s= marker_sets["Sec8_5"]
mark=s.place_marker((656.57, 527.002, 648.219), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_GFPC" not in marker_sets:
  s=new_marker_set('Sec8_GFPC')
  marker_sets["Sec8_GFPC"]=s
s= marker_sets["Sec8_GFPC"]
mark=s.place_marker((650.391, 496.924, 542.858), (0.7, 0.4, 0), 18.4716)
if "Sec8_Anch" not in marker_sets:
  s=new_marker_set('Sec8_Anch')
  marker_sets["Sec8_Anch"]=s
s= marker_sets["Sec8_Anch"]
mark=s.place_marker((662.636, 557.115, 753.535), (0.7, 0.4, 0), 18.4716)
if "Sec10_GFPN" not in marker_sets:
  s=new_marker_set('Sec10_GFPN')
  marker_sets["Sec10_GFPN"]=s
s= marker_sets["Sec10_GFPN"]
mark=s.place_marker((704.281, 503.596, 493.349), (0.2, 0.6, 0.2), 18.4716)
if "Sec10_0" not in marker_sets:
  s=new_marker_set('Sec10_0')
  marker_sets["Sec10_0"]=s
s= marker_sets["Sec10_0"]
mark=s.place_marker((691.799, 516.498, 494.036), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_1" not in marker_sets:
  s=new_marker_set('Sec10_1')
  marker_sets["Sec10_1"]=s
s= marker_sets["Sec10_1"]
mark=s.place_marker((671.242, 537.537, 496.046), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_2" not in marker_sets:
  s=new_marker_set('Sec10_2')
  marker_sets["Sec10_2"]=s
s= marker_sets["Sec10_2"]
mark=s.place_marker((650.697, 558.576, 498.085), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_3" not in marker_sets:
  s=new_marker_set('Sec10_3')
  marker_sets["Sec10_3"]=s
s= marker_sets["Sec10_3"]
mark=s.place_marker((626.045, 583.127, 500.2), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_4" not in marker_sets:
  s=new_marker_set('Sec10_4')
  marker_sets["Sec10_4"]=s
s= marker_sets["Sec10_4"]
mark=s.place_marker((596.971, 578.014, 499.145), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_5" not in marker_sets:
  s=new_marker_set('Sec10_5')
  marker_sets["Sec10_5"]=s
s= marker_sets["Sec10_5"]
mark=s.place_marker((584.163, 551.823, 506.133), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_GFPC" not in marker_sets:
  s=new_marker_set('Sec10_GFPC')
  marker_sets["Sec10_GFPC"]=s
s= marker_sets["Sec10_GFPC"]
mark=s.place_marker((540.06, 454.674, 611.871), (0.4, 0.75, 0.3), 18.4716)
if "Sec10_Anch" not in marker_sets:
  s=new_marker_set('Sec10_Anch')
  marker_sets["Sec10_Anch"]=s
s= marker_sets["Sec10_Anch"]
mark=s.place_marker((631.347, 641.621, 402.759), (0.4, 0.75, 0.3), 18.4716)
if "Sec15_GFPN" not in marker_sets:
  s=new_marker_set('Sec15_GFPN')
  marker_sets["Sec15_GFPN"]=s
s= marker_sets["Sec15_GFPN"]
mark=s.place_marker((568.942, 549.602, 529.226), (0.9, 0.5, 0.7), 18.4716)
if "Sec15_0" not in marker_sets:
  s=new_marker_set('Sec15_0')
  marker_sets["Sec15_0"]=s
s= marker_sets["Sec15_0"]
mark=s.place_marker((579.789, 543.361, 538.511), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_1" not in marker_sets:
  s=new_marker_set('Sec15_1')
  marker_sets["Sec15_1"]=s
s= marker_sets["Sec15_1"]
mark=s.place_marker((577.727, 516.93, 529.007), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_2" not in marker_sets:
  s=new_marker_set('Sec15_2')
  marker_sets["Sec15_2"]=s
s= marker_sets["Sec15_2"]
mark=s.place_marker((574.381, 492.155, 516.063), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_3" not in marker_sets:
  s=new_marker_set('Sec15_3')
  marker_sets["Sec15_3"]=s
s= marker_sets["Sec15_3"]
mark=s.place_marker((586.728, 471.43, 501.577), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_4" not in marker_sets:
  s=new_marker_set('Sec15_4')
  marker_sets["Sec15_4"]=s
s= marker_sets["Sec15_4"]
mark=s.place_marker((591.048, 444.046, 496.84), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_5" not in marker_sets:
  s=new_marker_set('Sec15_5')
  marker_sets["Sec15_5"]=s
s= marker_sets["Sec15_5"]
mark=s.place_marker((599.497, 417.24, 497.369), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_GFPC" not in marker_sets:
  s=new_marker_set('Sec15_GFPC')
  marker_sets["Sec15_GFPC"]=s
s= marker_sets["Sec15_GFPC"]
mark=s.place_marker((670.499, 448.5, 527.213), (1, 0.6, 0.8), 18.4716)
if "Sec15_Anch" not in marker_sets:
  s=new_marker_set('Sec15_Anch')
  marker_sets["Sec15_Anch"]=s
s= marker_sets["Sec15_Anch"]
mark=s.place_marker((528.487, 386.001, 467.526), (1, 0.6, 0.8), 18.4716)
if "Exo70_GFPN" not in marker_sets:
  s=new_marker_set('Exo70_GFPN')
  marker_sets["Exo70_GFPN"]=s
s= marker_sets["Exo70_GFPN"]
mark=s.place_marker((524.04, 568.181, 572.181), (0.8, 0, 0), 18.4716)
if "Exo70_0" not in marker_sets:
  s=new_marker_set('Exo70_0')
  marker_sets["Exo70_0"]=s
s= marker_sets["Exo70_0"]
mark=s.place_marker((525.276, 571.671, 556.963), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_1" not in marker_sets:
  s=new_marker_set('Exo70_1')
  marker_sets["Exo70_1"]=s
s= marker_sets["Exo70_1"]
mark=s.place_marker((529.258, 580.251, 529.881), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_2" not in marker_sets:
  s=new_marker_set('Exo70_2')
  marker_sets["Exo70_2"]=s
s= marker_sets["Exo70_2"]
mark=s.place_marker((547.537, 576.504, 508.04), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_3" not in marker_sets:
  s=new_marker_set('Exo70_3')
  marker_sets["Exo70_3"]=s
s= marker_sets["Exo70_3"]
mark=s.place_marker((565.864, 572.742, 486.2), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_4" not in marker_sets:
  s=new_marker_set('Exo70_4')
  marker_sets["Exo70_4"]=s
s= marker_sets["Exo70_4"]
mark=s.place_marker((588.553, 568.851, 468.912), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_GFPC" not in marker_sets:
  s=new_marker_set('Exo70_GFPC')
  marker_sets["Exo70_GFPC"]=s
s= marker_sets["Exo70_GFPC"]
mark=s.place_marker((705.748, 474.225, 557.579), (1, 0.2, 0.2), 18.4716)
if "Exo70_Anch" not in marker_sets:
  s=new_marker_set('Exo70_Anch')
  marker_sets["Exo70_Anch"]=s
s= marker_sets["Exo70_Anch"]
mark=s.place_marker((477.603, 670.358, 384.03), (1, 0.2, 0.2), 18.4716)
if "Exo84_GFPN" not in marker_sets:
  s=new_marker_set('Exo84_GFPN')
  marker_sets["Exo84_GFPN"]=s
s= marker_sets["Exo84_GFPN"]
mark=s.place_marker((568.263, 615.714, 542.602), (0.9, 0.4, 0), 18.4716)
if "Exo84_0" not in marker_sets:
  s=new_marker_set('Exo84_0')
  marker_sets["Exo84_0"]=s
s= marker_sets["Exo84_0"]
mark=s.place_marker((560.634, 589.396, 539.676), (1, 0.5, 0), 17.1475)
if "Exo84_1" not in marker_sets:
  s=new_marker_set('Exo84_1')
  marker_sets["Exo84_1"]=s
s= marker_sets["Exo84_1"]
mark=s.place_marker((547.887, 552.429, 533.857), (1, 0.5, 0), 17.1475)
if "Exo84_2" not in marker_sets:
  s=new_marker_set('Exo84_2')
  marker_sets["Exo84_2"]=s
s= marker_sets["Exo84_2"]
mark=s.place_marker((537.07, 515.697, 528.339), (1, 0.5, 0), 17.1475)
if "Exo84_3" not in marker_sets:
  s=new_marker_set('Exo84_3')
  marker_sets["Exo84_3"]=s
s= marker_sets["Exo84_3"]
mark=s.place_marker((527.868, 484.957, 523.785), (1, 0.5, 0), 17.1475)
if "Exo84_GFPC" not in marker_sets:
  s=new_marker_set('Exo84_GFPC')
  marker_sets["Exo84_GFPC"]=s
s= marker_sets["Exo84_GFPC"]
mark=s.place_marker((568.791, 511.347, 608.299), (1, 0.6, 0.1), 18.4716)
if "Exo84_Anch" not in marker_sets:
  s=new_marker_set('Exo84_Anch')
  marker_sets["Exo84_Anch"]=s
s= marker_sets["Exo84_Anch"]
mark=s.place_marker((482.881, 430.091, 445.773), (1, 0.6, 0.1), 18.4716)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
