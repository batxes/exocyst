#-- File: nup84_complex_in_bead_representation.py --#
import IMP
import IMP.restrainer
import IMP.atom
IMP.set_log_level(IMP.VERBOSE)
# Create restrainer object
restrainer = IMP.restrainer.Main()
# Add representation, restraint, optimization and display to restrainer

rep = restrainer.add_representation('input/repr_exocyst_rdm.xml')
rsr = restrainer.add_restraint('input/restraint_exocyst.xml')
opt = restrainer.add_optimization('input/optimization.xml')
disp = restrainer.add_display('input/displ_exocyst.xml')

###=======================================================================###
# At this point all data from XML files have been placed into the model.
# Now it is possible to perform various operations on the IMP model.
###=======================================================================###
# Save the initial state in Chimera format
restrainer.log.write('output/initial.py')
# Perform optimization
restrainer.optimize()

# Save the optimized state in Chimera format
restrainer.log.write('output/optimized.py')
score = restrainer.get_model().evaluate(False)
print "Final score: "+str(score)
