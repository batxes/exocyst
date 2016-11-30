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
mark=s.place_marker((494.074, 587.143, 473.944), (0.89, 0.1, 0.1), 18.4716)
if "Cog2_0" not in marker_sets:
  s=new_marker_set('Cog2_0')
  marker_sets["Cog2_0"]=s
s= marker_sets["Cog2_0"]
mark=s.place_marker((518.107, 642.699, 440.876), (0.89, 0.1, 0.1), 17.1475)
if "Cog2_1" not in marker_sets:
  s=new_marker_set('Cog2_1')
  marker_sets["Cog2_1"]=s
s= marker_sets["Cog2_1"]
mark=s.place_marker((552.647, 708.003, 408.406), (0.89, 0.1, 0.1), 17.1475)
if "Cog2_GFPC" not in marker_sets:
  s=new_marker_set('Cog2_GFPC')
  marker_sets["Cog2_GFPC"]=s
s= marker_sets["Cog2_GFPC"]
mark=s.place_marker((601.61, 655.031, 526.484), (0.89, 0.1, 0.1), 18.4716)
if "Cog2_Anch" not in marker_sets:
  s=new_marker_set('Cog2_Anch')
  marker_sets["Cog2_Anch"]=s
s= marker_sets["Cog2_Anch"]
mark=s.place_marker((614.495, 849.024, 288.228), (0.89, 0.1, 0.1), 18.4716)
if "Cog3_GFPN" not in marker_sets:
  s=new_marker_set('Cog3_GFPN')
  marker_sets["Cog3_GFPN"]=s
s= marker_sets["Cog3_GFPN"]
mark=s.place_marker((505.64, 627.483, 454.189), (1, 1, 0), 18.4716)
if "Cog3_0" not in marker_sets:
  s=new_marker_set('Cog3_0')
  marker_sets["Cog3_0"]=s
s= marker_sets["Cog3_0"]
mark=s.place_marker((504.38, 626.215, 455.311), (1, 1, 0.2), 17.1475)
if "Cog3_1" not in marker_sets:
  s=new_marker_set('Cog3_1')
  marker_sets["Cog3_1"]=s
s= marker_sets["Cog3_1"]
mark=s.place_marker((477.002, 628.738, 448.43), (1, 1, 0.2), 17.1475)
if "Cog3_2" not in marker_sets:
  s=new_marker_set('Cog3_2')
  marker_sets["Cog3_2"]=s
s= marker_sets["Cog3_2"]
mark=s.place_marker((451.117, 634.472, 457.967), (1, 1, 0.2), 17.1475)
if "Cog3_3" not in marker_sets:
  s=new_marker_set('Cog3_3')
  marker_sets["Cog3_3"]=s
s= marker_sets["Cog3_3"]
mark=s.place_marker((452.056, 628.377, 485.411), (1, 1, 0.2), 17.1475)
if "Cog3_4" not in marker_sets:
  s=new_marker_set('Cog3_4')
  marker_sets["Cog3_4"]=s
s= marker_sets["Cog3_4"]
mark=s.place_marker((457.917, 648.541, 503.857), (1, 1, 0.2), 17.1475)
if "Cog3_5" not in marker_sets:
  s=new_marker_set('Cog3_5')
  marker_sets["Cog3_5"]=s
s= marker_sets["Cog3_5"]
mark=s.place_marker((446.033, 673.507, 509.417), (1, 1, 0.2), 17.1475)
if "Cog3_GFPC" not in marker_sets:
  s=new_marker_set('Cog3_GFPC')
  marker_sets["Cog3_GFPC"]=s
s= marker_sets["Cog3_GFPC"]
mark=s.place_marker((498.067, 600.2, 450.838), (1, 1, 0.4), 18.4716)
if "Cog3_Anch" not in marker_sets:
  s=new_marker_set('Cog3_Anch')
  marker_sets["Cog3_Anch"]=s
s= marker_sets["Cog3_Anch"]
mark=s.place_marker((389.767, 746.45, 561.895), (1, 1, 0.4), 18.4716)
if "Cog4_GFPN" not in marker_sets:
  s=new_marker_set('Cog4_GFPN')
  marker_sets["Cog4_GFPN"]=s
s= marker_sets["Cog4_GFPN"]
mark=s.place_marker((473.496, 848.516, 408.846), (0, 0, 0.8), 18.4716)
if "Cog4_0" not in marker_sets:
  s=new_marker_set('Cog4_0')
  marker_sets["Cog4_0"]=s
s= marker_sets["Cog4_0"]
mark=s.place_marker((473.496, 848.516, 408.846), (0, 0, 0.8), 17.1475)
if "Cog4_1" not in marker_sets:
  s=new_marker_set('Cog4_1')
  marker_sets["Cog4_1"]=s
s= marker_sets["Cog4_1"]
mark=s.place_marker((477.985, 821.31, 419.47), (0, 0, 0.8), 17.1475)
if "Cog4_2" not in marker_sets:
  s=new_marker_set('Cog4_2')
  marker_sets["Cog4_2"]=s
s= marker_sets["Cog4_2"]
mark=s.place_marker((481.934, 793.957, 429.109), (0, 0, 0.8), 17.1475)
if "Cog4_3" not in marker_sets:
  s=new_marker_set('Cog4_3')
  marker_sets["Cog4_3"]=s
s= marker_sets["Cog4_3"]
mark=s.place_marker((486.5, 765.978, 436.068), (0, 0, 0.8), 17.1475)
if "Cog4_4" not in marker_sets:
  s=new_marker_set('Cog4_4')
  marker_sets["Cog4_4"]=s
s= marker_sets["Cog4_4"]
mark=s.place_marker((490.867, 737.513, 434.2), (0, 0, 0.8), 17.1475)
if "Cog4_5" not in marker_sets:
  s=new_marker_set('Cog4_5')
  marker_sets["Cog4_5"]=s
s= marker_sets["Cog4_5"]
mark=s.place_marker((495.26, 710.698, 425.566), (0, 0, 0.8), 17.1475)
if "Cog4_6" not in marker_sets:
  s=new_marker_set('Cog4_6')
  marker_sets["Cog4_6"]=s
s= marker_sets["Cog4_6"]
mark=s.place_marker((489.497, 683.113, 421.527), (0, 0, 0.8), 17.1475)
if "Cog4_GFPC" not in marker_sets:
  s=new_marker_set('Cog4_GFPC')
  marker_sets["Cog4_GFPC"]=s
s= marker_sets["Cog4_GFPC"]
mark=s.place_marker((430.982, 899.803, 550.233), (0, 0, 0.8), 18.4716)
if "Cog4_Anch" not in marker_sets:
  s=new_marker_set('Cog4_Anch')
  marker_sets["Cog4_Anch"]=s
s= marker_sets["Cog4_Anch"]
mark=s.place_marker((558.133, 463.968, 301.166), (0, 0, 0.8), 18.4716)
if "Cog5_GFPN" not in marker_sets:
  s=new_marker_set('Cog5_GFPN')
  marker_sets["Cog5_GFPN"]=s
s= marker_sets["Cog5_GFPN"]
mark=s.place_marker((514.475, 692.397, 386.393), (0.3, 0.3, 0.3), 18.4716)
if "Cog5_0" not in marker_sets:
  s=new_marker_set('Cog5_0')
  marker_sets["Cog5_0"]=s
s= marker_sets["Cog5_0"]
mark=s.place_marker((514.475, 692.397, 386.393), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_1" not in marker_sets:
  s=new_marker_set('Cog5_1')
  marker_sets["Cog5_1"]=s
s= marker_sets["Cog5_1"]
mark=s.place_marker((542.944, 691.941, 380.284), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_2" not in marker_sets:
  s=new_marker_set('Cog5_2')
  marker_sets["Cog5_2"]=s
s= marker_sets["Cog5_2"]
mark=s.place_marker((569.44, 687.705, 392.109), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_3" not in marker_sets:
  s=new_marker_set('Cog5_3')
  marker_sets["Cog5_3"]=s
s= marker_sets["Cog5_3"]
mark=s.place_marker((577.793, 688.631, 420.406), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_GFPC" not in marker_sets:
  s=new_marker_set('Cog5_GFPC')
  marker_sets["Cog5_GFPC"]=s
s= marker_sets["Cog5_GFPC"]
mark=s.place_marker((549.099, 589.966, 493.31), (0.3, 0.3, 0.3), 18.4716)
if "Cog5_Anch" not in marker_sets:
  s=new_marker_set('Cog5_Anch')
  marker_sets["Cog5_Anch"]=s
s= marker_sets["Cog5_Anch"]
mark=s.place_marker((612.322, 793.903, 363.818), (0.3, 0.3, 0.3), 18.4716)
if "Cog6_GFPN" not in marker_sets:
  s=new_marker_set('Cog6_GFPN')
  marker_sets["Cog6_GFPN"]=s
s= marker_sets["Cog6_GFPN"]
mark=s.place_marker((537.563, 627.898, 457.337), (0.21, 0.49, 0.72), 18.4716)
if "Cog6_0" not in marker_sets:
  s=new_marker_set('Cog6_0')
  marker_sets["Cog6_0"]=s
s= marker_sets["Cog6_0"]
mark=s.place_marker((537.578, 627.893, 457.338), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_1" not in marker_sets:
  s=new_marker_set('Cog6_1')
  marker_sets["Cog6_1"]=s
s= marker_sets["Cog6_1"]
mark=s.place_marker((525.981, 646.826, 474.204), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_2" not in marker_sets:
  s=new_marker_set('Cog6_2')
  marker_sets["Cog6_2"]=s
s= marker_sets["Cog6_2"]
mark=s.place_marker((509.752, 667.202, 484.72), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_3" not in marker_sets:
  s=new_marker_set('Cog6_3')
  marker_sets["Cog6_3"]=s
s= marker_sets["Cog6_3"]
mark=s.place_marker((490.989, 687.892, 487.449), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_4" not in marker_sets:
  s=new_marker_set('Cog6_4')
  marker_sets["Cog6_4"]=s
s= marker_sets["Cog6_4"]
mark=s.place_marker((468.115, 686.975, 471.389), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_5" not in marker_sets:
  s=new_marker_set('Cog6_5')
  marker_sets["Cog6_5"]=s
s= marker_sets["Cog6_5"]
mark=s.place_marker((440.321, 692.161, 469.26), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_6" not in marker_sets:
  s=new_marker_set('Cog6_6')
  marker_sets["Cog6_6"]=s
s= marker_sets["Cog6_6"]
mark=s.place_marker((430.287, 668.297, 480.813), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_GFPC" not in marker_sets:
  s=new_marker_set('Cog6_GFPC')
  marker_sets["Cog6_GFPC"]=s
s= marker_sets["Cog6_GFPC"]
mark=s.place_marker((454.193, 642.986, 402.632), (0.21, 0.49, 0.72), 18.4716)
if "Cog6_Anch" not in marker_sets:
  s=new_marker_set('Cog6_Anch')
  marker_sets["Cog6_Anch"]=s
s= marker_sets["Cog6_Anch"]
mark=s.place_marker((408.801, 689.743, 563.018), (0.21, 0.49, 0.72), 18.4716)
if "Cog7_GFPN" not in marker_sets:
  s=new_marker_set('Cog7_GFPN')
  marker_sets["Cog7_GFPN"]=s
s= marker_sets["Cog7_GFPN"]
mark=s.place_marker((493.53, 632.211, 380.981), (0.7, 0.7, 0.7), 18.4716)
if "Cog7_0" not in marker_sets:
  s=new_marker_set('Cog7_0')
  marker_sets["Cog7_0"]=s
s= marker_sets["Cog7_0"]
mark=s.place_marker((513.783, 640.117, 395.786), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_1" not in marker_sets:
  s=new_marker_set('Cog7_1')
  marker_sets["Cog7_1"]=s
s= marker_sets["Cog7_1"]
mark=s.place_marker((557.446, 659.279, 428.466), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_2" not in marker_sets:
  s=new_marker_set('Cog7_2')
  marker_sets["Cog7_2"]=s
s= marker_sets["Cog7_2"]
mark=s.place_marker((601.903, 677.318, 460.677), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_GFPC" not in marker_sets:
  s=new_marker_set('Cog7_GFPC')
  marker_sets["Cog7_GFPC"]=s
s= marker_sets["Cog7_GFPC"]
mark=s.place_marker((610.469, 598.13, 475.902), (0.7, 0.7, 0.7), 18.4716)
if "Cog7_Anch" not in marker_sets:
  s=new_marker_set('Cog7_Anch')
  marker_sets["Cog7_Anch"]=s
s= marker_sets["Cog7_Anch"]
mark=s.place_marker((654.598, 761.449, 491.752), (0.7, 0.7, 0.7), 18.4716)
if "Cog8_0" not in marker_sets:
  s=new_marker_set('Cog8_0')
  marker_sets["Cog8_0"]=s
s= marker_sets["Cog8_0"]
mark=s.place_marker((548.142, 569.792, 429.506), (1, 0.5, 0), 17.1475)
if "Cog8_1" not in marker_sets:
  s=new_marker_set('Cog8_1')
  marker_sets["Cog8_1"]=s
s= marker_sets["Cog8_1"]
mark=s.place_marker((550.134, 597.801, 427.903), (1, 0.5, 0), 17.1475)
if "Cog8_2" not in marker_sets:
  s=new_marker_set('Cog8_2')
  marker_sets["Cog8_2"]=s
s= marker_sets["Cog8_2"]
mark=s.place_marker((553.625, 625.503, 426.142), (1, 0.5, 0), 17.1475)
if "Cog8_3" not in marker_sets:
  s=new_marker_set('Cog8_3')
  marker_sets["Cog8_3"]=s
s= marker_sets["Cog8_3"]
mark=s.place_marker((566.761, 637.558, 403.886), (1, 0.5, 0), 17.1475)
if "Cog8_4" not in marker_sets:
  s=new_marker_set('Cog8_4')
  marker_sets["Cog8_4"]=s
s= marker_sets["Cog8_4"]
mark=s.place_marker((579.889, 656.181, 386.756), (1, 0.5, 0), 17.1475)
if "Cog8_5" not in marker_sets:
  s=new_marker_set('Cog8_5')
  marker_sets["Cog8_5"]=s
s= marker_sets["Cog8_5"]
mark=s.place_marker((587.195, 675.353, 366.929), (1, 0.5, 0), 17.1475)
if "Cog8_GFPC" not in marker_sets:
  s=new_marker_set('Cog8_GFPC')
  marker_sets["Cog8_GFPC"]=s
s= marker_sets["Cog8_GFPC"]
mark=s.place_marker((533.353, 633.828, 411.86), (1, 0.6, 0.1), 18.4716)
if "Cog8_Anch" not in marker_sets:
  s=new_marker_set('Cog8_Anch')
  marker_sets["Cog8_Anch"]=s
s= marker_sets["Cog8_Anch"]
mark=s.place_marker((638.717, 721.544, 324.315), (1, 0.6, 0.1), 18.4716)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])
