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
mark=s.place_marker((496.985, 545.482, 536.858), (0.89, 0.1, 0.1), 17.1475)
if "Cog2_1" not in marker_sets:
  s=new_marker_set('Cog2_1')
  marker_sets["Cog2_1"]=s
s= marker_sets["Cog2_1"]
mark=s.place_marker((553.385, 499.078, 499.528), (0.89, 0.1, 0.1), 17.1475)
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
mark=s.place_marker((477.719, 553.445, 553.515), (1, 1, 0.2), 17.1475)
if "Cog3_1" not in marker_sets:
  s=new_marker_set('Cog3_1')
  marker_sets["Cog3_1"]=s
s= marker_sets["Cog3_1"]
mark=s.place_marker((493.026, 546.951, 576.415), (1, 1, 0.2), 17.1475)
if "Cog3_2" not in marker_sets:
  s=new_marker_set('Cog3_2')
  marker_sets["Cog3_2"]=s
s= marker_sets["Cog3_2"]
mark=s.place_marker((501.462, 521.958, 586.634), (1, 1, 0.2), 17.1475)
if "Cog3_3" not in marker_sets:
  s=new_marker_set('Cog3_3')
  marker_sets["Cog3_3"]=s
s= marker_sets["Cog3_3"]
mark=s.place_marker((484.224, 499.937, 585.181), (1, 1, 0.2), 17.1475)
if "Cog3_4" not in marker_sets:
  s=new_marker_set('Cog3_4')
  marker_sets["Cog3_4"]=s
s= marker_sets["Cog3_4"]
mark=s.place_marker((467.846, 483.096, 600.741), (1, 1, 0.2), 17.1475)
if "Cog3_5" not in marker_sets:
  s=new_marker_set('Cog3_5')
  marker_sets["Cog3_5"]=s
s= marker_sets["Cog3_5"]
mark=s.place_marker((464.182, 496.957, 625.073), (1, 1, 0.2), 17.1475)
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
mark=s.place_marker((618.996, 405.172, 572.828), (0, 0, 0.8), 17.1475)
if "Cog4_2" not in marker_sets:
  s=new_marker_set('Cog4_2')
  marker_sets["Cog4_2"]=s
s= marker_sets["Cog4_2"]
mark=s.place_marker((599.328, 422.146, 561.433), (0, 0, 0.8), 17.1475)
if "Cog4_3" not in marker_sets:
  s=new_marker_set('Cog4_3')
  marker_sets["Cog4_3"]=s
s= marker_sets["Cog4_3"]
mark=s.place_marker((577.93, 441.087, 559.745), (0, 0, 0.8), 17.1475)
if "Cog4_4" not in marker_sets:
  s=new_marker_set('Cog4_4')
  marker_sets["Cog4_4"]=s
s= marker_sets["Cog4_4"]
mark=s.place_marker((564.287, 466.196, 559.547), (0, 0, 0.8), 17.1475)
if "Cog4_5" not in marker_sets:
  s=new_marker_set('Cog4_5')
  marker_sets["Cog4_5"]=s
s= marker_sets["Cog4_5"]
mark=s.place_marker((553.549, 492.856, 558.65), (0, 0, 0.8), 17.1475)
if "Cog4_6" not in marker_sets:
  s=new_marker_set('Cog4_6')
  marker_sets["Cog4_6"]=s
s= marker_sets["Cog4_6"]
mark=s.place_marker((540.126, 518.499, 556.814), (0, 0, 0.8), 17.1475)
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
mark=s.place_marker((549.324, 532.226, 514.053), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_2" not in marker_sets:
  s=new_marker_set('Cog5_2')
  marker_sets["Cog5_2"]=s
s= marker_sets["Cog5_2"]
mark=s.place_marker((536.397, 524.905, 489.469), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_3" not in marker_sets:
  s=new_marker_set('Cog5_3')
  marker_sets["Cog5_3"]=s
s= marker_sets["Cog5_3"]
mark=s.place_marker((524.122, 500.435, 479.433), (0.3, 0.3, 0.3), 17.1475)
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
mark=s.place_marker((471.844, 545.727, 521.865), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_1" not in marker_sets:
  s=new_marker_set('Cog6_1')
  marker_sets["Cog6_1"]=s
s= marker_sets["Cog6_1"]
mark=s.place_marker((470.628, 521.967, 506.824), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_2" not in marker_sets:
  s=new_marker_set('Cog6_2')
  marker_sets["Cog6_2"]=s
s= marker_sets["Cog6_2"]
mark=s.place_marker((460.788, 514.529, 532.373), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_3" not in marker_sets:
  s=new_marker_set('Cog6_3')
  marker_sets["Cog6_3"]=s
s= marker_sets["Cog6_3"]
mark=s.place_marker((458.787, 521.426, 559.462), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_4" not in marker_sets:
  s=new_marker_set('Cog6_4')
  marker_sets["Cog6_4"]=s
s= marker_sets["Cog6_4"]
mark=s.place_marker((464.52, 528.967, 585.895), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_5" not in marker_sets:
  s=new_marker_set('Cog6_5')
  marker_sets["Cog6_5"]=s
s= marker_sets["Cog6_5"]
mark=s.place_marker((476.53, 529.096, 611.115), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_6" not in marker_sets:
  s=new_marker_set('Cog6_6')
  marker_sets["Cog6_6"]=s
s= marker_sets["Cog6_6"]
mark=s.place_marker((486.039, 519.514, 635.529), (0.21, 0.49, 0.72), 17.1475)
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
mark=s.place_marker((533.473, 568.634, 534.116), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_1" not in marker_sets:
  s=new_marker_set('Cog7_1')
  marker_sets["Cog7_1"]=s
s= marker_sets["Cog7_1"]
mark=s.place_marker((506.308, 530.437, 500.582), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_2" not in marker_sets:
  s=new_marker_set('Cog7_2')
  marker_sets["Cog7_2"]=s
s= marker_sets["Cog7_2"]
mark=s.place_marker((484.284, 491.18, 464.322), (0.7, 0.7, 0.7), 17.1475)
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
mark=s.place_marker((466.499, 551.144, 431.279), (1, 0.5, 0), 17.1475)
if "Cog8_1" not in marker_sets:
  s=new_marker_set('Cog8_1')
  marker_sets["Cog8_1"]=s
s= marker_sets["Cog8_1"]
mark=s.place_marker((478.514, 531.665, 447.807), (1, 0.5, 0), 17.1475)
if "Cog8_2" not in marker_sets:
  s=new_marker_set('Cog8_2')
  marker_sets["Cog8_2"]=s
s= marker_sets["Cog8_2"]
mark=s.place_marker((484.131, 528.749, 475.063), (1, 0.5, 0), 17.1475)
if "Cog8_3" not in marker_sets:
  s=new_marker_set('Cog8_3')
  marker_sets["Cog8_3"]=s
s= marker_sets["Cog8_3"]
mark=s.place_marker((510.894, 530.194, 465.382), (1, 0.5, 0), 17.1475)
if "Cog8_4" not in marker_sets:
  s=new_marker_set('Cog8_4')
  marker_sets["Cog8_4"]=s
s= marker_sets["Cog8_4"]
mark=s.place_marker((537.567, 527.213, 455.838), (1, 0.5, 0), 17.1475)
if "Cog8_5" not in marker_sets:
  s=new_marker_set('Cog8_5')
  marker_sets["Cog8_5"]=s
s= marker_sets["Cog8_5"]
mark=s.place_marker((564.437, 536.26, 459.546), (1, 0.5, 0), 17.1475)
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
