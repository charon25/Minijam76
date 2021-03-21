import co
import _atoms_ as atoms
import _stable_atoms_ as stable_atoms
import _neutron_atoms_ as neutron_atoms
import _decaying_atoms_ as decaying_atoms
import _neutrons_ as neutrons

class Levels():
    def __init__(self):
        self.index = 0
        self.atoms = []
        self.line1 = ""
        self.line2 = ""
        
    def restart(self):
        self.index = 0
        
    def get_next_level(self):
        self.index += 1
        if self.index == 1:
            self.__level1()
        elif self.index == 2:
            self.__level2()
        elif self.index == 3:
            self.__level3()
            
        return (self.atoms, self.line1, self.line2)
    
    def __level1(self):
        self.atoms = []
        self.line1 = "Click, drag and release left click to launch a neutron (blue)."
        self.line2 = "Propel it into a fissile atom (pinkish circles) to generate more neutrons !"
        self.atoms.append(neutron_atoms.U235((co.WIDTH - co.U235_SIZE) / 2, (co.HEIGHT - co.U235_SIZE) / 2, 2))
        
        
    def __level2(self):
        pass
        
    def __level3(self):
        pass
    
    def create_random_level(self):
        
        return ([], "", "")