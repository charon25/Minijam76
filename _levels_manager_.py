import co
import util
import math, random
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
        self.required_neutrons = 0
        
        
    def reset_all_atoms(self):
        for atom in self.atoms:
            atom.reset()
        
    def restart(self):
        self.index = 0
        
    def get_current_level(self):
        return self.__load_level_index()
        
    def get_next_level(self):
        self.index = min(self.index + 1, co.LEVELS_COUNT)
        return self.__load_level_index()
    
    def __load_level_index(self):
        if self.index == 1:
            self.__level1()
        elif self.index == 2:
            self.__level2()
        elif self.index == 3:
            self.__level3()
        elif self.index == 4:
            self.__level4()
        elif self.index == 5:
            self.__level5()
        elif self.index == 6:
            self.__level6()
        elif self.index == 7:
            self.__level7()
        elif self.index == 8:
            self.__level8()
            
        self.reset_all_atoms()
        return (self.atoms, self.line1, self.line2, self.required_neutrons)
    
    def reload_last_level(self):
        self.reset_all_atoms()
        return (self.atoms, "", "", -1)
    
    def __level1(self):
        self.atoms = []
        self.atoms.append(neutron_atoms.U235((co.WIDTH - co.U235_SIZE) / 2, (co.HEIGHT - co.U235_SIZE) / 2, 2))
        #
        self.line1 = "Click, drag and release left click to launch a neutron (blue)."
        self.line2 = "Propel it into a fissile atom (pinkish circles) to generate more neutrons !"
        self.required_neutrons = 1
               
    def __level2(self):
        self.atoms = []
        self.atoms.append(neutron_atoms.U235(350, (co.HEIGHT - co.U235_SIZE) / 2, 1))
        self.atoms.append(neutron_atoms.U235(350+229, (co.HEIGHT - co.U235_SIZE) / 2 - 192, 1))
        self.atoms.append(neutron_atoms.U235(350+229, (co.HEIGHT - co.U235_SIZE) / 2 + 192, 1))
        self.atoms.append(neutron_atoms.U235(350+229+300, (co.HEIGHT - co.U235_SIZE) / 2 - 192, 2))
        self.atoms.append(neutron_atoms.U235(350+229+300, (co.HEIGHT - co.U235_SIZE) / 2 + 192, 2))
        #
        self.line1 = "Generated neutrons can also fission others atoms, and thus create a chain reaction!"
        self.line2 = "Leave only stable atoms (gray circles) in a level to complete it."
        self.required_neutrons = 1
        
    def __level3(self):
        self.atoms = []
        self.atoms.append(decaying_atoms.Np239((co.WIDTH - co.U235_SIZE) / 3, (co.HEIGHT - co.U235_SIZE) / 2))
        self.atoms.append(decaying_atoms.Np239((co.WIDTH - co.U235_SIZE) * 2 / 3, (co.HEIGHT - co.U235_SIZE) / 2))
        
        #
        self.line1 = ""
        self.line2 = "Yellow atoms will disintegrate on their own after a while, forming new atoms."
        self.required_neutrons = 1
        
    def __level4(self):
        self.atoms = []
        self.atoms.append(neutron_atoms.U234((co.WIDTH - co.U235_SIZE) / 2, (co.HEIGHT - co.U235_SIZE) / 4, 1))
        self.atoms.append(neutron_atoms.U238((co.WIDTH - co.U235_SIZE) / 2, (co.HEIGHT - co.U235_SIZE) * 2 / 3))
        
        #
        self.line1 = "The last type of atom is the blue one."
        self.line2 = "They will simply transform into another atom when absorbing a neutron."
        self.required_neutrons = 3
        
    def __level5(self):
        self.atoms = []
        self.atoms.append(neutron_atoms.U235((co.WIDTH - co.U235_SIZE) / 4, (co.HEIGHT - co.U235_SIZE) / 2, 0))
        self.atoms.append(neutron_atoms.U235((co.WIDTH - co.U235_SIZE) / 2, (co.HEIGHT - co.U235_SIZE) / 2, 1))
        self.atoms.append(neutron_atoms.U235((co.WIDTH - co.U235_SIZE) * 3 / 4, (co.HEIGHT - co.U235_SIZE) / 2, 2))
        
        
        #
        self.line1 = "Uranium 235 is special as it has 3 forms."
        self.line2 = "They all have different outcomes when they absorb a neutron!"
        self.required_neutrons = 5
        
    def __level6(self):
        self.atoms = []
        for k in range(1, 6):
            self.atoms.append(neutron_atoms.U235((co.WIDTH - co.U235_SIZE) * k / 6, (co.HEIGHT - co.U235_SIZE) / 4, 2))
            self.atoms.append(neutron_atoms.Pu239((co.WIDTH - co.U235_SIZE) * k / 6, (co.HEIGHT - co.U235_SIZE) * 3 / 4))
        for k in range(1, 5):
            self.atoms.append(neutron_atoms.U235((co.WIDTH - co.U235_SIZE) * k / 5, (co.HEIGHT - co.U235_SIZE) / 2, 1))
        
        #
        self.line1 = "Now let's have fun with all the possible reactions!"
        self.line2 = "In the menu you can start a random level if you want to play more :)"
        self.required_neutrons = 1
        
    def __level7(self):
        self.atoms = []
        self.atoms.append(neutron_atoms.U238((co.WIDTH - co.U235_SIZE) / 2, (co.HEIGHT - co.U235_SIZE) / 2))
        self.atoms.append(neutron_atoms.U235((co.WIDTH - co.U235_SIZE) / 2, (co.HEIGHT - co.U235_SIZE) / 6, 1))
        self.atoms.append(neutron_atoms.U235((co.WIDTH - co.U235_SIZE) / 2 - 280, (co.HEIGHT - co.U235_SIZE) / 2 + 100, 1))
        self.atoms.append(neutron_atoms.U235((co.WIDTH - co.U235_SIZE) / 2 + 280, (co.HEIGHT - co.U235_SIZE) / 2 + 100, 1))
        
        #
        self.line1 = self.line2 = ""
        self.required_neutrons = 2
        
    def __level8(self):
        self.atoms = []
        self.atoms.append(neutron_atoms.U238((co.WIDTH - co.U235_SIZE) / 2, (co.HEIGHT - co.U235_SIZE) / 2))
        self.atoms.append(neutron_atoms.U235((co.WIDTH - co.U235_SIZE) / 4, (co.HEIGHT - co.U235_SIZE) / 2, 1))
        self.atoms.append(neutron_atoms.Pu239((co.WIDTH - co.U235_SIZE) * 3 / 4, (co.HEIGHT - co.U235_SIZE) / 2))
          
        #
        self.line1 = ""
        self.line2 = "I ran out of time for more levels, but you can still play random ones!"
        self.required_neutrons = 2
            

    def get_random_atom(self):
        x, y = random.randint(0, co.WIDTH - co.U235_SIZE - 10), random.randint(0, co.HEIGHT - co.U235_SIZE - 10)
        while any(util.is_there_atom_collisions(x, y, atom.x, atom.y) for atom in self.atoms):
            x, y = random.randint(0, co.WIDTH - co.U235_SIZE - 10), random.randint(0, co.HEIGHT - co.U235_SIZE - 10)
        r = random.randint(9, 19)
        if r == 9:
            return neutron_atoms.U235(x, y, 1)
        if r == 10:
            return neutron_atoms.U235(x, y, 2)
        if r == 11:
            return neutron_atoms.U236(x, y)
        if r == 12:
            return decaying_atoms.U237(x, y)
        if r == 13:
            return neutron_atoms.U238(x, y)
        if r == 14:
            return decaying_atoms.U239(x, y)
        if r == 15:
            return neutron_atoms.Np237(x, y)
        if r == 16:
            return decaying_atoms.Np238(x, y)
        if r == 17:
            return decaying_atoms.Np239(x, y)
        if r == 18:
            return decaying_atoms.Pu238(x, y)
        if r == 19:
            return neutron_atoms.Pu239(x, y)
        
    
    def create_random_level(self):
        self.atoms = []
        n_atoms = random.randint(co.RAND_MIN_ATOMS, co.RAND_MAX_ATOMS)
        for i in range(n_atoms):
            self.atoms.append(self.get_random_atom())
        
        return (self.atoms, "", "", -1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    