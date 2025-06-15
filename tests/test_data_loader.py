from data_loader import load_fasta_sequences

def test_load_fasta_sequences():
    df = load_fasta_sequences("tests/data/test.fasta")
    assert "sequence" in df.columns
    assert "cluster_id" in df.columns
    assert len(df) > 0
