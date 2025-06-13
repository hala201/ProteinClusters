def load_fasta_sequences(path):
    from Bio import SeqIO
    import pandas as pd

    sequences = []
    cluster_ids = []
    for record in SeqIO.parse(path, "fasta"):
        header_parts = record.description.split(" ")
        cluster_id = header_parts[0]
        sequences.append(str(record.seq))
        cluster_ids.append(cluster_id)

    return pd.DataFrame({"cluster_id": cluster_ids, "sequence": sequences})