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
mark=s.place_marker((452.25, 542.286, 492.08), (0.15, 0.4, 0.6), 18.4716)
if "Sec3_0" not in marker_sets:
  s=new_marker_set('Sec3_0')
  marker_sets["Sec3_0"]=s
s= marker_sets["Sec3_0"]
mark=s.place_marker((446.99, 545.034, 520.381), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_1" not in marker_sets:
  s=new_marker_set('Sec3_1')
  marker_sets["Sec3_1"]=s
s= marker_sets["Sec3_1"]
mark=s.place_marker((444.119, 516.473, 533.196), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_2" not in marker_sets:
  s=new_marker_set('Sec3_2')
  marker_sets["Sec3_2"]=s
s= marker_sets["Sec3_2"]
mark=s.place_marker((439.985, 489.783, 517.069), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_3" not in marker_sets:
  s=new_marker_set('Sec3_3')
  marker_sets["Sec3_3"]=s
s= marker_sets["Sec3_3"]
mark=s.place_marker((455.776, 471.289, 502.959), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_4" not in marker_sets:
  s=new_marker_set('Sec3_4')
  marker_sets["Sec3_4"]=s
s= marker_sets["Sec3_4"]
mark=s.place_marker((474.507, 451.371, 496.404), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_5" not in marker_sets:
  s=new_marker_set('Sec3_5')
  marker_sets["Sec3_5"]=s
s= marker_sets["Sec3_5"]
mark=s.place_marker((482.853, 424.525, 496.373), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_6" not in marker_sets:
  s=new_marker_set('Sec3_6')
  marker_sets["Sec3_6"]=s
s= marker_sets["Sec3_6"]
mark=s.place_marker((459.732, 412.379, 506.76), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_GFPC" not in marker_sets:
  s=new_marker_set('Sec3_GFPC')
  marker_sets["Sec3_GFPC"]=s
s= marker_sets["Sec3_GFPC"]
mark=s.place_marker((422.307, 518.031, 526.873), (0.3, 0.6, 0.8), 18.4716)
if "Sec3_Anch" not in marker_sets:
  s=new_marker_set('Sec3_Anch')
  marker_sets["Sec3_Anch"]=s
s= marker_sets["Sec3_Anch"]
mark=s.place_marker((497.009, 306.663, 486.71), (0.3, 0.6, 0.8), 18.4716)
if "Sec5_GFPN" not in marker_sets:
  s=new_marker_set('Sec5_GFPN')
  marker_sets["Sec5_GFPN"]=s
s= marker_sets["Sec5_GFPN"]
mark=s.place_marker((483.096, 528.551, 497.237), (0.5, 0.3, 0.6), 18.4716)
if "Sec5_0" not in marker_sets:
  s=new_marker_set('Sec5_0')
  marker_sets["Sec5_0"]=s
s= marker_sets["Sec5_0"]
mark=s.place_marker((470.626, 532.638, 498.852), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_1" not in marker_sets:
  s=new_marker_set('Sec5_1')
  marker_sets["Sec5_1"]=s
s= marker_sets["Sec5_1"]
mark=s.place_marker((446.708, 517.897, 498.709), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_2" not in marker_sets:
  s=new_marker_set('Sec5_2')
  marker_sets["Sec5_2"]=s
s= marker_sets["Sec5_2"]
mark=s.place_marker((425.256, 506.188, 484.81), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_3" not in marker_sets:
  s=new_marker_set('Sec5_3')
  marker_sets["Sec5_3"]=s
s= marker_sets["Sec5_3"]
mark=s.place_marker((399.6, 516, 478.817), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_4" not in marker_sets:
  s=new_marker_set('Sec5_4')
  marker_sets["Sec5_4"]=s
s= marker_sets["Sec5_4"]
mark=s.place_marker((384.309, 539.456, 481.293), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_5" not in marker_sets:
  s=new_marker_set('Sec5_5')
  marker_sets["Sec5_5"]=s
s= marker_sets["Sec5_5"]
mark=s.place_marker((357.053, 544.792, 477.006), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_GFPC" not in marker_sets:
  s=new_marker_set('Sec5_GFPC')
  marker_sets["Sec5_GFPC"]=s
s= marker_sets["Sec5_GFPC"]
mark=s.place_marker((399.085, 485.531, 510.933), (0.7, 0.4, 0.7), 18.4716)
if "Sec6_GFPN" not in marker_sets:
  s=new_marker_set('Sec6_GFPN')
  marker_sets["Sec6_GFPN"]=s
s= marker_sets["Sec6_GFPN"]
mark=s.place_marker((475.139, 500.646, 549.303), (1, 1, 0), 18.4716)
if "Sec6_0" not in marker_sets:
  s=new_marker_set('Sec6_0')
  marker_sets["Sec6_0"]=s
s= marker_sets["Sec6_0"]
mark=s.place_marker((474.023, 501.684, 515.4), (1, 1, 0.2), 17.1475)
if "Sec6_1" not in marker_sets:
  s=new_marker_set('Sec6_1')
  marker_sets["Sec6_1"]=s
s= marker_sets["Sec6_1"]
mark=s.place_marker((471.839, 503.929, 480.114), (1, 1, 0.2), 17.1475)
if "Sec6_2" not in marker_sets:
  s=new_marker_set('Sec6_2')
  marker_sets["Sec6_2"]=s
s= marker_sets["Sec6_2"]
mark=s.place_marker((469.468, 506.275, 444.898), (1, 1, 0.2), 17.1475)
if "Sec6_3" not in marker_sets:
  s=new_marker_set('Sec6_3')
  marker_sets["Sec6_3"]=s
s= marker_sets["Sec6_3"]
mark=s.place_marker((465.968, 510.781, 410.682), (1, 1, 0.2), 17.1475)
if "Sec6_4" not in marker_sets:
  s=new_marker_set('Sec6_4')
  marker_sets["Sec6_4"]=s
s= marker_sets["Sec6_4"]
mark=s.place_marker((457.863, 515.045, 376.667), (1, 1, 0.2), 17.1475)
if "Sec6_5" not in marker_sets:
  s=new_marker_set('Sec6_5')
  marker_sets["Sec6_5"]=s
s= marker_sets["Sec6_5"]
mark=s.place_marker((448.122, 524.258, 344.487), (1, 1, 0.2), 17.1475)
if "Sec6_GFPC" not in marker_sets:
  s=new_marker_set('Sec6_GFPC')
  marker_sets["Sec6_GFPC"]=s
s= marker_sets["Sec6_GFPC"]
mark=s.place_marker((463.163, 448.151, 366.263), (1, 1, 0.4), 18.4716)
if "Sec6_Anch" not in marker_sets:
  s=new_marker_set('Sec6_Anch')
  marker_sets["Sec6_Anch"]=s
s= marker_sets["Sec6_Anch"]
mark=s.place_marker((423.358, 589.653, 280.3), (1, 1, 0.4), 18.4716)
if "Sec8_0" not in marker_sets:
  s=new_marker_set('Sec8_0')
  marker_sets["Sec8_0"]=s
s= marker_sets["Sec8_0"]
mark=s.place_marker((474.02, 472.514, 533.628), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_1" not in marker_sets:
  s=new_marker_set('Sec8_1')
  marker_sets["Sec8_1"]=s
s= marker_sets["Sec8_1"]
mark=s.place_marker((462.632, 446.908, 531.31), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_2" not in marker_sets:
  s=new_marker_set('Sec8_2')
  marker_sets["Sec8_2"]=s
s= marker_sets["Sec8_2"]
mark=s.place_marker((443.592, 426.652, 535.48), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_3" not in marker_sets:
  s=new_marker_set('Sec8_3')
  marker_sets["Sec8_3"]=s
s= marker_sets["Sec8_3"]
mark=s.place_marker((429.713, 404.709, 524.723), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_4" not in marker_sets:
  s=new_marker_set('Sec8_4')
  marker_sets["Sec8_4"]=s
s= marker_sets["Sec8_4"]
mark=s.place_marker((429.53, 388.44, 501.812), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_5" not in marker_sets:
  s=new_marker_set('Sec8_5')
  marker_sets["Sec8_5"]=s
s= marker_sets["Sec8_5"]
mark=s.place_marker((427.623, 373.689, 477.973), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_GFPC" not in marker_sets:
  s=new_marker_set('Sec8_GFPC')
  marker_sets["Sec8_GFPC"]=s
s= marker_sets["Sec8_GFPC"]
mark=s.place_marker((397.481, 435.285, 396.787), (0.7, 0.4, 0), 18.4716)
if "Sec8_Anch" not in marker_sets:
  s=new_marker_set('Sec8_Anch')
  marker_sets["Sec8_Anch"]=s
s= marker_sets["Sec8_Anch"]
mark=s.place_marker((457.766, 312.114, 559.189), (0.7, 0.4, 0), 18.4716)
if "Sec10_GFPN" not in marker_sets:
  s=new_marker_set('Sec10_GFPN')
  marker_sets["Sec10_GFPN"]=s
s= marker_sets["Sec10_GFPN"]
mark=s.place_marker((461.37, 459.603, 334.456), (0.2, 0.6, 0.2), 18.4716)
if "Sec10_0" not in marker_sets:
  s=new_marker_set('Sec10_0')
  marker_sets["Sec10_0"]=s
s= marker_sets["Sec10_0"]
mark=s.place_marker((466.211, 463.654, 334.518), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_1" not in marker_sets:
  s=new_marker_set('Sec10_1')
  marker_sets["Sec10_1"]=s
s= marker_sets["Sec10_1"]
mark=s.place_marker((446.514, 481.034, 344.493), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_2" not in marker_sets:
  s=new_marker_set('Sec10_2')
  marker_sets["Sec10_2"]=s
s= marker_sets["Sec10_2"]
mark=s.place_marker((424.527, 474.594, 360.76), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_3" not in marker_sets:
  s=new_marker_set('Sec10_3')
  marker_sets["Sec10_3"]=s
s= marker_sets["Sec10_3"]
mark=s.place_marker((447.332, 462.674, 381.576), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_4" not in marker_sets:
  s=new_marker_set('Sec10_4')
  marker_sets["Sec10_4"]=s
s= marker_sets["Sec10_4"]
mark=s.place_marker((440.446, 485.693, 396.159), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_5" not in marker_sets:
  s=new_marker_set('Sec10_5')
  marker_sets["Sec10_5"]=s
s= marker_sets["Sec10_5"]
mark=s.place_marker((433.023, 509.521, 409.1), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_GFPC" not in marker_sets:
  s=new_marker_set('Sec10_GFPC')
  marker_sets["Sec10_GFPC"]=s
s= marker_sets["Sec10_GFPC"]
mark=s.place_marker((321.464, 463.925, 491.214), (0.4, 0.75, 0.3), 18.4716)
if "Sec10_Anch" not in marker_sets:
  s=new_marker_set('Sec10_Anch')
  marker_sets["Sec10_Anch"]=s
s= marker_sets["Sec10_Anch"]
mark=s.place_marker((549.906, 554.619, 331.935), (0.4, 0.75, 0.3), 18.4716)
if "Sec15_GFPN" not in marker_sets:
  s=new_marker_set('Sec15_GFPN')
  marker_sets["Sec15_GFPN"]=s
s= marker_sets["Sec15_GFPN"]
mark=s.place_marker((420.639, 516.57, 430.707), (0.9, 0.5, 0.7), 18.4716)
if "Sec15_0" not in marker_sets:
  s=new_marker_set('Sec15_0')
  marker_sets["Sec15_0"]=s
s= marker_sets["Sec15_0"]
mark=s.place_marker((406.629, 511.728, 430.317), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_1" not in marker_sets:
  s=new_marker_set('Sec15_1')
  marker_sets["Sec15_1"]=s
s= marker_sets["Sec15_1"]
mark=s.place_marker((387.697, 491.373, 426.284), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_2" not in marker_sets:
  s=new_marker_set('Sec15_2')
  marker_sets["Sec15_2"]=s
s= marker_sets["Sec15_2"]
mark=s.place_marker((364.369, 495.235, 411.112), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_3" not in marker_sets:
  s=new_marker_set('Sec15_3')
  marker_sets["Sec15_3"]=s
s= marker_sets["Sec15_3"]
mark=s.place_marker((340.108, 499.087, 397.477), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_4" not in marker_sets:
  s=new_marker_set('Sec15_4')
  marker_sets["Sec15_4"]=s
s= marker_sets["Sec15_4"]
mark=s.place_marker((322.218, 508.418, 377.925), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_5" not in marker_sets:
  s=new_marker_set('Sec15_5')
  marker_sets["Sec15_5"]=s
s= marker_sets["Sec15_5"]
mark=s.place_marker((312.241, 484.281, 367.556), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_GFPC" not in marker_sets:
  s=new_marker_set('Sec15_GFPC')
  marker_sets["Sec15_GFPC"]=s
s= marker_sets["Sec15_GFPC"]
mark=s.place_marker((361.302, 417.406, 366.31), (1, 0.6, 0.8), 18.4716)
if "Sec15_Anch" not in marker_sets:
  s=new_marker_set('Sec15_Anch')
  marker_sets["Sec15_Anch"]=s
s= marker_sets["Sec15_Anch"]
mark=s.place_marker((263.159, 551.133, 368.797), (1, 0.6, 0.8), 18.4716)
if "Exo70_GFPN" not in marker_sets:
  s=new_marker_set('Exo70_GFPN')
  marker_sets["Exo70_GFPN"]=s
s= marker_sets["Exo70_GFPN"]
mark=s.place_marker((414.232, 529.538, 502.19), (0.8, 0, 0), 18.4716)
if "Exo70_0" not in marker_sets:
  s=new_marker_set('Exo70_0')
  marker_sets["Exo70_0"]=s
s= marker_sets["Exo70_0"]
mark=s.place_marker((420.81, 539.346, 492.204), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_1" not in marker_sets:
  s=new_marker_set('Exo70_1')
  marker_sets["Exo70_1"]=s
s= marker_sets["Exo70_1"]
mark=s.place_marker((434.529, 555.495, 472.79), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_2" not in marker_sets:
  s=new_marker_set('Exo70_2')
  marker_sets["Exo70_2"]=s
s= marker_sets["Exo70_2"]
mark=s.place_marker((440.935, 555.506, 444.737), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_3" not in marker_sets:
  s=new_marker_set('Exo70_3')
  marker_sets["Exo70_3"]=s
s= marker_sets["Exo70_3"]
mark=s.place_marker((444.531, 549.272, 416.936), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_4" not in marker_sets:
  s=new_marker_set('Exo70_4')
  marker_sets["Exo70_4"]=s
s= marker_sets["Exo70_4"]
mark=s.place_marker((448.385, 543.89, 388.998), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_GFPC" not in marker_sets:
  s=new_marker_set('Exo70_GFPC')
  marker_sets["Exo70_GFPC"]=s
s= marker_sets["Exo70_GFPC"]
mark=s.place_marker((395.034, 379.324, 364.988), (1, 0.2, 0.2), 18.4716)
if "Exo70_Anch" not in marker_sets:
  s=new_marker_set('Exo70_Anch')
  marker_sets["Exo70_Anch"]=s
s= marker_sets["Exo70_Anch"]
mark=s.place_marker((509.963, 703.963, 400.71), (1, 0.2, 0.2), 18.4716)
if "Exo84_GFPN" not in marker_sets:
  s=new_marker_set('Exo84_GFPN')
  marker_sets["Exo84_GFPN"]=s
s= marker_sets["Exo84_GFPN"]
mark=s.place_marker((484.167, 529.899, 466.221), (0.9, 0.4, 0), 18.4716)
if "Exo84_0" not in marker_sets:
  s=new_marker_set('Exo84_0')
  marker_sets["Exo84_0"]=s
s= marker_sets["Exo84_0"]
mark=s.place_marker((456.741, 531.269, 463.225), (1, 0.5, 0), 17.1475)
if "Exo84_1" not in marker_sets:
  s=new_marker_set('Exo84_1')
  marker_sets["Exo84_1"]=s
s= marker_sets["Exo84_1"]
mark=s.place_marker((418.899, 531.649, 454.926), (1, 0.5, 0), 17.1475)
if "Exo84_2" not in marker_sets:
  s=new_marker_set('Exo84_2')
  marker_sets["Exo84_2"]=s
s= marker_sets["Exo84_2"]
mark=s.place_marker((381.914, 534.768, 446.376), (1, 0.5, 0), 17.1475)
if "Exo84_3" not in marker_sets:
  s=new_marker_set('Exo84_3')
  marker_sets["Exo84_3"]=s
s= marker_sets["Exo84_3"]
mark=s.place_marker((350.642, 537.412, 439.067), (1, 0.5, 0), 17.1475)
if "Exo84_GFPC" not in marker_sets:
  s=new_marker_set('Exo84_GFPC')
  marker_sets["Exo84_GFPC"]=s
s= marker_sets["Exo84_GFPC"]
mark=s.place_marker((381.405, 457.09, 488.981), (1, 0.6, 0.1), 18.4716)
if "Exo84_Anch" not in marker_sets:
  s=new_marker_set('Exo84_Anch')
  marker_sets["Exo84_Anch"]=s
s= marker_sets["Exo84_Anch"]
mark=s.place_marker((292.706, 611.017, 387.815), (1, 0.6, 0.1), 18.4716)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
