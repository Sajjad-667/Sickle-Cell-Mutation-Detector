# 🧬 Sickle Cell Mutation Detector

This Python project detects the **sickle cell mutation** in a DNA sequence, locates the mutation position, and compares the translated protein sequences of the normal and mutated DNA. The sickle cell mutation occurs when the codon **GAG** (glutamic acid) is replaced by **GTG** (valine) in the hemoglobin gene.

---

## 📌 Features

- Detects presence of the sickle cell mutation (GTG codon).
- Identifies the position of the mutation in the DNA sequence.
- Translates both normal and mutated DNA to protein.
- Provides side-by-side protein sequence comparison.

---

## 🧪 Example

```
Normal sequence:
✅ No sickle cell mutation detected.

Sickle cell sequence:
⚠️ Sickle cell mutation detected (GTG codon found).

--- Mutation Position Check ---
⚠️ Mutation (GTG) found at position 4 (0-based index).
ℹ️ Expected normal codon (GAG) would be at the same position.

--- Protein Translation ---
Normal Protein: PPEKVAVNALPGGKVNVDEVVRAWG
Sickle Protein: PVKVAVNALPGGKVNVDEVVRAWG
```

---

## 🚀 Requirements

- Python 3.7+
- [Biopython](https://biopython.org/)

Install Biopython:

```bash
pip install biopython
```

---

## 📂 Files

- `main.py` – Contains all mutation detection and translation logic.
- `README.md` – Documentation for setup and usage.

---

## 📥 Usage

Run the Python script using:

```bash
python main.py
```

You can replace the `normal_seq` and `sickle_seq` variables with your own DNA sequences to test for mutation.

---

## 📘 Background

The sickle cell disease is caused by a **point mutation** in the β-globin gene of hemoglobin. This tool demonstrates a basic form of genetic sequence analysis using Python and BioPython.

---

## 🧑‍🔬 Author

Developed by [Your Name] – for educational and bioinformatics practice.

---

## 📜 License

This project is licensed under the MIT License.
