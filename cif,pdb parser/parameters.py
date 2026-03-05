from Bio.PDB import PDBParser

atom_parameters = {
    "H": {"mass": 1.008, "charge": 0.1, "radius": 1.2},
    "C": {"mass": 12.011, "charge": 0.0, "radius": 1.7},
    "N": {"mass": 14.007, "charge": -0.3, "radius": 1.55},
    "O": {"mass": 15.999, "charge": -0.5, "radius": 1.52},
    "S": {"mass": 32.06, "charge": -0.2, "radius": 1.8},
}

parser=PDBParser(PERMISSIVE=True)
structure=parser.get_structure("protein","protein.pdb")

atom_data = []

for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                element=atom.element
                params=atom_parameters.get(element)
                if params:
                    mass=params["mass"]
                    charge=params["charge"]
                    radius=params["radius"]

                    atom_data.append({
                        "chain": chain.id,
                        "residue": residue.resname,
                        "atom": atom.get_name(),
                        "mass": mass,
                        "charge": charge,
                        "radius": radius
                    })

for atom in atom_data:
    print(
        atom["chain"],
        atom["residue"],
        atom["atom"],
        atom["mass"],
        atom["charge"],
        atom["radius"]
    )