from main import get_descendants_uuids_by_type

def test_get_descendants_uuids_by_type():
    descendants = [{ 'uuid': 'apple', 'entity_type': 'Sample'}, { 'uuid' : 'lemon', 'entity_type': 'Dataset'}, { 'uuid': 'lime', 'entity_type': 'Sample'}]
    output = {
        'Dataset': ['lemon'],
        'Sample': ['apple', 'lime'],
    }
    assert get_descendants_uuids_by_type(descendants) == output
