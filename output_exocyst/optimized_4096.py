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
mark=s.place_marker((478.546, 526.631, 481.825), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_1" not in marker_sets:
  s=new_marker_set('Sec3_1')
  marker_sets["Sec3_1"]=s
s= marker_sets["Sec3_1"]
mark=s.place_marker((494.296, 503.953, 465.721), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_2" not in marker_sets:
  s=new_marker_set('Sec3_2')
  marker_sets["Sec3_2"]=s
s= marker_sets["Sec3_2"]
mark=s.place_marker((482.361, 474.735, 460.422), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_3" not in marker_sets:
  s=new_marker_set('Sec3_3')
  marker_sets["Sec3_3"]=s
s= marker_sets["Sec3_3"]
mark=s.place_marker((454.478, 467.915, 460.303), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_4" not in marker_sets:
  s=new_marker_set('Sec3_4')
  marker_sets["Sec3_4"]=s
s= marker_sets["Sec3_4"]
mark=s.place_marker((438.819, 452.175, 478.522), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_5" not in marker_sets:
  s=new_marker_set('Sec3_5')
  marker_sets["Sec3_5"]=s
s= marker_sets["Sec3_5"]
mark=s.place_marker((440.974, 434.688, 501.18), (0.21, 0.49, 0.72), 17.1475)
if "Sec3_6" not in marker_sets:
  s=new_marker_set('Sec3_6')
  marker_sets["Sec3_6"]=s
s= marker_sets["Sec3_6"]
mark=s.place_marker((458.724, 412.899, 507.041), (0.21, 0.49, 0.72), 17.1475)
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
mark=s.place_marker((484.076, 529.901, 514.075), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_1" not in marker_sets:
  s=new_marker_set('Sec5_1')
  marker_sets["Sec5_1"]=s
s= marker_sets["Sec5_1"]
mark=s.place_marker((456.674, 526.964, 508.201), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_2" not in marker_sets:
  s=new_marker_set('Sec5_2')
  marker_sets["Sec5_2"]=s
s= marker_sets["Sec5_2"]
mark=s.place_marker((441.236, 503.735, 504.272), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_3" not in marker_sets:
  s=new_marker_set('Sec5_3')
  marker_sets["Sec5_3"]=s
s= marker_sets["Sec5_3"]
mark=s.place_marker((426.595, 486.678, 487.372), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_4" not in marker_sets:
  s=new_marker_set('Sec5_4')
  marker_sets["Sec5_4"]=s
s= marker_sets["Sec5_4"]
mark=s.place_marker((411.201, 473.848, 467.657), (0.6, 0.31, 0.64), 17.1475)
if "Sec5_5" not in marker_sets:
  s=new_marker_set('Sec5_5')
  marker_sets["Sec5_5"]=s
s= marker_sets["Sec5_5"]
mark=s.place_marker((412.578, 478.997, 440.065), (0.6, 0.31, 0.64), 17.1475)
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
mark=s.place_marker((472.259, 497.946, 517.379), (1, 1, 0.2), 17.1475)
if "Sec6_1" not in marker_sets:
  s=new_marker_set('Sec6_1')
  marker_sets["Sec6_1"]=s
s= marker_sets["Sec6_1"]
mark=s.place_marker((467.503, 494.534, 483.718), (1, 1, 0.2), 17.1475)
if "Sec6_2" not in marker_sets:
  s=new_marker_set('Sec6_2')
  marker_sets["Sec6_2"]=s
s= marker_sets["Sec6_2"]
mark=s.place_marker((464.802, 500.983, 448.871), (1, 1, 0.2), 17.1475)
if "Sec6_3" not in marker_sets:
  s=new_marker_set('Sec6_3')
  marker_sets["Sec6_3"]=s
s= marker_sets["Sec6_3"]
mark=s.place_marker((462.492, 506.601, 414.274), (1, 1, 0.2), 17.1475)
if "Sec6_4" not in marker_sets:
  s=new_marker_set('Sec6_4')
  marker_sets["Sec6_4"]=s
s= marker_sets["Sec6_4"]
mark=s.place_marker((455.119, 512.534, 379.26), (1, 1, 0.2), 17.1475)
if "Sec6_5" not in marker_sets:
  s=new_marker_set('Sec6_5')
  marker_sets["Sec6_5"]=s
s= marker_sets["Sec6_5"]
mark=s.place_marker((446.744, 523.668, 345.796), (1, 1, 0.2), 17.1475)
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
mark=s.place_marker((522.925, 443.857, 505.302), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_1" not in marker_sets:
  s=new_marker_set('Sec8_1')
  marker_sets["Sec8_1"]=s
s= marker_sets["Sec8_1"]
mark=s.place_marker((497.04, 447.714, 495.053), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_2" not in marker_sets:
  s=new_marker_set('Sec8_2')
  marker_sets["Sec8_2"]=s
s= marker_sets["Sec8_2"]
mark=s.place_marker((471.47, 455.662, 486.48), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_3" not in marker_sets:
  s=new_marker_set('Sec8_3')
  marker_sets["Sec8_3"]=s
s= marker_sets["Sec8_3"]
mark=s.place_marker((463.602, 428.698, 477.133), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_4" not in marker_sets:
  s=new_marker_set('Sec8_4')
  marker_sets["Sec8_4"]=s
s= marker_sets["Sec8_4"]
mark=s.place_marker((447.655, 403.781, 476.217), (0.65, 0.34, 0.16), 17.1475)
if "Sec8_5" not in marker_sets:
  s=new_marker_set('Sec8_5')
  marker_sets["Sec8_5"]=s
s= marker_sets["Sec8_5"]
mark=s.place_marker((432.201, 378.776, 478.964), (0.65, 0.34, 0.16), 17.1475)
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
mark=s.place_marker((462.276, 456.435, 332.048), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_1" not in marker_sets:
  s=new_marker_set('Sec10_1')
  marker_sets["Sec10_1"]=s
s= marker_sets["Sec10_1"]
mark=s.place_marker((441.838, 460.653, 350.863), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_2" not in marker_sets:
  s=new_marker_set('Sec10_2')
  marker_sets["Sec10_2"]=s
s= marker_sets["Sec10_2"]
mark=s.place_marker((447.903, 445.729, 373.884), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_3" not in marker_sets:
  s=new_marker_set('Sec10_3')
  marker_sets["Sec10_3"]=s
s= marker_sets["Sec10_3"]
mark=s.place_marker((434.454, 464.856, 397.309), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_4" not in marker_sets:
  s=new_marker_set('Sec10_4')
  marker_sets["Sec10_4"]=s
s= marker_sets["Sec10_4"]
mark=s.place_marker((425.094, 489.023, 386.453), (0.3, 0.69, 0.29), 17.1475)
if "Sec10_5" not in marker_sets:
  s=new_marker_set('Sec10_5')
  marker_sets["Sec10_5"]=s
s= marker_sets["Sec10_5"]
mark=s.place_marker((430.802, 508.46, 405.929), (0.3, 0.69, 0.29), 17.1475)
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
mark=s.place_marker((405.932, 516.114, 428.24), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_1" not in marker_sets:
  s=new_marker_set('Sec15_1')
  marker_sets["Sec15_1"]=s
s= marker_sets["Sec15_1"]
mark=s.place_marker((385.422, 504.235, 443.338), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_2" not in marker_sets:
  s=new_marker_set('Sec15_2')
  marker_sets["Sec15_2"]=s
s= marker_sets["Sec15_2"]
mark=s.place_marker((365.841, 510.88, 424.312), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_3" not in marker_sets:
  s=new_marker_set('Sec15_3')
  marker_sets["Sec15_3"]=s
s= marker_sets["Sec15_3"]
mark=s.place_marker((352.246, 501.785, 401.465), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_4" not in marker_sets:
  s=new_marker_set('Sec15_4')
  marker_sets["Sec15_4"]=s
s= marker_sets["Sec15_4"]
mark=s.place_marker((335.653, 490.746, 381.657), (0.97, 0.51, 0.75), 17.1475)
if "Sec15_5" not in marker_sets:
  s=new_marker_set('Sec15_5')
  marker_sets["Sec15_5"]=s
s= marker_sets["Sec15_5"]
mark=s.place_marker((312.23, 484.27, 367.553), (0.97, 0.51, 0.75), 17.1475)
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
mark=s.place_marker((419.567, 524.557, 488.001), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_1" not in marker_sets:
  s=new_marker_set('Exo70_1')
  marker_sets["Exo70_1"]=s
s= marker_sets["Exo70_1"]
mark=s.place_marker((432.052, 512.644, 464.853), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_2" not in marker_sets:
  s=new_marker_set('Exo70_2')
  marker_sets["Exo70_2"]=s
s= marker_sets["Exo70_2"]
mark=s.place_marker((438.513, 518.77, 437.296), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_3" not in marker_sets:
  s=new_marker_set('Exo70_3')
  marker_sets["Exo70_3"]=s
s= marker_sets["Exo70_3"]
mark=s.place_marker((446.326, 536.724, 416.217), (0.89, 0.1, 0.1), 17.1475)
if "Exo70_4" not in marker_sets:
  s=new_marker_set('Exo70_4')
  marker_sets["Exo70_4"]=s
s= marker_sets["Exo70_4"]
mark=s.place_marker((449.344, 543.406, 388.461), (0.89, 0.1, 0.1), 17.1475)
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
mark=s.place_marker((456.486, 535.97, 459.836), (1, 0.5, 0), 17.1475)
if "Exo84_1" not in marker_sets:
  s=new_marker_set('Exo84_1')
  marker_sets["Exo84_1"]=s
s= marker_sets["Exo84_1"]
mark=s.place_marker((418.559, 540.931, 452.968), (1, 0.5, 0), 17.1475)
if "Exo84_2" not in marker_sets:
  s=new_marker_set('Exo84_2')
  marker_sets["Exo84_2"]=s
s= marker_sets["Exo84_2"]
mark=s.place_marker((381.886, 539.554, 445.483), (1, 0.5, 0), 17.1475)
if "Exo84_3" not in marker_sets:
  s=new_marker_set('Exo84_3')
  marker_sets["Exo84_3"]=s
s= marker_sets["Exo84_3"]
mark=s.place_marker((350.538, 538.411, 439.086), (1, 0.5, 0), 17.1475)
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
