import app  # Import the main application module

def test_main_function(capsys):
    # Run the main function from app.py
    app.main()
    
    # Capture the stdout output
    captured = capsys.readouterr()
    
    # Check if expected messages are present in output
    assert "Serving HTTP on port" in captured.out
