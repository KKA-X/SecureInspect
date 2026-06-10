from src.hashing import calculate_sha256

def test_hash_exists(tmp_path):

    f = tmp_path / "sample.txt"

    f.write_text("secureinspect")

    assert len(calculate_sha256(f)) == 64

def test_same_content_same_hash(tmp_path):

    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"

    a.write_text("hello")
    b.write_text("hello")

    assert calculate_sha256(a) == calculate_sha256(b)

def test_different_content_different_hash(tmp_path):

    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"

    a.write_text("one")
    b.write_text("two")

    assert calculate_sha256(a) != calculate_sha256(b)

def test_empty_file_hash(tmp_path):

    f = tmp_path / "empty.txt"

    f.write_text("")

    hash_value = calculate_sha256(f)

    assert len(hash_value) == 64