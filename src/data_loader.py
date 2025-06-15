def load_fasta_sequences(path):
    from Bio import SeqIO
    import pandas as pd

    sequences = []
    cluster_ids = []
    for record in SeqIO.parse(path, "fasta"):
        header = record.description  # e.g., sp|A4GCJ4|RDRP_I36A0
        try:
            family_code = header.split("|")[2].split("_")[0]  # e.g., RDRP from RDRP_I36A0
        except IndexError:
            family_code = "UNKNOWN"
        sequences.append(str(record.seq))
        cluster_ids.append(family_code)

    return pd.DataFrame({"cluster_id": cluster_ids, "sequence": sequences})