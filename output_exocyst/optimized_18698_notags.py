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
mark=s.place_marker((477.667, 552.751, 484.094), (0.21, 0.49, 0.72), 2)
if "Sec3_1" not in marker_sets:
  s=new_marker_set('Sec3_1')
  marker_sets["Sec3_1"]=s
s= marker_sets["Sec3_1"]
mark=s.place_marker((495.54, 528.239, 475.821), (0.21, 0.49, 0.72), 2)
if "Sec3_2" not in marker_sets:
  s=new_marker_set('Sec3_2')
  marker_sets["Sec3_2"]=s
s= marker_sets["Sec3_2"]
mark=s.place_marker((504.416, 501.495, 489.783), (0.21, 0.49, 0.72), 2)
if "Sec3_3" not in marker_sets:
  s=new_marker_set('Sec3_3')
  marker_sets["Sec3_3"]=s
s= marker_sets["Sec3_3"]
mark=s.place_marker((498.517, 475.864, 499.668), (0.21, 0.49, 0.72), 2)
if "Sec3_4" not in marker_sets:
  s=new_marker_set('Sec3_4')
  marker_sets["Sec3_4"]=s
s= marker_sets["Sec3_4"]
mark=s.place_marker((493.197, 451.678, 512.957), (0.21, 0.49, 0.72), 2)
if "Sec3_5" not in marker_sets:
  s=new_marker_set('Sec3_5')
  marker_sets["Sec3_5"]=s
s= marker_sets["Sec3_5"]
mark=s.place_marker((484.693, 425.331, 508.192), (0.21, 0.49, 0.72), 2)
if "Sec3_6" not in marker_sets:
  s=new_marker_set('Sec3_6')
  marker_sets["Sec3_6"]=s
s= marker_sets["Sec3_6"]
mark=s.place_marker((459.806, 412.356, 506.819), (0.21, 0.49, 0.72), 2)
if "Sec5_0" not in marker_sets:
  s=new_marker_set('Sec5_0')
  marker_sets["Sec5_0"]=s
s= marker_sets["Sec5_0"]
mark=s.place_marker((488.49, 532.093, 509.222), (0.6, 0.31, 0.64), 2)
if "Sec5_1" not in marker_sets:
  s=new_marker_set('Sec5_1')
  marker_sets["Sec5_1"]=s
s= marker_sets["Sec5_1"]
mark=s.place_marker((484.164, 557.898, 519.461), (0.6, 0.31, 0.64), 2)
if "Sec5_2" not in marker_sets:
  s=new_marker_set('Sec5_2')
  marker_sets["Sec5_2"]=s
s= marker_sets["Sec5_2"]
mark=s.place_marker((500.109, 580.849, 522.416), (0.6, 0.31, 0.64), 2)
if "Sec5_3" not in marker_sets:
  s=new_marker_set('Sec5_3')
  marker_sets["Sec5_3"]=s
s= marker_sets["Sec5_3"]
mark=s.place_marker((486.339, 579.187, 546.85), (0.6, 0.31, 0.64), 2)
if "Sec5_4" not in marker_sets:
  s=new_marker_set('Sec5_4')
  marker_sets["Sec5_4"]=s
s= marker_sets["Sec5_4"]
mark=s.place_marker((463.959, 562.201, 546.91), (0.6, 0.31, 0.64), 2)
if "Sec5_5" not in marker_sets:
  s=new_marker_set('Sec5_5')
  marker_sets["Sec5_5"]=s
s= marker_sets["Sec5_5"]
mark=s.place_marker((450.656, 546.194, 528.036), (0.6, 0.31, 0.64), 2)
if "Sec6_0" not in marker_sets:
  s=new_marker_set('Sec6_0')
  marker_sets["Sec6_0"]=s
s= marker_sets["Sec6_0"]
mark=s.place_marker((473.803, 501.875, 515.987), (1, 1, 0.2), 2)
if "Sec6_1" not in marker_sets:
  s=new_marker_set('Sec6_1')
  marker_sets["Sec6_1"]=s
s= marker_sets["Sec6_1"]
mark=s.place_marker((471.347, 504.601, 481.354), (1, 1, 0.2), 2)
if "Sec6_2" not in marker_sets:
  s=new_marker_set('Sec6_2')
  marker_sets["Sec6_2"]=s
s= marker_sets["Sec6_2"]
mark=s.place_marker((469.142, 507.356, 446.725), (1, 1, 0.2), 2)
if "Sec6_3" not in marker_sets:
  s=new_marker_set('Sec6_3')
  marker_sets["Sec6_3"]=s
s= marker_sets["Sec6_3"]
mark=s.place_marker((465.319, 511.232, 412.159), (1, 1, 0.2), 2)
if "Sec6_4" not in marker_sets:
  s=new_marker_set('Sec6_4')
  marker_sets["Sec6_4"]=s
s= marker_sets["Sec6_4"]
mark=s.place_marker((457.707, 514.934, 377.585), (1, 1, 0.2), 2)
if "Sec6_5" not in marker_sets:
  s=new_marker_set('Sec6_5')
  marker_sets["Sec6_5"]=s
s= marker_sets["Sec6_5"]
mark=s.place_marker((448.096, 524.338, 344.985), (1, 1, 0.2), 2)
if "Sec8_0" not in marker_sets:
  s=new_marker_set('Sec8_0')
  marker_sets["Sec8_0"]=s
s= marker_sets["Sec8_0"]
mark=s.place_marker((434.437, 486.771, 532.126), (0.65, 0.34, 0.16), 2)
if "Sec8_1" not in marker_sets:
  s=new_marker_set('Sec8_1')
  marker_sets["Sec8_1"]=s
s= marker_sets["Sec8_1"]
mark=s.place_marker((452.694, 474.76, 514.458), (0.65, 0.34, 0.16), 2)
if "Sec8_2" not in marker_sets:
  s=new_marker_set('Sec8_2')
  marker_sets["Sec8_2"]=s
s= marker_sets["Sec8_2"]
mark=s.place_marker((440.032, 450.445, 508.127), (0.65, 0.34, 0.16), 2)
if "Sec8_3" not in marker_sets:
  s=new_marker_set('Sec8_3')
  marker_sets["Sec8_3"]=s
s= marker_sets["Sec8_3"]
mark=s.place_marker((429.482, 426.104, 498.761), (0.65, 0.34, 0.16), 2)
if "Sec8_4" not in marker_sets:
  s=new_marker_set('Sec8_4')
  marker_sets["Sec8_4"]=s
s= marker_sets["Sec8_4"]
mark=s.place_marker((428.382, 399.682, 489.136), (0.65, 0.34, 0.16), 2)
if "Sec8_5" not in marker_sets:
  s=new_marker_set('Sec8_5')
  marker_sets["Sec8_5"]=s
s= marker_sets["Sec8_5"]
mark=s.place_marker((427.636, 373.829, 478.069), (0.65, 0.34, 0.16), 2)
if "Sec10_0" not in marker_sets:
  s=new_marker_set('Sec10_0')
  marker_sets["Sec10_0"]=s
s= marker_sets["Sec10_0"]
mark=s.place_marker((474.375, 456.473, 332.912), (0.3, 0.69, 0.29), 2)
if "Sec10_1" not in marker_sets:
  s=new_marker_set('Sec10_1')
  marker_sets["Sec10_1"]=s
s= marker_sets["Sec10_1"]
mark=s.place_marker((488.488, 480.586, 329.933), (0.3, 0.69, 0.29), 2)
if "Sec10_2" not in marker_sets:
  s=new_marker_set('Sec10_2')
  marker_sets["Sec10_2"]=s
s= marker_sets["Sec10_2"]
mark=s.place_marker((492.915, 485.497, 357.241), (0.3, 0.69, 0.29), 2)
if "Sec10_3" not in marker_sets:
  s=new_marker_set('Sec10_3')
  marker_sets["Sec10_3"]=s
s= marker_sets["Sec10_3"]
mark=s.place_marker((469.055, 481.363, 379.8), (0.3, 0.69, 0.29), 2)
if "Sec10_4" not in marker_sets:
  s=new_marker_set('Sec10_4')
  marker_sets["Sec10_4"]=s
s= marker_sets["Sec10_4"]
mark=s.place_marker((446.205, 486.386, 395.352), (0.3, 0.69, 0.29), 2)
if "Sec10_5" not in marker_sets:
  s=new_marker_set('Sec10_5')
  marker_sets["Sec10_5"]=s
s= marker_sets["Sec10_5"]
mark=s.place_marker((432.564, 507.61, 407.69), (0.3, 0.69, 0.29), 2)
if "Sec15_0" not in marker_sets:
  s=new_marker_set('Sec15_0')
  marker_sets["Sec15_0"]=s
s= marker_sets["Sec15_0"]
mark=s.place_marker((406.499, 516.556, 428.058), (0.97, 0.51, 0.75), 2)
if "Sec15_1" not in marker_sets:
  s=new_marker_set('Sec15_1')
  marker_sets["Sec15_1"]=s
s= marker_sets["Sec15_1"]
mark=s.place_marker((405.939, 489.035, 422.416), (0.97, 0.51, 0.75), 2)
if "Sec15_2" not in marker_sets:
  s=new_marker_set('Sec15_2')
  marker_sets["Sec15_2"]=s
s= marker_sets["Sec15_2"]
mark=s.place_marker((380.119, 485.021, 412.085), (0.97, 0.51, 0.75), 2)
if "Sec15_3" not in marker_sets:
  s=new_marker_set('Sec15_3')
  marker_sets["Sec15_3"]=s
s= marker_sets["Sec15_3"]
mark=s.place_marker((363.677, 483.235, 389.37), (0.97, 0.51, 0.75), 2)
if "Sec15_4" not in marker_sets:
  s=new_marker_set('Sec15_4')
  marker_sets["Sec15_4"]=s
s= marker_sets["Sec15_4"]
mark=s.place_marker((336.864, 482.685, 380.985), (0.97, 0.51, 0.75), 2)
if "Sec15_5" not in marker_sets:
  s=new_marker_set('Sec15_5')
  marker_sets["Sec15_5"]=s
s= marker_sets["Sec15_5"]
mark=s.place_marker((312.235, 484.273, 367.553), (0.97, 0.51, 0.75), 2)
if "Exo70_0" not in marker_sets:
  s=new_marker_set('Exo70_0')
  marker_sets["Exo70_0"]=s
s= marker_sets["Exo70_0"]
mark=s.place_marker((420.285, 523.509, 488.89), (0.89, 0.1, 0.1), 2)
if "Exo70_1" not in marker_sets:
  s=new_marker_set('Exo70_1')
  marker_sets["Exo70_1"]=s
s= marker_sets["Exo70_1"]
mark=s.place_marker((432.349, 511.527, 465.586), (0.89, 0.1, 0.1), 2)
if "Exo70_2" not in marker_sets:
  s=new_marker_set('Exo70_2')
  marker_sets["Exo70_2"]=s
s= marker_sets["Exo70_2"]
mark=s.place_marker((438.799, 520.027, 438.706), (0.89, 0.1, 0.1), 2)
if "Exo70_3" not in marker_sets:
  s=new_marker_set('Exo70_3')
  marker_sets["Exo70_3"]=s
s= marker_sets["Exo70_3"]
mark=s.place_marker((444.493, 537.947, 416.923), (0.89, 0.1, 0.1), 2)
if "Exo70_4" not in marker_sets:
  s=new_marker_set('Exo70_4')
  marker_sets["Exo70_4"]=s
s= marker_sets["Exo70_4"]
mark=s.place_marker((448.171, 543.824, 389.08), (0.89, 0.1, 0.1), 2)
if "Exo84_0" not in marker_sets:
  s=new_marker_set('Exo84_0')
  marker_sets["Exo84_0"]=s
s= marker_sets["Exo84_0"]
mark=s.place_marker((457.252, 534.728, 463.239), (1, 0.5, 0), 2)
if "Exo84_1" not in marker_sets:
  s=new_marker_set('Exo84_1')
  marker_sets["Exo84_1"]=s
s= marker_sets["Exo84_1"]
mark=s.place_marker((418.831, 540.618, 456.039), (1, 0.5, 0), 2)
if "Exo84_2" not in marker_sets:
  s=new_marker_set('Exo84_2')
  marker_sets["Exo84_2"]=s
s= marker_sets["Exo84_2"]
mark=s.place_marker((382.042, 539.522, 447.14), (1, 0.5, 0), 2)
if "Exo84_3" not in marker_sets:
  s=new_marker_set('Exo84_3')
  marker_sets["Exo84_3"]=s
s= marker_sets["Exo84_3"]
mark=s.place_marker((350.804, 538.595, 439.584), (1, 0.5, 0), 2)
