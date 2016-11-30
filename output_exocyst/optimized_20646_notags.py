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
if "Sec3_0" not in marker_sets:
  s=new_marker_set('Sec3_0')
  marker_sets["Sec3_0"]=s
s= marker_sets["Sec3_0"]
mark=s.place_marker((509.573, 602.148, 561.667), (0.21, 0.49, 0.72), 2)
if "Sec3_1" not in marker_sets:
  s=new_marker_set('Sec3_1')
  marker_sets["Sec3_1"]=s
s= marker_sets["Sec3_1"]
mark=s.place_marker((505.32, 581.324, 584.82), (0.21, 0.49, 0.72), 2)
if "Sec3_2" not in marker_sets:
  s=new_marker_set('Sec3_2')
  marker_sets["Sec3_2"]=s
s= marker_sets["Sec3_2"]
mark=s.place_marker((529.159, 562.954, 593.885), (0.21, 0.49, 0.72), 2)
if "Sec3_3" not in marker_sets:
  s=new_marker_set('Sec3_3')
  marker_sets["Sec3_3"]=s
s= marker_sets["Sec3_3"]
mark=s.place_marker((555.768, 558.416, 601.681), (0.21, 0.49, 0.72), 2)
if "Sec3_4" not in marker_sets:
  s=new_marker_set('Sec3_4')
  marker_sets["Sec3_4"]=s
s= marker_sets["Sec3_4"]
mark=s.place_marker((581.046, 562.098, 613.389), (0.21, 0.49, 0.72), 2)
if "Sec3_5" not in marker_sets:
  s=new_marker_set('Sec3_5')
  marker_sets["Sec3_5"]=s
s= marker_sets["Sec3_5"]
mark=s.place_marker((603.246, 564.585, 630.439), (0.21, 0.49, 0.72), 2)
if "Sec3_6" not in marker_sets:
  s=new_marker_set('Sec3_6')
  marker_sets["Sec3_6"]=s
s= marker_sets["Sec3_6"]
mark=s.place_marker((623.836, 565.854, 649.526), (0.21, 0.49, 0.72), 2)
if "Sec5_0" not in marker_sets:
  s=new_marker_set('Sec5_0')
  marker_sets["Sec5_0"]=s
s= marker_sets["Sec5_0"]
mark=s.place_marker((554.104, 623.367, 554.521), (0.6, 0.31, 0.64), 2)
if "Sec5_1" not in marker_sets:
  s=new_marker_set('Sec5_1')
  marker_sets["Sec5_1"]=s
s= marker_sets["Sec5_1"]
mark=s.place_marker((543.225, 601.294, 568.161), (0.6, 0.31, 0.64), 2)
if "Sec5_2" not in marker_sets:
  s=new_marker_set('Sec5_2')
  marker_sets["Sec5_2"]=s
s= marker_sets["Sec5_2"]
mark=s.place_marker((555.393, 576.06, 570.928), (0.6, 0.31, 0.64), 2)
if "Sec5_3" not in marker_sets:
  s=new_marker_set('Sec5_3')
  marker_sets["Sec5_3"]=s
s= marker_sets["Sec5_3"]
mark=s.place_marker((581.295, 566.55, 565.526), (0.6, 0.31, 0.64), 2)
if "Sec5_4" not in marker_sets:
  s=new_marker_set('Sec5_4')
  marker_sets["Sec5_4"]=s
s= marker_sets["Sec5_4"]
mark=s.place_marker((604.578, 551.607, 560.596), (0.6, 0.31, 0.64), 2)
if "Sec5_5" not in marker_sets:
  s=new_marker_set('Sec5_5')
  marker_sets["Sec5_5"]=s
s= marker_sets["Sec5_5"]
mark=s.place_marker((606.191, 523.747, 557.278), (0.6, 0.31, 0.64), 2)
if "Sec6_0" not in marker_sets:
  s=new_marker_set('Sec6_0')
  marker_sets["Sec6_0"]=s
s= marker_sets["Sec6_0"]
mark=s.place_marker((561.365, 613.1, 595.264), (1, 1, 0.2), 2)
if "Sec6_1" not in marker_sets:
  s=new_marker_set('Sec6_1')
  marker_sets["Sec6_1"]=s
s= marker_sets["Sec6_1"]
mark=s.place_marker((577.407, 602.029, 567.501), (1, 1, 0.2), 2)
if "Sec6_2" not in marker_sets:
  s=new_marker_set('Sec6_2')
  marker_sets["Sec6_2"]=s
s= marker_sets["Sec6_2"]
mark=s.place_marker((592.578, 590.975, 539.321), (1, 1, 0.2), 2)
if "Sec6_3" not in marker_sets:
  s=new_marker_set('Sec6_3')
  marker_sets["Sec6_3"]=s
s= marker_sets["Sec6_3"]
mark=s.place_marker((606.012, 579.676, 510.534), (1, 1, 0.2), 2)
if "Sec6_4" not in marker_sets:
  s=new_marker_set('Sec6_4')
  marker_sets["Sec6_4"]=s
s= marker_sets["Sec6_4"]
mark=s.place_marker((619.537, 568.34, 481.802), (1, 1, 0.2), 2)
if "Sec6_5" not in marker_sets:
  s=new_marker_set('Sec6_5')
  marker_sets["Sec6_5"]=s
s= marker_sets["Sec6_5"]
mark=s.place_marker((628.955, 557.228, 451.486), (1, 1, 0.2), 2)
if "Sec8_0" not in marker_sets:
  s=new_marker_set('Sec8_0')
  marker_sets["Sec8_0"]=s
s= marker_sets["Sec8_0"]
mark=s.place_marker((632.974, 563.113, 523.696), (0.65, 0.34, 0.16), 2)
if "Sec8_1" not in marker_sets:
  s=new_marker_set('Sec8_1')
  marker_sets["Sec8_1"]=s
s= marker_sets["Sec8_1"]
mark=s.place_marker((647.696, 561.804, 547.587), (0.65, 0.34, 0.16), 2)
if "Sec8_2" not in marker_sets:
  s=new_marker_set('Sec8_2')
  marker_sets["Sec8_2"]=s
s= marker_sets["Sec8_2"]
mark=s.place_marker((637.354, 552.128, 571.854), (0.65, 0.34, 0.16), 2)
if "Sec8_3" not in marker_sets:
  s=new_marker_set('Sec8_3')
  marker_sets["Sec8_3"]=s
s= marker_sets["Sec8_3"]
mark=s.place_marker((650.919, 544.821, 595.351), (0.65, 0.34, 0.16), 2)
if "Sec8_4" not in marker_sets:
  s=new_marker_set('Sec8_4')
  marker_sets["Sec8_4"]=s
s= marker_sets["Sec8_4"]
mark=s.place_marker((654.945, 537.561, 622.195), (0.65, 0.34, 0.16), 2)
if "Sec8_5" not in marker_sets:
  s=new_marker_set('Sec8_5')
  marker_sets["Sec8_5"]=s
s= marker_sets["Sec8_5"]
mark=s.place_marker((656.513, 527.015, 648.194), (0.65, 0.34, 0.16), 2)
if "Sec10_0" not in marker_sets:
  s=new_marker_set('Sec10_0')
  marker_sets["Sec10_0"]=s
s= marker_sets["Sec10_0"]
mark=s.place_marker((699.953, 513.166, 491.699), (0.3, 0.69, 0.29), 2)
if "Sec10_1" not in marker_sets:
  s=new_marker_set('Sec10_1')
  marker_sets["Sec10_1"]=s
s= marker_sets["Sec10_1"]
mark=s.place_marker((678.496, 527.187, 480.189), (0.3, 0.69, 0.29), 2)
if "Sec10_2" not in marker_sets:
  s=new_marker_set('Sec10_2')
  marker_sets["Sec10_2"]=s
s= marker_sets["Sec10_2"]
mark=s.place_marker((651.41, 521.78, 475.029), (0.3, 0.69, 0.29), 2)
if "Sec10_3" not in marker_sets:
  s=new_marker_set('Sec10_3')
  marker_sets["Sec10_3"]=s
s= marker_sets["Sec10_3"]
mark=s.place_marker((620.444, 532.325, 480.069), (0.3, 0.69, 0.29), 2)
if "Sec10_4" not in marker_sets:
  s=new_marker_set('Sec10_4')
  marker_sets["Sec10_4"]=s
s= marker_sets["Sec10_4"]
mark=s.place_marker((602.442, 525.79, 500.629), (0.3, 0.69, 0.29), 2)
if "Sec10_5" not in marker_sets:
  s=new_marker_set('Sec10_5')
  marker_sets["Sec10_5"]=s
s= marker_sets["Sec10_5"]
mark=s.place_marker((585.744, 547.637, 506.412), (0.3, 0.69, 0.29), 2)
if "Sec15_0" not in marker_sets:
  s=new_marker_set('Sec15_0')
  marker_sets["Sec15_0"]=s
s= marker_sets["Sec15_0"]
mark=s.place_marker((578.583, 544.515, 539.391), (0.97, 0.51, 0.75), 2)
if "Sec15_1" not in marker_sets:
  s=new_marker_set('Sec15_1')
  marker_sets["Sec15_1"]=s
s= marker_sets["Sec15_1"]
mark=s.place_marker((578.785, 516.543, 536.253), (0.97, 0.51, 0.75), 2)
if "Sec15_2" not in marker_sets:
  s=new_marker_set('Sec15_2')
  marker_sets["Sec15_2"]=s
s= marker_sets["Sec15_2"]
mark=s.place_marker((581.199, 488.592, 534.052), (0.97, 0.51, 0.75), 2)
if "Sec15_3" not in marker_sets:
  s=new_marker_set('Sec15_3')
  marker_sets["Sec15_3"]=s
s= marker_sets["Sec15_3"]
mark=s.place_marker((585.7, 461.261, 529.091), (0.97, 0.51, 0.75), 2)
if "Sec15_4" not in marker_sets:
  s=new_marker_set('Sec15_4')
  marker_sets["Sec15_4"]=s
s= marker_sets["Sec15_4"]
mark=s.place_marker((591.609, 437.186, 515.783), (0.97, 0.51, 0.75), 2)
if "Sec15_5" not in marker_sets:
  s=new_marker_set('Sec15_5')
  marker_sets["Sec15_5"]=s
s= marker_sets["Sec15_5"]
mark=s.place_marker((599.44, 417.333, 497.449), (0.97, 0.51, 0.75), 2)
if "Exo70_0" not in marker_sets:
  s=new_marker_set('Exo70_0')
  marker_sets["Exo70_0"]=s
s= marker_sets["Exo70_0"]
mark=s.place_marker((524.197, 571.386, 557.587), (0.89, 0.1, 0.1), 2)
if "Exo70_1" not in marker_sets:
  s=new_marker_set('Exo70_1')
  marker_sets["Exo70_1"]=s
s= marker_sets["Exo70_1"]
mark=s.place_marker((527.019, 581.021, 531.059), (0.89, 0.1, 0.1), 2)
if "Exo70_2" not in marker_sets:
  s=new_marker_set('Exo70_2')
  marker_sets["Exo70_2"]=s
s= marker_sets["Exo70_2"]
mark=s.place_marker((546.11, 578.036, 510.237), (0.89, 0.1, 0.1), 2)
if "Exo70_3" not in marker_sets:
  s=new_marker_set('Exo70_3')
  marker_sets["Exo70_3"]=s
s= marker_sets["Exo70_3"]
mark=s.place_marker((567.057, 574.687, 491.362), (0.89, 0.1, 0.1), 2)
if "Exo70_4" not in marker_sets:
  s=new_marker_set('Exo70_4')
  marker_sets["Exo70_4"]=s
s= marker_sets["Exo70_4"]
mark=s.place_marker((587.819, 570.963, 472.37), (0.89, 0.1, 0.1), 2)
if "Exo84_0" not in marker_sets:
  s=new_marker_set('Exo84_0')
  marker_sets["Exo84_0"]=s
s= marker_sets["Exo84_0"]
mark=s.place_marker((558.815, 589.983, 539.77), (1, 0.5, 0), 2)
if "Exo84_1" not in marker_sets:
  s=new_marker_set('Exo84_1')
  marker_sets["Exo84_1"]=s
s= marker_sets["Exo84_1"]
mark=s.place_marker((546.476, 553.253, 533.907), (1, 0.5, 0), 2)
if "Exo84_2" not in marker_sets:
  s=new_marker_set('Exo84_2')
  marker_sets["Exo84_2"]=s
s= marker_sets["Exo84_2"]
mark=s.place_marker((536.203, 516.249, 528.355), (1, 0.5, 0), 2)
if "Exo84_3" not in marker_sets:
  s=new_marker_set('Exo84_3')
  marker_sets["Exo84_3"]=s
s= marker_sets["Exo84_3"]
mark=s.place_marker((527.593, 485.285, 523.779), (1, 0.5, 0), 2)
