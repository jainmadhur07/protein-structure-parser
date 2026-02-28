import os
from Bio.PDB import PDBParser, MMCIFParser

pdb_file = "1BRS.pdb"
cif_file = "1BRS.cif"

if os.path.exists(pdb_file):
    print("=== PDB ===")
    parser = PDBParser(PERMISSIVE=True)
    structure = parser.get_structure("1BRS", pdb_file)
    chain_count = {}

    for model in structure:
        for chain in model:
            original_id = chain.id

            if original_id not in chain_count:
                chain_count[original_id] = 1
            else:
                chain_count[original_id] += 1

            new_chain_id = f"{original_id}{chain_count[original_id]}"

            for residue in chain:
                for atom in residue:
                    print(new_chain_id, residue.resname, atom.get_name(), atom.get_coord())



if os.path.exists(cif_file):
    print("\n=== CIF ===")
    parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure("1BRS", cif_file)
    chain_count = {}

    for model in structure:
        for chain in model:
            original_id = chain.id

            if original_id not in chain_count:
                chain_count[original_id] = 1
            else:
                chain_count[original_id] += 1

            new_chain_id = f"{original_id}{chain_count[original_id]}"

            for residue in chain:
                for atom in residue:
                    print(new_chain_id, residue.resname, atom.get_name(), atom.get_coord())

if not os.path.exists(pdb_file) and not os.path.exists(cif_file):
    print("No PDB or CIF file found.")