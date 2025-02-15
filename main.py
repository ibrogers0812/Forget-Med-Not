# Ensure 2 blank lines before this function
from app import create_app

def main():
    app = create_app()
    app.run(host='0.0.0.0', port=5000)

# Call the main function when this script is run
if __name__ == "__main__":
    main()
