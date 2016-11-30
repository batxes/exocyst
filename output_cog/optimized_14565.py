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
mark=s.place_marker((443.454, 580.329, 564.589), (0.89, 0.1, 0.1), 18.4716)
if "Cog2_0" not in marker_sets:
  s=new_marker_set('Cog2_0')
  marker_sets["Cog2_0"]=s
s= marker_sets["Cog2_0"]
mark=s.place_marker((496.384, 553.915, 533.501), (0.89, 0.1, 0.1), 17.1475)
if "Cog2_1" not in marker_sets:
  s=new_marker_set('Cog2_1')
  marker_sets["Cog2_1"]=s
s= marker_sets["Cog2_1"]
mark=s.place_marker((553.367, 507.83, 494.099), (0.89, 0.1, 0.1), 17.1475)
if "Cog2_GFPC" not in marker_sets:
  s=new_marker_set('Cog2_GFPC')
  marker_sets["Cog2_GFPC"]=s
s= marker_sets["Cog2_GFPC"]
mark=s.place_marker((417.361, 478.403, 475.912), (0.89, 0.1, 0.1), 18.4716)
if "Cog2_Anch" not in marker_sets:
  s=new_marker_set('Cog2_Anch')
  marker_sets["Cog2_Anch"]=s
s= marker_sets["Cog2_Anch"]
mark=s.place_marker((716.134, 422.834, 428.888), (0.89, 0.1, 0.1), 18.4716)
if "Cog3_GFPN" not in marker_sets:
  s=new_marker_set('Cog3_GFPN')
  marker_sets["Cog3_GFPN"]=s
s= marker_sets["Cog3_GFPN"]
mark=s.place_marker((478.895, 553.034, 552.336), (1, 1, 0), 18.4716)
if "Cog3_0" not in marker_sets:
  s=new_marker_set('Cog3_0')
  marker_sets["Cog3_0"]=s
s= marker_sets["Cog3_0"]
mark=s.place_marker((477.951, 552.997, 553.401), (1, 1, 0.2), 17.1475)
if "Cog3_1" not in marker_sets:
  s=new_marker_set('Cog3_1')
  marker_sets["Cog3_1"]=s
s= marker_sets["Cog3_1"]
mark=s.place_marker((450.462, 545.466, 554.309), (1, 1, 0.2), 17.1475)
if "Cog3_2" not in marker_sets:
  s=new_marker_set('Cog3_2')
  marker_sets["Cog3_2"]=s
s= marker_sets["Cog3_2"]
mark=s.place_marker((442.248, 518.781, 558.088), (1, 1, 0.2), 17.1475)
if "Cog3_3" not in marker_sets:
  s=new_marker_set('Cog3_3')
  marker_sets["Cog3_3"]=s
s= marker_sets["Cog3_3"]
mark=s.place_marker((460.981, 509.627, 576.041), (1, 1, 0.2), 17.1475)
if "Cog3_4" not in marker_sets:
  s=new_marker_set('Cog3_4')
  marker_sets["Cog3_4"]=s
s= marker_sets["Cog3_4"]
mark=s.place_marker((471.191, 496.787, 597.994), (1, 1, 0.2), 17.1475)
if "Cog3_5" not in marker_sets:
  s=new_marker_set('Cog3_5')
  marker_sets["Cog3_5"]=s
s= marker_sets["Cog3_5"]
mark=s.place_marker((463.682, 497.2, 624.785), (1, 1, 0.2), 17.1475)
if "Cog3_GFPC" not in marker_sets:
  s=new_marker_set('Cog3_GFPC')
  marker_sets["Cog3_GFPC"]=s
s= marker_sets["Cog3_GFPC"]
mark=s.place_marker((469.155, 579.433, 556.905), (1, 1, 0.4), 18.4716)
if "Cog3_Anch" not in marker_sets:
  s=new_marker_set('Cog3_Anch')
  marker_sets["Cog3_Anch"]=s
s= marker_sets["Cog3_Anch"]
mark=s.place_marker((463.057, 418.793, 696.936), (1, 1, 0.4), 18.4716)
if "Cog4_GFPN" not in marker_sets:
  s=new_marker_set('Cog4_GFPN')
  marker_sets["Cog4_GFPN"]=s
s= marker_sets["Cog4_GFPN"]
mark=s.place_marker((632.967, 389.679, 591.412), (0, 0, 0.8), 18.4716)
if "Cog4_0" not in marker_sets:
  s=new_marker_set('Cog4_0')
  marker_sets["Cog4_0"]=s
s= marker_sets["Cog4_0"]
mark=s.place_marker((632.967, 389.679, 591.412), (0, 0, 0.8), 17.1475)
if "Cog4_1" not in marker_sets:
  s=new_marker_set('Cog4_1')
  marker_sets["Cog4_1"]=s
s= marker_sets["Cog4_1"]
mark=s.place_marker((623.341, 416.627, 591.88), (0, 0, 0.8), 17.1475)
if "Cog4_2" not in marker_sets:
  s=new_marker_set('Cog4_2')
  marker_sets["Cog4_2"]=s
s= marker_sets["Cog4_2"]
mark=s.place_marker((607.522, 440.09, 594.055), (0, 0, 0.8), 17.1475)
if "Cog4_3" not in marker_sets:
  s=new_marker_set('Cog4_3')
  marker_sets["Cog4_3"]=s
s= marker_sets["Cog4_3"]
mark=s.place_marker((590.216, 462.211, 596.832), (0, 0, 0.8), 17.1475)
if "Cog4_4" not in marker_sets:
  s=new_marker_set('Cog4_4')
  marker_sets["Cog4_4"]=s
s= marker_sets["Cog4_4"]
mark=s.place_marker((574.611, 485.71, 594.497), (0, 0, 0.8), 17.1475)
if "Cog4_5" not in marker_sets:
  s=new_marker_set('Cog4_5')
  marker_sets["Cog4_5"]=s
s= marker_sets["Cog4_5"]
mark=s.place_marker((557.633, 504.876, 581.902), (0, 0, 0.8), 17.1475)
if "Cog4_6" not in marker_sets:
  s=new_marker_set('Cog4_6')
  marker_sets["Cog4_6"]=s
s= marker_sets["Cog4_6"]
mark=s.place_marker((540.536, 521.956, 566.545), (0, 0, 0.8), 17.1475)
if "Cog4_GFPC" not in marker_sets:
  s=new_marker_set('Cog4_GFPC')
  marker_sets["Cog4_GFPC"]=s
s= marker_sets["Cog4_GFPC"]
mark=s.place_marker((544.042, 285.18, 666.243), (0, 0, 0.8), 18.4716)
if "Cog4_Anch" not in marker_sets:
  s=new_marker_set('Cog4_Anch')
  marker_sets["Cog4_Anch"]=s
s= marker_sets["Cog4_Anch"]
mark=s.place_marker((520.092, 758.118, 456.674), (0, 0, 0.8), 18.4716)
if "Cog5_GFPN" not in marker_sets:
  s=new_marker_set('Cog5_GFPN')
  marker_sets["Cog5_GFPN"]=s
s= marker_sets["Cog5_GFPN"]
mark=s.place_marker((568.047, 527.972, 534.668), (0.3, 0.3, 0.3), 18.4716)
if "Cog5_0" not in marker_sets:
  s=new_marker_set('Cog5_0')
  marker_sets["Cog5_0"]=s
s= marker_sets["Cog5_0"]
mark=s.place_marker((568.047, 527.972, 534.668), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_1" not in marker_sets:
  s=new_marker_set('Cog5_1')
  marker_sets["Cog5_1"]=s
s= marker_sets["Cog5_1"]
mark=s.place_marker((552.32, 504.503, 527.922), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_2" not in marker_sets:
  s=new_marker_set('Cog5_2')
  marker_sets["Cog5_2"]=s
s= marker_sets["Cog5_2"]
mark=s.place_marker((533.431, 489.357, 511.641), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_3" not in marker_sets:
  s=new_marker_set('Cog5_3')
  marker_sets["Cog5_3"]=s
s= marker_sets["Cog5_3"]
mark=s.place_marker((523.505, 494.635, 484.599), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_GFPC" not in marker_sets:
  s=new_marker_set('Cog5_GFPC')
  marker_sets["Cog5_GFPC"]=s
s= marker_sets["Cog5_GFPC"]
mark=s.place_marker((420.525, 559.27, 515.178), (0.3, 0.3, 0.3), 18.4716)
if "Cog5_Anch" not in marker_sets:
  s=new_marker_set('Cog5_Anch')
  marker_sets["Cog5_Anch"]=s
s= marker_sets["Cog5_Anch"]
mark=s.place_marker((624.293, 434.594, 442.447), (0.3, 0.3, 0.3), 18.4716)
if "Cog6_GFPN" not in marker_sets:
  s=new_marker_set('Cog6_GFPN')
  marker_sets["Cog6_GFPN"]=s
s= marker_sets["Cog6_GFPN"]
mark=s.place_marker((471.882, 545.731, 521.895), (0.21, 0.49, 0.72), 18.4716)
if "Cog6_0" not in marker_sets:
  s=new_marker_set('Cog6_0')
  marker_sets["Cog6_0"]=s
s= marker_sets["Cog6_0"]
mark=s.place_marker((471.538, 545.681, 521.662), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_1" not in marker_sets:
  s=new_marker_set('Cog6_1')
  marker_sets["Cog6_1"]=s
s= marker_sets["Cog6_1"]
mark=s.place_marker((481.489, 522.079, 534.189), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_2" not in marker_sets:
  s=new_marker_set('Cog6_2')
  marker_sets["Cog6_2"]=s
s= marker_sets["Cog6_2"]
mark=s.place_marker((497.829, 525.225, 556.98), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_3" not in marker_sets:
  s=new_marker_set('Cog6_3')
  marker_sets["Cog6_3"]=s
s= marker_sets["Cog6_3"]
mark=s.place_marker((500.285, 513.326, 582.255), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_4" not in marker_sets:
  s=new_marker_set('Cog6_4')
  marker_sets["Cog6_4"]=s
s= marker_sets["Cog6_4"]
mark=s.place_marker((504.554, 508.552, 609.437), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_5" not in marker_sets:
  s=new_marker_set('Cog6_5')
  marker_sets["Cog6_5"]=s
s= marker_sets["Cog6_5"]
mark=s.place_marker((506.565, 501.51, 636.413), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_6" not in marker_sets:
  s=new_marker_set('Cog6_6')
  marker_sets["Cog6_6"]=s
s= marker_sets["Cog6_6"]
mark=s.place_marker((485.353, 519.901, 635.376), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_GFPC" not in marker_sets:
  s=new_marker_set('Cog6_GFPC')
  marker_sets["Cog6_GFPC"]=s
s= marker_sets["Cog6_GFPC"]
mark=s.place_marker((537.982, 573.068, 592.989), (0.21, 0.49, 0.72), 18.4716)
if "Cog6_Anch" not in marker_sets:
  s=new_marker_set('Cog6_Anch')
  marker_sets["Cog6_Anch"]=s
s= marker_sets["Cog6_Anch"]
mark=s.place_marker((430.966, 463.874, 674.202), (0.21, 0.49, 0.72), 18.4716)
if "Cog7_GFPN" not in marker_sets:
  s=new_marker_set('Cog7_GFPN')
  marker_sets["Cog7_GFPN"]=s
s= marker_sets["Cog7_GFPN"]
mark=s.place_marker((545.474, 585.993, 549.296), (0.7, 0.7, 0.7), 18.4716)
if "Cog7_0" not in marker_sets:
  s=new_marker_set('Cog7_0')
  marker_sets["Cog7_0"]=s
s= marker_sets["Cog7_0"]
mark=s.place_marker((535.085, 570.729, 533.084), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_1" not in marker_sets:
  s=new_marker_set('Cog7_1')
  marker_sets["Cog7_1"]=s
s= marker_sets["Cog7_1"]
mark=s.place_marker((511.262, 530.966, 498.127), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_2" not in marker_sets:
  s=new_marker_set('Cog7_2')
  marker_sets["Cog7_2"]=s
s= marker_sets["Cog7_2"]
mark=s.place_marker((486.284, 491.904, 462.981), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_GFPC" not in marker_sets:
  s=new_marker_set('Cog7_GFPC')
  marker_sets["Cog7_GFPC"]=s
s= marker_sets["Cog7_GFPC"]
mark=s.place_marker((430.761, 550.098, 452.354), (0.7, 0.7, 0.7), 18.4716)
if "Cog7_Anch" not in marker_sets:
  s=new_marker_set('Cog7_Anch')
  marker_sets["Cog7_Anch"]=s
s= marker_sets["Cog7_Anch"]
mark=s.place_marker((492.823, 394.237, 425.308), (0.7, 0.7, 0.7), 18.4716)
if "Cog8_0" not in marker_sets:
  s=new_marker_set('Cog8_0')
  marker_sets["Cog8_0"]=s
s= marker_sets["Cog8_0"]
mark=s.place_marker((514.535, 550.055, 598.199), (1, 0.5, 0), 17.1475)
if "Cog8_1" not in marker_sets:
  s=new_marker_set('Cog8_1')
  marker_sets["Cog8_1"]=s
s= marker_sets["Cog8_1"]
mark=s.place_marker((519.845, 548.705, 570.506), (1, 0.5, 0), 17.1475)
if "Cog8_2" not in marker_sets:
  s=new_marker_set('Cog8_2')
  marker_sets["Cog8_2"]=s
s= marker_sets["Cog8_2"]
mark=s.place_marker((526.113, 540.929, 543.551), (1, 0.5, 0), 17.1475)
if "Cog8_3" not in marker_sets:
  s=new_marker_set('Cog8_3')
  marker_sets["Cog8_3"]=s
s= marker_sets["Cog8_3"]
mark=s.place_marker((540.329, 540.884, 518.044), (1, 0.5, 0), 17.1475)
if "Cog8_4" not in marker_sets:
  s=new_marker_set('Cog8_4')
  marker_sets["Cog8_4"]=s
s= marker_sets["Cog8_4"]
mark=s.place_marker((553.183, 541.412, 491.27), (1, 0.5, 0), 17.1475)
if "Cog8_5" not in marker_sets:
  s=new_marker_set('Cog8_5')
  marker_sets["Cog8_5"]=s
s= marker_sets["Cog8_5"]
mark=s.place_marker((564.786, 536.467, 463.873), (1, 0.5, 0), 17.1475)
if "Cog8_GFPC" not in marker_sets:
  s=new_marker_set('Cog8_GFPC')
  marker_sets["Cog8_GFPC"]=s
s= marker_sets["Cog8_GFPC"]
mark=s.place_marker((514.271, 563.061, 517.007), (1, 0.6, 0.1), 18.4716)
if "Cog8_Anch" not in marker_sets:
  s=new_marker_set('Cog8_Anch')
  marker_sets["Cog8_Anch"]=s
s= marker_sets["Cog8_Anch"]
mark=s.place_marker((617.996, 511.327, 402.883), (1, 0.6, 0.1), 18.4716)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
