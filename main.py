from Bio.Seq import Seq

# Function to check for the sickle cell mutation in a DNA sequence
def check_sickle_cell_mutation(dna_seq):
    # The mutation occurs when the normal codon GAG (glutamic acid) is replaced by GTG (valine)
    if "GTG" in dna_seq:
        print("⚠️ Sickle cell mutation detected (GTG codon found).")
    else:
        print("✅ No sickle cell mutation detected.")

# Example sequences
normal_seq = "CCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAG"
sickle_seq = "CCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAG"

# Checking both sequences
print("Normal sequence:")
check_sickle_cell_mutation(normal_seq)

print("\nSickle cell sequence:")
check_sickle_cell_mutation(sickle_seq)

# Function to locate the mutation codon (GTG) in the DNA sequence
def find_mutation_position(dna_seq):
    normal_codon = "GAG"
    mutation_codon = "GTG"
    
    # Find the index of the mutated codon
    pos = dna_seq.find(mutation_codon)
    
    if pos != -1:
        print(f"⚠️ Mutation (GTG) found at position {pos} (0-based index).")
        print(f"ℹ️ Expected normal codon (GAG) would be at the same position.")
    else:
        print("✅ No sickle cell mutation (GTG) found in the sequence.")

# Using the sickle cell sequence
print("\n--- Mutation Position Check ---")
find_mutation_position(sickle_seq)

# Convert the DNA sequences to Biopython Seq objects for translation
normal_dna = Seq(normal_seq)
sickle_dna = Seq(sickle_seq)

# Translate DNA to protein (until the first stop codon)
print("\n--- Protein Translation ---")
print("Normal Protein:", normal_dna.translate(to_stop=True))
print("Sickle Protein:", sickle_dna.translate(to_stop=True))