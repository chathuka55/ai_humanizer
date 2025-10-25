from humanizer.main import humanizer_pipeline

def test_pipeline_runs():
    sample = "Artificial intelligence is changing technology rapidly."
    output = humanizer_pipeline(sample)
    assert isinstance(output, str)
    assert len(output) > 0